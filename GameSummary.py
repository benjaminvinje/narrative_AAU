class GameSummary:
	def __init__(self, id, away_score, away_team_id, away_team_name, competition_id, competition_name, game_date,
				 home_score, home_team_id, home_team_name, matchday, period_1_start, period_2_start, season_id,
				 season_name):
		self.id = id
		self.away_score = away_score
		self.away_team_id = away_team_id
		self.away_team_name = away_team_name
		self.competition_id = competition_id
		self.competition_name = competition_name
		self.game_date = game_date
		self.home_score = home_score
		self.home_team_id = home_team_id
		self.home_team_name = home_team_name
		self.matchday = matchday
		self.period_1_start = period_1_start
		self.period_2_start = period_2_start
		self.season_id = season_id
		self.season_name = season_name
