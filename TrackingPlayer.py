from AttackDirection import AttackDirection
from Coord import Coord
from TeamType import TeamType


class TrackingPlayer:
	def __init__(self, team, systemId, number, xCoord, yCoord, speed):
		self.number = number
		self.coord = Coord(xCoord, yCoord)
		self.systemId = systemId
		self.team_type = team
		self.speed = speed

	def is_referee(self):
		return self.team_type == 4 or self.team_type == -1

	def is_player(self):
		return not self.is_referee()

	def __str__(self):
		return 'Number: {0}, x: {1}, y: {2}'.format(self.number, self.coord.x, self.coord.y)

	def is_between_own_goal_and_ball(self, opposite_team_attack_direction, ball):
		if opposite_team_attack_direction == AttackDirection.LEFT:
			return self.coord.x < ball.coord.x
		else:
			return self.coord.x > ball.coord.x


def from_line(participant_as_line) -> "TrackingPlayer":
	items = participant_as_line.split(",")
	if int(items[0]) == 1:
		team = TeamType.HOME
	elif int(items[0]) == 0:
		team = TeamType.AWAY
	else:
		team = TeamType.UNDEFINED
	systemId = int(items[1])
	number = int(items[2])
	xCoord = int(items[3])
	yCoord = int(items[4])
	speed = float(items[5])
	return TrackingPlayer(team, systemId, number, xCoord, yCoord, speed)
