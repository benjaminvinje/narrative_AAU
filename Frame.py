import Ball
import FrameEvent
import TrackingPlayer


class Frame:
	def __init__(self, id, players, ball, events):
		self.id = id
		self.players = players
		self.ball = ball
		self.frame_events = events


	def __str__(self):
		return 'ball: [{}, {}, {}]'.format(self.ball.vector[0], self.ball.vector[1], self.ball.vector[2])


def from_line(frame_as_line) -> "Frame":
	items = frame_as_line.split(":")
	id = int(items[0])
	players = create_players(items[1])
	ball = Ball.from_line(items[2])
	events = []
	if items[3] is not "":
		events = create_events_list(items[3], id)
	return Frame(id, players, ball, events)


def create_players(param):
	items = param.split(";")
	retval = []
	for item in items[:-1]:
		retval.append(TrackingPlayer.from_line(item))
	return retval


def create_events_list(param, frame_id):
	items = param.split(";")
	retval = []
	for item in items[:-1]:
		retval.append(FrameEvent.from_line(item, frame_id))
	return retval
