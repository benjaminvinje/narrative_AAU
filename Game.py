import os
import time
from bisect import bisect_left
from collections import Counter

import numpy as np

import Frame
import MathHelper
from AttackDirection import AttackDirection
from Coord import Coord
from Event import Event
from QuallifierType import QualifierType
from TeamType import TeamType
from my_xml import XmlHelper
from my_xml.XmlAttributes import XmlAttributes
from my_xml.XmlTags import XmlTags
from EventType import EventType


class Game:
	def __init__(self, location_data, event_data, match_data, meta_data, summary_path, lines, loader):
		self.frames = []
		self.frame_ids = []
		self.match_data_path = match_data
		self.event_data_path = event_data
		self.meta_data_path = meta_data
		self.location_data_path = location_data
		self.summary_path = summary_path
		_, self.filename = os.path.split(location_data)
		self.number_of_lines_to_load = lines
		self.first_period_frame_id = 0
		self.events = []
		self.players = []
		self.teams = []
		self.game_summary = None
		self.position_frequency = 25  # [Hz]
		self.period_metadata = None
		self.match_metadata = None
		# self.loader = MA3XmlLoader()
		self.loader = loader
		self.aligning_stats = None

	def load(self):
		self.load_xml_data()
		self.load_location_data()
		self.events.sort(key=lambda event: (event.period_id, event.min, event.sec, event.same_minute_order()))

	def load_xml_data(self, use_original_file=False):
		self.loader.load(self, use_original_file)
		self.period_metadata = self.load_metadata_period()
		self.match_metadata = self.load_metadata_match()
		self.first_period_frame_id = self.get_frame_id_By_Xml_Attribute(XmlAttributes.ISTARTFRAME, 1)
		self.first_period_end_frame_id = self.get_frame_id_By_Xml_Attribute(XmlAttributes.IENDFRAME, 1)
		self.second_period_frame_id = self.get_frame_id_By_Xml_Attribute(XmlAttributes.ISTARTFRAME, 2)
		self.second_period_end_frame_id = self.get_frame_id_By_Xml_Attribute(XmlAttributes.IENDFRAME, 2)
		self.position_frequency = int(self.match_metadata[0].attributes[XmlAttributes.FREQUENCY].value)

	def load_location_data(self):
		start = time.time()
		lines = 0
		self.frames = []

		path = self.location_data_path

		used_location_file = self.location_data_path
		for line in open(used_location_file, 'r'):
			line = line.rstrip()

			lines += 1
			frame = Frame.from_line(line)
			if len(self.frames) > 1:
				frame.ball.speed, frame.ball.vector = MathHelper.calculate_ball_movement(frame, self.frames[-1])

			self.frames.append(frame)
			for frame_event in frame.frame_events:
				event = self.get_event_by_event_id(frame_event.id)
				if event is None:
					continue

				event.frame_id = frame_event.frame_id

			if lines == self.number_of_lines_to_load:  # Load only the beginning of the game
				break
		self.frame_ids = [f.id for f in self.frames]

		end = time.time()
		print(
			"The game contains {0} lines which corresponds to {1:.2f} minutes of the game.".format(len(self.frames),
																								   len(self.frames) / (
																									   self.position_frequency) / 60))
		elapsed_time = end - start
		print("Loading location took {0:.2f} seconds".format(elapsed_time))

	def load_metadata_period(self):
		doc = XmlHelper.load_xml(self.meta_data_path)
		return doc.getElementsByTagName(XmlTags.PERIOD)

	def load_metadata_match(self):
		doc = XmlHelper.load_xml(self.meta_data_path)
		return doc.getElementsByTagName(XmlTags.MATCH)

	def load_game_summary(self):
		summary = self.loader.load_game_summary(self)
		return summary

	def get_frame_id_By_Xml_Attribute(self, xml_attribute, part):
		frame_id = None
		for period in self.period_metadata:
			if int(period.attributes[XmlAttributes.IID].value) == part:
				frame_id = int(period.attributes[xml_attribute].value)
				break
		return frame_id

	def get_index_by_id(self, id):
		if id < self.frames[0].id:
			return 0

		i = bisect_left(self.frame_ids, id)
		if i != len(self.frame_ids) and self.frame_ids[i] == id:
			return i
		raise ValueError

	def get_tracking_player_from_event(self, event, frame):
		if event.player_id is None:
			return None

		player = event.player
		return self.get_tracking_player_from_event_player(player, frame)

	def get_tracking_player_from_event_player(self, event_player, frame):
		if event_player is None:
			return None
		return next(
			(p for p in frame.players if p.number == event_player.number and p.team_type == event_player.team_type),
			None)

	def get_event_player_from_event(self, event):
		if event.player_id is None:
			return None

		for player in self.players:
			if event.player_id == player.player_ref:
				return player
		return None

	def get_event_player_by_tracking_player(self, track_player):
		for event_player in self.players:
			try:
				if event_player.number == track_player.number and event_player.team_type == track_player.team_type:
					return event_player
			except AttributeError:
				print("s")
		return None

	def get_pitch_dimensions(self):
		width = float(self.match_metadata[0].attributes[XmlAttributes.PITCH_WIDTH_METERS].value)
		height = float(self.match_metadata[0].attributes[XmlAttributes.PITCH_HEIGHT_METERS].value)
		return width, height

	def get_tracking_player_closest_to_ball(self, index):
		min_dist = 100000000
		closest_player = None
		try:
			correct_players = list(filter(lambda p: p.number != -1, self.frames[index].players))
		except IndexError:
			print("error1")
		for player in correct_players:
			dist = MathHelper.dist_between(player.coord, self.frames[index].ball.coord)
			if dist < min_dist:
				closest_player = player
				min_dist = dist

		if closest_player is None:
			print("error2")
		return closest_player

	def get_tracking_player_by_frame_index_and_track_player(self, index, track_player):
		if track_player is None:
			return track_player
		for player in self.frames[index].players:
			if player.number == track_player.number and player.team_type == track_player.team_type:
				return player
		return None


	def set_events_coords(self, event):
		factor = 1
		# in first period away team is in right half
		if event.team_id == self.get_team_by_team_type(TeamType.AWAY).id and event.period_id == 1:
			factor = -1
		# in second period home team is in the right half
		if event.team_id == self.get_team_by_team_type(TeamType.HOME).id and event.period_id == 2:
			factor = -1

		# set track position of an event from home team perspective in the first half (on left side)
		width, height = self.get_pitch_dimensions()
		x = event.x
		y = event.y
		x = width * (x / 100)
		y = height * (y / 100)
		x = x - width / 2
		y = y - height / 2
		x *= 100
		y *= 100
		x *= factor
		y *= factor
		event.coord.x = x
		event.coord.y = y

		if event.has_end_coords():
			x = float(event.get_qualifier_value(QualifierType.PASS_END_X))
			y = float(event.get_qualifier_value(QualifierType.PASS_END_Y))
			x = width * (x / 100)
			y = height * (y / 100)
			x = x - width / 2
			y = y - height / 2
			x *= 100
			y *= 100
			x *= factor
			y *= factor
			event.coord_end = Coord(x, y)

	def set_event_position_by_track_player(self, event, track_player):
		width, height = self.get_pitch_dimensions()

		x = track_player.coord.x
		y = track_player.coord.y
		x = x + width * 100 / 2
		y = y + height * 100 / 2
		x = x / width
		y = y / height
		# in first period away team is in right half
		if event.team_id == self.get_team_by_team_type(TeamType.AWAY).id and event.period_id == 1:
			x = 100 - x
			y = 100 - y
		# in second period home team is in the right half
		if event.team_id == self.get_team_by_team_type(TeamType.HOME).id and event.period_id == 2:
			x = 100 - x
			y = 100 - y

		event.x = x
		event.y = y

	def get_index_by_time(self, minute, second, period):
		sec_since_period_start = minute * 60 + second - (period - 1) * 45 * 60
		if period == 1:
			return self.get_index_by_id(
				self.first_period_frame_id) + sec_since_period_start * self.position_frequency
		else:
			return self.get_index_by_id(
				self.second_period_frame_id) + sec_since_period_start * self.position_frequency

	def get_surrounding_aligned_events(self, event):
		idx = self.events.index(event)
		after_event = None
		before_event = None
		for i in range(idx + 1, len(self.events)):
			if self.events[i].is_aligned():
				after_event = self.events[i]
				break
		for i in range(idx - 1, 0, -1):
			if self.events[i].is_aligned():
				before_event = self.events[i]
				break

		return before_event, after_event


	def get_event_by_event_id(self, id):
		for event in self.events:
			if event.id == id:
				return event
		return None

	def get_players_by_team_type_from_frame(self, team, frame):
		return [player for player in frame.players if player.team_type == team]

	# if diff is positive, the event according to alignment happened later than in raw event data
	def get_aligned_event_time_difference(self, event):
		if not event.is_aligned():
			return 0

		if event.period_id == 1:
			frames_from_start_to_event = event.frame_id - self.first_period_frame_id
			event_orig_time_in_frames = self.position_frequency * (event.min * 60 + event.sec)
			diff = frames_from_start_to_event - event_orig_time_in_frames
			return diff

		elif event.period_id == 2:
			frames_from_period_start_to_event = event.frame_id - self.second_period_frame_id
			event_orig_time_in_frames = self.position_frequency * ((event.min - 45) * 60 + event.sec)
			diff = frames_from_period_start_to_event - event_orig_time_in_frames
			return diff

	def get_team_by_id(self, id):
		for team in self.teams:
			if team.id == id:
				return team
		return None

	def get_team_by_team_type(self, team_type):
		for team in self.teams:
			if team.team_type == team_type:
				return team
		return None

	def get_goals_by_team_type_and_frame(self, team_type, frame):
		# find goal events before given frame
		goal_events = [event for event in self.events if event.type == EventType.GOAL]
		team = self.get_team_by_team_type(team_type)
		goals = 0
		for event in goal_events:
			if not event.is_aligned():
				continue
			if event.frame_id < frame.id and event.team_id == team.id:
				goals += 1
		return goals

	def get_event_index_by_event(self, event):
		self.events.index(event)

	def get_player_by_id(self, ref):
		for player in self.players:
			if player.player_ref == ref:
				return player
		return None

	def get_team_by_name(self, name):
		for team in self.teams:
			if team.name == name:
				return team
		return None

	def get_period_id_of_frame(self, frame):
		if frame.id < self.second_period_frame_id:
			return 1
		return 2

	def contains_reception_events(self):
		for event in self.events:
			if event.type == EventType.RECEPTION:
				return True
		return False

	def get_aligned_events(self):
		return [event for event in self.events if event.is_aligned()]

	def get_frame_by_id(self, id):
		idx = self.get_index_by_id(id)
		return self.frames[idx]

	def determine_attack_direction(self, team_id, period_id):
		period_start_event = [event for event in self.events if
							  event.type == EventType.START and event.period_id == period_id and event.team_id == team_id]
		text = period_start_event[0].get_qualifier_value(QualifierType.DIRECTION_OF_PLAY)
		if text == "Left to Right":
			return AttackDirection.RIGHT
		else:
			return AttackDirection.LEFT

