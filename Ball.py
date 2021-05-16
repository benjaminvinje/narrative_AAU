from Coord import Coord
from TeamType import TeamType


class Ball:
	def __init__(self, xCoord, yCoord, zCoord, alive, team_possession):
		self.coord = Coord(xCoord, yCoord, zCoord)
		self.alive = alive
		self.possession = team_possession
		self.speed = 0
		self.vector = None

	def is_alive(self):
		return self.alive

	def is_dead(self):
		return not self.alive

	def is_dying(self, next_frame):
		return self.is_alive() and next_frame.ball.is_dead()

	def __str__(self):
		return 'x: {}, y: {}, z: {}, [{}, {}, {}]'.format(self.coord.x, self.coord.y, self.coord.z, self.vector[0],self.vector[1],self.vector[2])


def from_line(ball_as_line) -> "Ball":
	ball_as_line = ball_as_line.replace(";", "")
	items = ball_as_line.split(",")
	xCoord = int(items[0])
	yCoord = int(items[1])
	zCoord = int(items[2])
	# unknown_parameter = float(items[3])
	poss = TeamType(items[4])
	alive = items[5] == "Alive"
	return Ball(xCoord, yCoord, zCoord, alive, poss)
