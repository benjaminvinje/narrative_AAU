from collections import Counter

import sys

import matplotlib
from PyQt4.QtGui import QApplication, QMainWindow

from MainWindow import MainWindow
from WelcomeDialog import WelcomeDialog


def calculate_event_stats(events):
	ret_dict = []
	for event in events:
		ret_dict.append(event.type.name)
	counts = Counter(ret_dict)
	number_of_events = len(events)
	for k in counts:
		counts[k] = counts[k] / number_of_events * 100
	return counts


def main():
	app = QApplication(sys.argv)

	welcome_dialog = WelcomeDialog()
	if not welcome_dialog.exec_():
		sys.exit(0)

	window = MainWindow(welcome_dialog.dir_path, welcome_dialog.game_id, welcome_dialog.game)
	window.show()
	sys.exit(app.exec_())

	#
	# game_numbers = [1059348, 1059341,1059342,1059343,1059344,1059345,1059346]
	# # game_numbers = [1059348]
	#
	# games = []
	# events_improved = []
	# events = []
	# mismatched_events= 0
	# synchronized_events= 0
	# corrected_performers= 0
	# for i in game_numbers:
	# 	print("Game {0} started...".format(i))
	# 	game = Launcher.initiate("D:\master_data\data\many_games", i)
	# 	game.load()
	# 	events.extend(game.events)
	#
	# 	stats = adjust_events(game)
	# 	events_improved.extend(game.events)
	#
	# 	games.append(game)
	# 	mismatched_events += stats.mismatched_events
	# 	corrected_performers += stats.corrected_performers
	#
	# 	orig_events = [event for event in game.events if event.type != EventType.CARRY and event.type != EventType.RECEPTION]
	# 	for event in orig_events:
	# 		if event.is_aligned():
	# 			synchronized_events += 1
	#
	#
	# 	print("Game {0} ended...".format(i))
	#
	# print("total events: {0}".format(len(events)))
	# print("synchronized events: {0}".format(synchronized_events))
	# print("added events: {0}".format(len(events_improved) - len(events)))
	# print("mismatched events: {0}".format(mismatched_events))
	# print("corrected performers events: {0}".format(corrected_performers))



def adjust_events(game):
	generator = Aligner(game)

	generator.adjust_events()
	# game.load()
	print_stats(generator.stats)
	return generator.stats


def print_stats(stats):
	print("Pass variance: {0:.2f}".format(stats.pass_variance()))
	print("Pass std dev: {0:.2f} frames".format(stats.pass_std_dev()))
	print("Pass avg: {0:.2f} frames".format(stats.pass_avg()))
	print("State variance: {0:.2f}".format(stats.state_variance()))
	print("State std dev: {0:.2f} frames".format(stats.state_std_dev()))
	print("State avg: {0:.2f} frames".format(stats.state_avg()))
	print("Mismatched events: {0}".format(stats.mismatched_events))


if __name__ == '__main__':
	main()
