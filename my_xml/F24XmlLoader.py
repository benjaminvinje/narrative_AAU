import re

from my_xml import XmlHelper
from Event import Event
from EventPlayer import EventPlayer
from GameSummary import GameSummary
from my_xml.XmlLoader import XmlLoader
from Position import Position
from Qualifier import Qualifier
from Team import Team
from TeamType import TeamType
from my_xml.XmlAttributes import XmlAttributes
from my_xml.XmlTags import XmlTags


class F24XmlLoader(XmlLoader):

	def load(self, game, use_original_file):
		self.load_event_data(game, use_original_file)
		self.load_teams(game)
		self.load_players_from_xml(game)
		self.load_player_names(game)
		self.load_game_summary(game)

	def load_event_data(self, game, use_original_file=False):
		game.events = []
		mydoc = XmlHelper.load_xml(game.event_data_path)
		xml_events = mydoc.getElementsByTagName(XmlTags.EVENT)

		for idx, xml_event in enumerate(xml_events):
			event = self.create_event_based_on_xml(xml_event)
			game.events.append(event)

	def load_teams(self, game):
		game.teams = []
		doc = XmlHelper.load_xml(game.match_data_path)
		xml_teamdata = doc.getElementsByTagName(XmlTags.TEAMDATA)

		for team in xml_teamdata:
			side = team.attributes[XmlAttributes.SIDE].value
			s = TeamType(side[0])
			ref = team.attributes[XmlAttributes.TEAM_REF].value
			# if team ref has a form "t1234", then remove 't' from the variable, because it is not used anywhere else - needed to accomodate MA3 files
			if re.fullmatch("[t]\d{3,5}", ref):
				ref = ref.lstrip('t')
			direction1 = game.determine_attack_direction(ref, 1)
			direction2 = game.determine_attack_direction(ref, 2)
			game.teams.append(Team(ref, s, direction1, direction2))

		xml_teams = doc.getElementsByTagName(XmlTags.TEAM)
		for xml_team in xml_teams:
			ref = xml_team.attributes[XmlAttributes.UID].value
			if re.fullmatch("[t]\d{3,5}", ref):
				ref = ref.lstrip('t')
			game_team = game.get_team_by_id(ref)
			country = xml_team.getElementsByTagName(XmlTags.COUNTRY)[0].firstChild.nodeValue
			game_team.country = country
			name = xml_team.getElementsByTagName(XmlTags.NAME)[0].firstChild.nodeValue
			game_team.name = name

	def load_players_from_xml(self, game):
		game.players = []
		doc = XmlHelper.load_xml(game.match_data_path)
		xml_teamdata = doc.getElementsByTagName(XmlTags.TEAMDATA)

		for team in xml_teamdata:
			xml_players = team.getElementsByTagName(XmlTags.MATCHPLAYER)
			side = team.attributes[XmlAttributes.SIDE].value
			s = TeamType(side[0])
			for xml_player in xml_players:
				player = self.create_player_based_on_xml(game, xml_player, s)
				game.players.append(player)

	def create_player_based_on_xml(self, game, xml_player, side):
		attrs = xml_player.attributes
		formation_place = self.try_loading_attr(attrs, XmlAttributes.FORMATION_PLACE)
		if formation_place is None:  # in case the formation is given in Stat tag, we have to use different method of loading it
			formation_place = self.load_value_from_tag(xml_player, XmlTags.STAT, XmlAttributes.FORMATION_PLACE)

		playerref = attrs[XmlAttributes.PLAYERREF].value
		# if player ref has a form "p12345", then remove 'p' from the variable, because it is not used anywhere else.
		# (players IDs in events do not include the 'p') - needed to accomodate MA3 files
		if re.fullmatch("[p]\d{4,6}", playerref):
			playerref = playerref.lstrip('p')

		position = Position(attrs[XmlAttributes.POSITION].value)
		shirtnumber = attrs[XmlAttributes.SHIRTNUMBER].value
		status = attrs[XmlAttributes.STATUS].value

		subposition = self.try_loading_attr(attrs, XmlAttributes.SUBPOSITION)
		captain = self.try_loading_attr(attrs, XmlAttributes.CAPTAIN)

		team = game.get_team_by_team_type(side)

		player = EventPlayer(formation_place, playerref, position, subposition, shirtnumber, status, captain, side,
							 team)
		return player

	def load_player_names(self, game):
		doc = XmlHelper.load_xml(game.match_data_path)
		xml_players = doc.getElementsByTagName(XmlTags.PLAYER)
		for xml_player in xml_players:
			ref = xml_player.attributes[XmlAttributes.UID].value
			ref = ref.replace("p", "")
			personname = xml_player.getElementsByTagName(XmlTags.PERSONNAME)[0]
			first_name = personname.getElementsByTagName(XmlTags.FIRST)[0].firstChild.nodeValue
			last_name = personname.getElementsByTagName(XmlTags.LAST)[0].firstChild.nodeValue
			player = game.get_player_by_id(ref)
			if player is not None:
				player.first_name = first_name
				player.last_name = last_name

	def load_game_summary(self, game):
		mydoc = XmlHelper.load_xml(game.event_data_path)
		xml_game = mydoc.getElementsByTagName(XmlTags.GAME)
		summary = self.create_game_summary_based_on_xml(game, xml_game[0])
		return summary

	def create_game_summary_based_on_xml(self,game, xml_game):
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

