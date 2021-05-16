import os

import Constants
from Game import Game
from my_xml.F24XmlLoader import F24XmlLoader
from my_xml.MA3XmlLoader import MA3XmlLoader


def initiate(path, game_number, number_of_lines=500000):
	location_data = ""
	event_data = ""
	match_data = ""
	meta_data = ""
	loader = F24XmlLoader

	files = os.listdir(path)
	for file_name in files:
		if "{0}.dat".format(game_number) in file_name:
			location_data = "{0}/{1}".format(path, file_name)

		elif "{0}-eventdetails.xml".format(game_number) in file_name:
			event_data = "{0}/{1}".format(path, file_name)
			loader = F24XmlLoader()
			# event_data = "{0}/MA3_F24_API.xml".format(path, file_name)

		elif "{0}_f24.xml".format(game_number) in file_name:
			event_data = "{0}/{1}".format(path, file_name)
			loader = F24XmlLoader()

		elif "{0}-matchresults.xml".format(game_number) in file_name:
			match_data = "{0}/{1}".format(path, file_name)
			loader = F24XmlLoader()

		elif "{0}_f7.xml".format(game_number) in file_name:
			match_data = "{0}/{1}".format(path, file_name)
			loader = F24XmlLoader()

		elif "F24_API.xml" in file_name:
			event_data = "{0}/{1}".format(path, file_name)
			loader = MA3XmlLoader()

		elif "F7_API" in file_name:
			match_data = "{0}/{1}".format(path, file_name)
			loader = MA3XmlLoader()

		elif "{0}_metadata.xml".format(game_number) in file_name:
			meta_data = "{0}/{1}".format(path, file_name)

	summary_path = "{0}/{1}_{2}.txt".format(path, "alignment_summary", game_number)
	game = Game(location_data=location_data, event_data=event_data,
				match_data=match_data, meta_data=meta_data,
				summary_path=summary_path, lines=number_of_lines, loader=loader)
	return game


def extract_game_number_from_path(path):
	filename = path.split("/")[-1]
	game_id = 0
	try:
		game_id = int(filename.split(".")[0])
		game_id = game_id
	except ValueError:
		print("Wrong file")
	return game_id


def extract_directory_from_path(path):
	dir_list = path.split("/")
	del dir_list[-1]
	dir = os.sep.join(dir_list)
	return dir


