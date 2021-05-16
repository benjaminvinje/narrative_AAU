from Event import Event
from EventPlayer import EventPlayer
from GameSummary import GameSummary
from Position import Position
from Qualifier import Qualifier
from Team import Team
from TeamType import TeamType
from my_xml import XmlHelper
from my_xml.XmlAttributes import XmlAttributes
from my_xml.XmlLoader import XmlLoader
from my_xml.XmlTags import XmlTags


class MA3XmlLoader(XmlLoader):

	def load(self, game, use_original_file):
		self.load_event_data(game, use_original_file)
		self.load_teams(game)
		self.load_players_from_xml(game)
		self.load_game_summary(game)

	def load_event_data(self, game, use_original_file=False):
		game.events = []
		if use_original_file:
			mydoc = XmlHelper.load_xml(game.event_data_path)
			xml_events = mydoc.getElementsByTagName(XmlTags.EVENT_MA3)
		else:
			try:
				mydoc = XmlHelper.load_xml(game.event_data_improved_path)
				xml_events = mydoc.getElementsByTagName(XmlTags.EVENT)
				for idx, xml_event in enumerate(xml_events):
					event = self.create_event_based_on_xml(xml_event)
					game.events.append(event)
				return

			except FileNotFoundError:
				mydoc = XmlHelper.load_xml(game.event_data_path)
				xml_events = mydoc.getElementsByTagName(XmlTags.EVENT_MA3)

		for idx, xml_event in enumerate(xml_events):
			event = self.create_event_based_on_xml_ma3(xml_event)
			game.events.append(event)

	def create_event_based_on_xml_ma3(self, xml_event):
		attrs = xml_event.attributes
		event_id = attrs[XmlAttributes.EVENT_ID_MA3].value
		id = attrs[XmlAttributes.ID].value
		last_modified = attrs[XmlAttributes.LAST_MODIFIED_MA3].value
		min = attrs[XmlAttributes.MIN_MA3].value
		outcome = attrs[XmlAttributes.OUTCOME].value
		period_id = attrs[XmlAttributes.PERIOD_ID_MA3].value
		sec = attrs[XmlAttributes.SEC_MA3].value
		team_id = attrs[XmlAttributes.CONTESTANT_ID_MA3].value
		timestamp = attrs[XmlAttributes.TIMESTAMP_MA3].value
		type_id = attrs[XmlAttributes.TYPE_ID_MA3].value
		version = None
		x = attrs[XmlAttributes.X].value
		y = attrs[XmlAttributes.Y].value
		player_id = self.try_loading_attr(attrs, XmlAttributes.PLAYER_ID_MA3)
		reception_id = self.try_loading_attr(attrs, XmlAttributes.RECEPTION_ID)
		player_corrected = self.try_loading_attr(attrs, XmlAttributes.PLAYER_CORRECTED)
		frame_id = self.try_loading_attr(attrs, XmlAttributes.FRAME_ID)

		event = Event(id, event_id, type_id, period_id, min, sec, team_id, outcome, x, y, timestamp, last_modified,
					  version, player_id)
		event.reception_id = reception_id
		event.player_corrected = player_corrected
		event.frame_id = int(frame_id) if frame_id is not None else None

		qualifiers = xml_event.getElementsByTagName(XmlTags.QUALIFIER_MA3)
		for q in qualifiers:
			attrs = q.attributes
			qualifier_id = attrs[XmlAttributes.QUALIFIER_ID_MA3].value
			q_id = attrs[XmlAttributes.ID].value
			value = self.try_loading_attr(attrs, XmlAttributes.VALUE)

			qualifier = Qualifier(q_id, qualifier_id, value)
			event.qualifiers.append(qualifier)
		return event

	def load_teams(self, game):
		game.teams = []
		doc = XmlHelper.load_xml(game.match_data_path)
		xml_teamdata = doc.getElementsByTagName(XmlTags.CONTESTANT_MA3)

		for team in xml_teamdata:
			side = team.attributes[XmlAttributes.POSITION_MA3].value
			s = TeamType(side[0].upper())
			ref = team.attributes[XmlAttributes.ID].value
			name = team.attributes[XmlAttributes.NAME].value
			direction1 = game.determine_attack_direction(ref, 1)
			direction2 = game.determine_attack_direction(ref, 2)
			team = Team(ref, s, direction1, direction2)
			team.name = name
			game.teams.append(team)

	def load_players_from_xml(self, game):
		game.players = []
		doc = XmlHelper.load_xml(game.match_data_path)
		xml_teamdata = doc.getElementsByTagName(XmlTags.LINEUP)

		for team in xml_teamdata:
			xml_players = team.getElementsByTagName(XmlTags.PLAYER_MA3)
			team_id = team.attributes[XmlAttributes.CONTESTANT_ID_MA3].value
			for xml_player in xml_players:
				player = self.create_player_based_on_xml(game, xml_player, team_id)
				game.players.append(player)

	def create_player_based_on_xml(self, game, xml_player, team_id):
		attrs = xml_player.attributes
		formation_place = self.try_loading_attr(attrs, XmlAttributes.FORMATION_PLACE_MA3)
		formation_place = 0 if formation_place is None else formation_place

		playerref = attrs[XmlAttributes.PLAYER_ID_MA3].value
		position = Position(attrs[XmlAttributes.POSITION_MA3].value)
		shirtnumber = attrs[XmlAttributes.SHIRTNUMBER_MA3].value

		team = game.get_team_by_id(team_id)

		player = EventPlayer(formation_place, playerref, position, None, shirtnumber, None, None, team.team_type,
							 team)
		player.first_name = attrs[XmlAttributes.FIRST_NAME_MA3].value
		player.last_name = attrs[XmlAttributes.LAST_NAME_MA3].value
		return player

	def load_game_summary(self, game):
		mydoc = XmlHelper.load_xml(game.event_data_path)
		match_info = mydoc.getElementsByTagName(XmlTags.MATCH_INFO)[0]
		id = match_info.attributes[XmlAttributes.ID].value
		game_date = match_info.attributes[XmlAttributes.DATE].value
		week = match_info.attributes[XmlAttributes.WEEK].value
		matchday = "{0}".format(week)

		total = mydoc.getElementsByTagName(XmlTags.TOTAL)[0]
		home_score = total.attributes[XmlAttributes.HOME].value
		away_score = total.attributes[XmlAttributes.AWAY].value

		competition = mydoc.getElementsByTagName(XmlTags.COMPETITION)[0]
		competition_name = competition.attributes[XmlAttributes.NAME].value
		competition_id = competition.attributes[XmlAttributes.ID].value

		torunament_calendar = mydoc.getElementsByTagName(XmlTags.TOURNAMENT_CALENDAR)[0]
		season_name = torunament_calendar.firstChild.nodeValue
		season_id = torunament_calendar.attributes[XmlAttributes.ID].value

		periods = mydoc.getElementsByTagName(XmlTags.PERIOD)
		for period in periods:
			period_id = period.attributes[XmlAttributes.ID].value
			if period_id == "1":
				period_1_start = period.attributes[XmlAttributes.START].value
			else:
				period_2_start = period.attributes[XmlAttributes.START].value

		contestants = mydoc.getElementsByTagName(XmlTags.CONTESTANT_MA3)
		for xml_contestant in contestants:
			position = xml_contestant.attributes[XmlAttributes.POSITION_MA3].value
			if position == "home":
				home_team_name = xml_contestant.attributes[XmlAttributes.NAME].value
				home_team_id = xml_contestant.attributes[XmlAttributes.ID].value
			else:
				away_team_name = xml_contestant.attributes[XmlAttributes.NAME].value
				away_team_id = xml_contestant.attributes[XmlAttributes.ID].value

		game.game_summary = GameSummary(id, away_score, away_team_id, away_team_name, competition_id, competition_name,
										game_date, home_score, home_team_id, home_team_name, matchday, period_1_start,
										period_2_start, season_id, season_name)

		return game.game_summary

	def create_game_summary_based_on_xml(self, game, xml_game):
		attrs = xml_game.attributes
		id = attrs[XmlAttributes.ID].value
		away_score = attrs[XmlAttributes.AWAY_SCORE].value
		away_team_id = attrs[XmlAttributes.AWAY_TEAM_ID].value
		away_team_name = attrs[XmlAttributes.AWAY_TEAM_NAME].value
		competition_id = attrs[XmlAttributes.COMPETITION_ID].value
		competition_name = attrs[XmlAttributes.COMPETITION_NAME].value
		game_date = attrs[XmlAttributes.GAME_DATE].value
		home_score = attrs[XmlAttributes.HOME_SCORE].value
		home_team_id = attrs[XmlAttributes.HOME_TEAM_ID].value
		home_team_name = attrs[XmlAttributes.HOME_TEAM_NAME].value
		matchday = attrs[XmlAttributes.MATCHDAY].value
		period_1_start = attrs[XmlAttributes.PERIOD_1_START].value
		period_2_start = attrs[XmlAttributes.PERIOD_2_START].value
		season_id = attrs[XmlAttributes.SEASON_ID].value
		season_name = attrs[XmlAttributes.SEASON_NAME].value

		game.game_summary = GameSummary(id, away_score, away_team_id, away_team_name, competition_id, competition_name,
										game_date, home_score, home_team_id, home_team_name, matchday, period_1_start,
										period_2_start, season_id, season_name)
