

class Team:
	def __init__(self, id, team_type, direction, direction2):
		self.id = id
		self.team_type = team_type
		self.country = None
		self.name = None
		self.kit = None
		self.first_half_direction = direction
		self.second_half_direction = direction2

	def __str__(self):
		return "{0}".format(self.name)
