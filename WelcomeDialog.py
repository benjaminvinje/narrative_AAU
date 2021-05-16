import re
from os import path

from PyQt4 import QtCore
from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox, QPixmap, QDialogButtonBox

import Launcher
from GUI.GUI.WelcomeDialog import Ui_Dialog
from my_xml.F24XmlLoader import F24XmlLoader
from my_xml.MA3XmlLoader import MA3XmlLoader


class WelcomeDialog(QDialog):
	def __init__(self):
		super(WelcomeDialog, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.selectButton.clicked.connect(self.select_clicked)
		self.game_id = 0
		self.dir_path = ""
		self.setFixedSize(self.size())
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)
		self.ui.loadButton.clicked.connect(self.load_clicked)
		self.ui.progressBar.setVisible(False)
		self.ui.wait_label.setVisible(False)
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setToolTip("First load a game      ")
		self.game = None
		self.load_task = TaskThread(self.dir_path, self.game_id, self.game)
		self.load_task.taskFinished.connect(self.finish_loading)

	def select_clicked(self):
		path = str(QFileDialog.getOpenFileName(self,
											   "Select a tracking data file. The event files need to be in the same location.."))
		if not path:
			return

		potential_game_ids = re.findall("\d{6,7}", path)
		if not potential_game_ids:
			self.show_modal(QMessageBox.Critical, "Wrong file selected.", "Wrong file selected.               ",
							"Please select the file containing tracking data (ex. 1234567.dat)")
			return
		self.game_id = potential_game_ids[-1]

		self.dir_path = Launcher.extract_directory_from_path(path)
		preview_game = Launcher.initiate(self.dir_path, self.game_id)
		if not self.validate_required_files(preview_game):
			return

		self.set_preview_text(preview_game)

		self.ui.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)
		if self.game_id == 0 or self.dir_path == "":
			self.ui.loadButton.setEnabled(False)
		else:
			self.ui.loadButton.setEnabled(True)

	def set_preview_text(self, preview_game):
		if "MA3" in preview_game.event_data_path:
			preview_game.loader = MA3XmlLoader()
		else:
			preview_game.loader = F24XmlLoader()
		preview_game.load_game_summary()
		summary = preview_game.game_summary
		selected = "Selected Game:"
		line1 = "{0}\n{1}".format(summary.competition_name, summary.season_name)
		line2 = "Matchday {0}".format(summary.matchday)
		line3 = "{0} {1} vs. {2} {3}".format(summary.home_team_name, summary.home_score, summary.away_score,
											 summary.away_team_name)
		line4 = summary.game_date

		#self.show_hide_synced_icon()

		self.ui.gameLabel.setText("{0}\n{1}\n{2}\n{3}\n{4}".format(selected, line1, line2, line3, line4))

	def validate_required_files(self, game):
		missing_files = []
		if not path.exists(game.match_data_path):
			missing_files.append("match results")
		if not path.exists(game.event_data_path):
			missing_files.append("event details")
		if not path.exists(game.meta_data_path):
			missing_files.append("metadata")
		if not path.exists(game.location_data_path):
			missing_files.append("tracking data")

		if missing_files:
			window_title = "Missing Files"
			text = window_title
			separator = ", "
			informative_text = "Missing files in the directory containing information about {0}".format(
				separator.join(missing_files))

			self.show_modal(QMessageBox.Critical, window_title, text, informative_text)
			return False
		return True

	def show_modal(self, icon, window_title, text, informative_text):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(text)
		msg.setInformativeText(informative_text)
		msg.setWindowTitle(window_title)
		retval = msg.exec_()


	def load_clicked(self):
		self.ui.progressBar.setVisible(True)
		self.ui.wait_label.setVisible(True)
		self.load_task.game_id = self.game_id
		self.load_task.dir_path = self.dir_path
		self.load_task.game = self.game

		self.load_task.start()

	def finish_loading(self):
		self.ui.progressBar.setVisible(False)
		self.ui.wait_label.setVisible(False)
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setFocus()
		self.game = self.load_task.game


class TaskThread(QtCore.QThread):
	taskFinished = QtCore.pyqtSignal()

	def __init__(self, dir_path, game_id, game):
		super().__init__()
		self.dir_path = dir_path
		self.game_id = game_id
		self.game = game

	def run(self):
		self.game = Launcher.initiate(self.dir_path, self.game_id)
		# self.game = Launcher.initiate(self.dir_path, self.game_id, 10000)
		# self.game = Launcher.initiate(self.dir_path, self.game_id, 80000)
		self.game.load()

		self.taskFinished.emit()
