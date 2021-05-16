import os

import Launcher
from Aligner import Aligner


def stats():
	data_location = "./data/"

	pass_events = 0
	aerials_events = 0
	state_events = 0
	total_events = 0

	for folder in os.listdir(data_location):
		game_number = int(folder)
		game = Launcher.initiate(game_number)
		game.load_xml_data()
		generator = Aligner(game)

		for event in game.events:
			if event.type in generator.pass_events:
				pass_events += 1
			elif event.type in generator.state_changing_events:
				state_events += 1
			elif event.type in generator.duel_events:
				aerials_events += 1

		total_events += len(game.events)

	print("Total number of events: {0}".format(total_events))
	adj = aerials_events + state_events + pass_events
	print("Number of adjusted events: {0}".format(adj))
	print("Percentage of adjusted events {0:.2f}%".format(adj/total_events*100))






if __name__ == '__main__':
	stats()