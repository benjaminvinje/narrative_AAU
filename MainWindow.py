from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMainWindow, QIcon, QItemSelectionModel, QMessageBox, QSlider, QLineEdit, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PyQt4.phonon import Phonon
import matplotlib.pyplot as plt
from PyQt4.uic import loadUiType

from GUI.GUI.MainWindow import Ui_MainWindow
from GameViewer import GameViewer
import numpy as np
import Hygge
from matplotsoccer import field
from TeamType import TeamType

from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay, ConvexHull


# Ui_MainWindow, QMainWindow = loadUiType('.\GUI\GUI\mainwindow.ui')

class MainWindow(QMainWindow):
    def __init__(self, dir_path, game_id, game):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game_id = game_id
        self.dir_path = dir_path
        self.game = game

        self.viewer = GameViewer(self.game)
        self.viewer.ui_window = self

        self.set_title()

        #self.ui.toolboxTab.setStyleSheet

        self.figure = self.viewer.fig
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setVisible(False)
        self.ui.canvasLayout.addWidget(self.canvas)

        # self.ui.mplvl_3.addWidget(self.ui.mplwindow)
        # self.ui.mplvl_4.addWidget(self.ui.mplwindow2)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.canvas2.setVisible(False)
        self.ax1 = self.figure2.add_subplot(111)

        field(ax=self.ax1, show=False)
        self.ax1.set_title("Ingen situation valgt")

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.canvas3.setVisible(False)
        self.ax2 = self.figure3.add_subplot(111)

        field(ax=self.ax2, show=False)
        self.ax2.set_title("Lignende situation #1: ")

        self.figure4 = Figure()
        self.canvas4 = FigureCanvas(self.figure4)
        self.canvas4.setVisible(False)
        self.ax3 = self.figure4.add_subplot(111)

        field(ax=self.ax3, show=False)
        self.ax3.set_title("Lignende situation #2: ")

        self.figure5 = Figure()
        self.canvas5 = FigureCanvas(self.figure5)
        self.canvas5.setVisible(False)
        self.ax4 = self.figure5.add_subplot(111)

        field(ax=self.ax4, show=False)
        self.ax4.set_title("Lignende situation #3: ")

        self.figure6 = Figure()
        self.canvas6 = FigureCanvas(self.figure6)
        self.canvas6.setVisible(False)
        self.ax5 = self.figure6.add_subplot(111)

        field(ax=self.ax5, show=False)
        self.ax5.set_title("Lignende situation #4: ")

        self.figure7 = Figure()
        self.canvas7 = FigureCanvas(self.figure7)
        self.canvas7.setVisible(False)
        self.ax6 = self.figure7.add_subplot(111)

        field(ax=self.ax6, show=False)
        self.ax6.set_title("Lignende situation #5: ")

        self.figure8 = Figure()
        self.canvas8 = FigureCanvas(self.figure8)
        self.canvas8.setVisible(False)
        self.ax7 = self.figure8.add_subplot(111)

        field(ax=self.ax7, show=False)
        self.ax7.set_title("Lignende situation #6: ")

        self.figure9 = Figure()
        self.canvas9 = FigureCanvas(self.figure9)
        self.canvas9.setVisible(False)
        self.ax8 = self.figure9.add_subplot(111)

        field(ax=self.ax8, show=False)
        self.ax8.set_title("Ingen situation valgt")

        self.figure10 = Figure()
        self.canvas10 = FigureCanvas(self.figure10)
        self.canvas10.setVisible(False)
        self.ax9 = self.figure10.add_subplot(111)

        field(ax=self.ax9, show=False)
        self.ax9.set_title("Lignende situation #1: ")

        self.figure11 = Figure()
        self.canvas11 = FigureCanvas(self.figure11)
        self.canvas11.setVisible(False)
        self.ax10 = self.figure11.add_subplot(111)

        field(ax=self.ax10, show=False)
        self.ax10.set_title("Lignende situation #2: ")

        self.figure12 = Figure()
        self.canvas12 = FigureCanvas(self.figure12)
        self.canvas12.setVisible(False)
        self.ax11 = self.figure12.add_subplot(111)

        field(ax=self.ax11, show=False)
        self.ax11.set_title("Lignende situation #3: ")

        self.figure13 = Figure()
        self.canvas13 = FigureCanvas(self.figure13)
        self.canvas13.setVisible(False)
        self.ax12 = self.figure13.add_subplot(111)

        field(ax=self.ax12, show=False)
        self.ax12.set_title("Lignende situation #4: ")

        self.figure14 = Figure()
        self.canvas14 = FigureCanvas(self.figure14)
        self.canvas14.setVisible(False)
        self.ax13 = self.figure14.add_subplot(111)

        field(ax=self.ax13, show=False)
        self.ax13.set_title("Lignende situation #5: ")

        self.figure15 = Figure()
        self.canvas15 = FigureCanvas(self.figure15)
        self.canvas15.setVisible(False)
        self.ax14 = self.figure15.add_subplot(111)

        field(ax=self.ax14, show=False)
        self.ax14.set_title("Lignende situation #6: ")

        plt.tight_layout()
        plt.axis("on")

        # self.ax1 = self.figure2.add_subplot(111)
        # self.ax1.plot(np.random.rand(5))
        # self.toolbar1 = NavigationToolbar(self.canvas2, self)
        self.ui.mplvl_3.addWidget(self.canvas2)
        self.ui.mplvl_4.addWidget(self.canvas3)
        self.ui.mplvl_5.addWidget(self.canvas4)
        self.ui.mplvl_6.addWidget(self.canvas5)
        self.ui.mplvl_7.addWidget(self.canvas6)
        self.ui.mplvl_8.addWidget(self.canvas7)
        self.ui.mplvl_9.addWidget(self.canvas8)
        self.ui.mplvl_10.addWidget(self.canvas9)
        self.ui.mplvl_11.addWidget(self.canvas10)
        self.ui.mplvl_12.addWidget(self.canvas11)
        self.ui.mplvl_13.addWidget(self.canvas12)
        self.ui.mplvl_14.addWidget(self.canvas13)
        self.ui.mplvl_15.addWidget(self.canvas14)
        self.ui.mplvl_16.addWidget(self.canvas15)

        self.slider = QSlider(Qt.Horizontal, self)
        self.ui.verticalLayout_4.addWidget(self.slider)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.lineEdit = QLineEdit(self)
        self.ui.verticalLayout_4.addWidget(self.lineEdit)

        self.slider.valueChanged.connect(self.changedValue)

        self.initialize_widgets()

        self.show_initial_frame()

        self.marker_size = 40
        self.event_id_column = 6

        b1 = self.ui.NNbutton
        b1.clicked.connect(self.clickedbutton)

        b2 = self.ui.NNbutton_2
        b2.clicked.connect(self.clickedbuttonAway)

        b3 = self.ui.voronoiButton
        b3.clicked.connect(self.voronoi)

        b4 = self.ui.triangledey
        b4.clicked.connect(self.delaney)

        b5 = self.ui.convex
        b5.clicked.connect(self.convexy)

    def set_title(self):
        self.game.load_game_summary()
        summary = self.game.game_summary
        self.setWindowTitle("ANOTHER TITLE")
        season = "{0} {1}".format(summary.competition_name, summary.season_name)
        matchday = "Matchday {0}".format(summary.matchday)
        result = "{0} {1} vs. {2} {3}".format(summary.home_team_name, summary.home_score, summary.away_score,
                                              summary.away_team_name)
        date = summary.game_date
        self.setWindowTitle("{0} {1} {2}, {3}".format(season, matchday, date, result))

    def initialize_widgets(self):
        self.ui.pauseButton_4.clicked.connect(self.pause_button_clicked)
        self.ui.pauseButton_9.clicked.connect(self.pause_button_clicked)

        self.ui.tenSecBack_4.clicked.connect(self.ten_sec_back_clicked)
        self.ui.tenSecBack_9.clicked.connect(self.ten_sec_back_clicked)
        self.ui.fiveSecBack_4.clicked.connect(self.five_sec_back_clicked)
        self.ui.fiveSecBack_9.clicked.connect(self.five_sec_back_clicked)
        self.ui.fiveSecForward_4.clicked.connect(self.five_sec_forward_clicked)
        self.ui.fiveSecForward_9.clicked.connect(self.five_sec_forward_clicked)
        self.ui.tenSecForward_4.clicked.connect(self.ten_sec_forward_clicked)
        self.ui.tenSecForward_9.clicked.connect(self.ten_sec_forward_clicked)
        self.slider.valueChanged.connect(self.changedValue)

        # self.slider.sliderMoved(self.tickMinute_clicked)

        # self.ui.videoPlayer = Phonon.VideoPlayer()
        # media = Phonon.MediaSource('../Rondo.mp4')
        # self.ui.videoPlayer.load(media)
        # self.ui.mplvl_2.addWidget(self.ui.mplwindow)

    def show_initial_frame(self):
        if self.viewer.ax is not None:
            self.viewer.ax.clear()
        # ax.clear()
        # self.ui.videoPlayer.play()
        # self.ui.videoPlayer.show()

        self.viewer.show()
        self.canvas.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        self.canvas4.draw()
        self.canvas5.draw()
        self.canvas6.draw()
        self.canvas7.draw()
        self.canvas8.draw()
        self.canvas9.draw()
        self.canvas10.draw()
        self.canvas11.draw()
        self.canvas12.draw()
        self.canvas13.draw()
        self.canvas14.draw()
        self.canvas15.draw()
        self.canvas.setVisible(True)
        self.canvas2.setVisible(True)
        self.canvas3.setVisible(True)
        self.canvas4.setVisible(True)
        self.canvas5.setVisible(True)
        self.canvas6.setVisible(True)
        self.canvas7.setVisible(True)
        self.canvas8.setVisible(True)
        self.canvas9.setVisible(True)
        self.canvas10.setVisible(True)
        self.canvas11.setVisible(True)
        self.canvas12.setVisible(True)
        self.canvas13.setVisible(True)
        self.canvas14.setVisible(True)
        self.canvas15.setVisible(True)

    def pause_button_clicked(self):
        # self.viewer.forward = not self.viewer.forward
        self.viewer.start_or_pause_animation()
        if self.viewer.running:
            self.ui.pauseButton_4.setText("||")
            self.ui.pauseButton_9.setText("||")
            self.viewer.reset_pitch()  # reset pitch to get rid of the static events drawn on the pitch before animation start
        else:
            self.ui.pauseButton_4.setText("▶")
            self.ui.pauseButton_9.setText("▶")

    def forward_seconds(self, seconds):
        self.viewer.i += self.viewer.game.position_frequency * seconds

    def backward_seconds(self, seconds):
        self.viewer.i -= self.viewer.game.position_frequency * seconds

    def changedValue(self):
        sizee = self.slider.value()
        self.lineEdit.setText(str(sizee))
        self.viewer.reset_pitch()
        self.viewer.i = 0
        self.viewer.i += self.viewer.game.position_frequency * (sizee * 60)

    def ten_sec_back_clicked(self):
        self.backward_seconds(10)

    def ten_sec_forward_clicked(self):
        self.forward_seconds(10)

    def five_sec_back_clicked(self):
        self.backward_seconds(5)

    def five_sec_forward_clicked(self):
        self.forward_seconds(5)

    def show_modal(self, icon, window_title, text, informative_text):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setWindowTitle(window_title)
        retval = msg.exec_()

    def clickedbuttonAway(self):
        self.ax8.clear()
        self.ax9.clear()
        self.ax10.clear()
        self.ax11.clear()
        self.ax12.clear()
        self.ax13.clear()
        self.ax14.clear()


        framepick_away = Hygge.new_locs_away[:, self.viewer.i]
        fulldatalist_away = Hygge.full_data_away2
        megafulldatalist_away = Hygge.full_data_away
        neighbors_count = 7

        tree_away = Hygge.KDTree(fulldatalist_away)
        dist_away, ind_away = tree_away.query(framepick_away, k=neighbors_count)
        closest_neighbors_away = fulldatalist_away[ind_away.tolist()[0]]
        closest_neighbors_away_first = closest_neighbors_away[1]
        closest_neighbors_away_second = closest_neighbors_away[2]
        closest_neighbors_away_third = closest_neighbors_away[3]
        closest_neighbors_away_fourth = closest_neighbors_away[4]
        closest_neighbors_away_fifth = closest_neighbors_away[5]
        closest_neighbors_away_sixth = closest_neighbors_away[6]

        closest_neighbors_away_first = closest_neighbors_away_first.tolist()
        closest_neighbors_away_second = closest_neighbors_away_second.tolist()
        closest_neighbors_away_third = closest_neighbors_away_third.tolist()
        closest_neighbors_away_fourth = closest_neighbors_away_fourth.tolist()
        closest_neighbors_away_fifth = closest_neighbors_away_fifth.tolist()
        closest_neighbors_away_sixth = closest_neighbors_away_sixth.tolist()

        firstneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_first)
        secondneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_second)
        thirdneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_third)
        fourthneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_fourth)
        fifthneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_fifth)
        sixthneighbor_away_frame = megafulldatalist_away.tolist().index(closest_neighbors_away_sixth)



        currentframe_away = self.viewer.i / self.viewer.game.position_frequency
        currentframe_min_away = int(currentframe_away / 60)
        currentframe_sec_away = int(currentframe_away - currentframe_min_away * 60)

        framespeed_away = int(firstneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_away = int(framespeed_away / 60)
        plotseconds_away = int(framespeed_away - plotminutes_away * 60)

        framespeed_2_away = int(secondneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_2_away = int(framespeed_2_away / 60)
        plotseconds_2_away = int(framespeed_2_away - plotminutes_2_away * 60)

        framespeed_3_away = int(thirdneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_3_away = int(framespeed_3_away / 60)
        plotseconds_3_away = int(framespeed_3_away - plotminutes_3_away * 60)

        framespeed_4_away = int(fourthneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_4_away = int(framespeed_4_away / 60)
        plotseconds_4_away = int(framespeed_4_away - plotminutes_4_away * 60)

        framespeed_5_away = int(fifthneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_5_away = int(framespeed_5_away / 60)
        plotseconds_5_away = int(framespeed_5_away - plotminutes_5_away * 60)

        framespeed_6_away = int(sixthneighbor_away_frame / self.viewer.game.position_frequency)
        plotminutes_6_away = int(framespeed_6_away / 60)
        plotseconds_6_away = int(framespeed_6_away - plotminutes_6_away * 60)

        # Make framepick ready for plotting
        framepick_away = framepick_away.reshape(1, 12, 2)
        calcAdd = np.array([5250, 3400])
        calcMeters = np.array([100, 100])
        framepick_away += calcAdd
        framepick_away = framepick_away / calcMeters

        closest_neighbors_reshape_away = closest_neighbors_away.reshape(neighbors_count, 12, 2)
        closest_neighbors_reshape_away += calcAdd
        closest_neighbors_reshape_away = closest_neighbors_reshape_away / calcMeters


        # Plot
        field(ax=self.ax8, show=False)
        self.ax8.scatter(framepick_away[:, 0:1, 0], framepick_away[:, 0:1, 1], color='black', zorder=10)
        self.ax8.scatter(framepick_away[:, 1:, 0], framepick_away[:, 1:, 1], color='red', zorder=10)
        self.ax8.set_title("Valgt situation - {0}:{1:02d}".format(currentframe_min_away,
                                                                  currentframe_sec_away))
        self.canvas9.draw()

        # Plot nearest situations
        field(ax=self.ax9, show=False)
        self.ax9.scatter(closest_neighbors_reshape_away[1, 0:1, 0], closest_neighbors_reshape_away[1, 0:1, 1],
                         color='black', zorder=10)
        self.ax9.scatter(closest_neighbors_reshape_away[1, 1:, 0], closest_neighbors_reshape_away[1, 1:, 1],
                         color='red', zorder=10)
        self.ax9.set_title("Lignende situation #1 {0}:{1:02d}".format(plotminutes_away, plotseconds_away))
        self.canvas10.draw()

        field(ax=self.ax10, show=False)
        self.ax10.scatter(closest_neighbors_reshape_away[2, 0:1, 0], closest_neighbors_reshape_away[2, 0:1, 1],
                         color='black', zorder=10)
        self.ax10.scatter(closest_neighbors_reshape_away[2, 1:, 0], closest_neighbors_reshape_away[2, 1:, 1],
                         color='red', zorder=10)
        self.ax10.set_title("Lignende situation #2 {0}:{1:02d}".format(plotminutes_2_away, plotseconds_2_away))
        self.canvas11.draw()

        field(ax=self.ax11, show=False)
        self.ax11.scatter(closest_neighbors_reshape_away[3, 0:1, 0], closest_neighbors_reshape_away[3, 0:1, 1],
                         color='black', zorder=10)
        self.ax11.scatter(closest_neighbors_reshape_away[3, 1:, 0], closest_neighbors_reshape_away[3, 1:, 1],
                         color='red', zorder=10)
        self.ax11.set_title("Lignende situation #3 {0}:{1:02d}".format(plotminutes_3_away, plotseconds_3_away))
        self.canvas12.draw()

        field(ax=self.ax12, show=False)
        self.ax12.scatter(closest_neighbors_reshape_away[4, 0:1, 0], closest_neighbors_reshape_away[4, 0:1, 1],
                         color='black', zorder=10)
        self.ax12.scatter(closest_neighbors_reshape_away[4, 1:, 0], closest_neighbors_reshape_away[4, 1:, 1],
                         color='red', zorder=10)
        self.ax12.set_title("Lignende situation #4 {0}:{1:02d}".format(plotminutes_4_away, plotseconds_4_away))
        self.canvas13.draw()

        field(ax=self.ax13, show=False)
        self.ax13.scatter(closest_neighbors_reshape_away[5, 0:1, 0], closest_neighbors_reshape_away[5, 0:1, 1],
                         color='black', zorder=10)
        self.ax13.scatter(closest_neighbors_reshape_away[5, 1:, 0], closest_neighbors_reshape_away[5, 1:, 1],
                         color='red', zorder=10)
        self.ax13.set_title("Lignende situation #5 {0}:{1:02d}".format(plotminutes_5_away, plotseconds_5_away))
        self.canvas14.draw()

        field(ax=self.ax14, show=False)
        self.ax14.scatter(closest_neighbors_reshape_away[6, 0:1, 0], closest_neighbors_reshape_away[6, 0:1, 1],
                         color='black', zorder=10)
        self.ax14.scatter(closest_neighbors_reshape_away[6, 1:, 0], closest_neighbors_reshape_away[6, 1:, 1],
                         color='red', zorder=10)
        self.ax14.set_title("Lignende situation #6 {0}:{1:02d}".format(plotminutes_6_away, plotseconds_6_away))
        self.canvas15.draw()

    def voronoi(self):
        hej = self.viewer.game.frames[self.viewer.i]
        home_players_positions = self.viewer.prepare_players(frame=hej, teamtype=TeamType.HOME)
        vor = Voronoi(home_players_positions)
        voronoi_plot_2d(vor, ax=self.viewer.ax)
        self.viewer.ax.set_xlim([self.viewer.x_min, self.viewer.x_max])
        self.viewer.ax.set_ylim([self.viewer.y_min, self.viewer.y_max])
        self.canvas.draw()
        x = self.viewer.update_plot(self.viewer.i)
        for z in x:
            self.viewer.fig.draw_artist(z)

    def delaney(self):
        hygge = self.viewer.game.frames[self.viewer.i]
        home_players_dey = self.viewer.prepare_players(frame=hygge, teamtype=TeamType.HOME)
        deluaney = Delaunay(home_players_dey)
        plt.triplot(home_players_dey[:, 0], home_players_dey[:, 1], deluaney.simplices)
        self.viewer.ax.set_xlim([self.viewer.x_min, self.viewer.x_max])
        self.viewer.ax.set_ylim([self.viewer.y_min, self.viewer.y_max])
        self.canvas.draw()
        x = self.viewer.update_plot(self.viewer.i)
        for z in x:
            self.viewer.fig.draw_artist(z)

    def convexy(self):
        tiden = self.viewer.game.frames[self.viewer.i]
        home_players_con = self.viewer.prepare_players(frame=tiden, teamtype=TeamType.HOME)
        convexhull = ConvexHull(home_players_con)
        for simplex in convexhull.simplices:
            plt.plot(home_players_con[simplex, 0], home_players_con[simplex, 1], 'k-')
        self.viewer.ax.set_xlim([self.viewer.x_min, self.viewer.x_max])
        self.viewer.ax.set_ylim([self.viewer.y_min, self.viewer.y_max])
        self.canvas.draw()
        x = self.viewer.update_plot(self.viewer.i)
        for z in x:
            self.viewer.fig.draw_artist(z)


    '''
        #self.ax1.cla()
        #self.viewer.ax.clear()

        #self.ax1.clf()
        print('Current frame is ', self.viewer.i)
        print('Current frame ID: ', self.viewer.game.frames[self.viewer.i].id)
        #self.viewer.reset_pitch()

        #lullul = self.viewer.game.frames[self.viewer.game.get_index_by_id(self.viewer.game.first_period_frame_id)]
        #print(lullul)
        initial_frame = self.viewer.game.frames[self.viewer.i]
        #print(initial_frame)
        hej = self.viewer.i
        #print(hej)
        home_players_positions = self.viewer.prepare_players(frame=initial_frame, teamtype=TeamType.HOME)
        #self.viewer.ax.scatter(home_players_positions[:, 0], home_players_positions[:, 1])
        self.viewer.ax.scatter(home_playerssitions[:, 0], home_players_positions[:, 1],
                        c=self.viewer.home_color, edgecolors=self.viewer.home_edge_color, s=self.viewer.dot_size)


        print(home_players_positions)

        home_player_arrows_plots = []_po
        away_player_arrows_plots = []
        home_shirt_numbers_plots = []
        away_shirt_numbers_plots = []

        home_players = self.viewer.game.get_players_by_team_type_from_frame(TeamType.HOME, initial_frame)
        away_players = self.viewer.game.get_players_by_team_type_from_frame(TeamType.AWAY, initial_frame)
        for player in home_players:
            home_shirt_numbers_plots.append(
                self.viewer.ax.text(player.coord.x, player.coord.y, "", fontsize=9, ha="center", fontname=self.font))

            home_player_arrows_plots.append(self.viewer.ax.plot([], [], color=self.viewer.home_edge_color, zorder=-1)[0])

        for player in away_players:
            away_shirt_numbers_plots.append(
                self.viewer.ax.text(player.coord.x, player.coord.y, "", fontsize=9, ha="center", fontname=self.font))

            away_player_arrows_plots.append(self.viewer.ax.plot([], [], color=self.viewer.away_edge_color, zorder=-1)[0])

        #self.viewer.home_players_plot()
        #self.viewer.ax.scatter(home_players_positions[:, 0], home_players_positions[:, 1],
                                                #c="#ffffff", edgecolors=self.viewer.home_edge_color, s=self.viewer.dot_size)
        #voro = np.array(home_players_positions)
        vor = Voronoi(home_players_positions)
        voronoi_plot_2d(vor, ax=self.viewer.ax)
        self.viewer.ax.set_xlim([self.viewer.x_min, self.viewer.x_max])
        self.viewer.ax.set_ylim([self.viewer.y_min, self.viewer.y_max])
        #self.figure2.tight_layout()


        print('lol')

        self.viewer.update_score_board(initial_frame)
        self.viewer.prepare_shirt_number_plots(initial_frame)

        self.canvas.draw()
        print('lol')
    '''

    def clickedbutton(self):
        # print('Clicked location on the pitch: x: {0}, y: {1}'.format(evt.xdata, evt.ydata))
        print('Current frame is ', self.viewer.i)
        print('Current frame ID: ', self.viewer.game.frames[self.viewer.i].id)

        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.ax5.clear()
        self.ax6.clear()
        self.ax7.clear()

        framepick = Hygge.new_locs_home[:, self.viewer.i]
        fulldatalist = Hygge.full_data2
        megafulldatalist = Hygge.full_data
        neighbors_count = 7

        tree = Hygge.KDTree(fulldatalist)
        dist, ind = tree.query(framepick, k=neighbors_count)
        closest_neighbors = fulldatalist[ind.tolist()[0]]
        closest_neighbors_first = closest_neighbors[1]
        closest_neighbors_second = closest_neighbors[2]
        closest_neighbors_third = closest_neighbors[3]
        closest_neighbors_fourth = closest_neighbors[4]
        closest_neighbors_fifth = closest_neighbors[5]
        closest_neighbors_sixth = closest_neighbors[6]
        closest_neighbors_first = closest_neighbors_first.tolist()
        closest_neighbors_second = closest_neighbors_second.tolist()
        closest_neighbors_third = closest_neighbors_third.tolist()
        closest_neighbors_fourth = closest_neighbors_fourth.tolist()
        closest_neighbors_fifth = closest_neighbors_fifth.tolist()
        closest_neighbors_sixth = closest_neighbors_sixth.tolist()
        firstneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_first)
        secondneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_second)
        thirdneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_third)
        fourthneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_fourth)
        fifthneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_fifth)
        sixthneighbor_frame = megafulldatalist.tolist().index(closest_neighbors_sixth)
        print("kig her", firstneighbor_frame)

        currentframe = self.viewer.i / self.viewer.game.position_frequency
        currentframe_min = int(currentframe / 60)
        currentframe_sec = int(currentframe - currentframe_min * 60)
        currentframe_milisec = int(currentframe - currentframe_sec * 60)
        print(currentframe)
        print(currentframe_min)
        print(currentframe_sec)
        print(currentframe_milisec)

        framespeed = int(firstneighbor_frame / self.viewer.game.position_frequency)
        plotminutes = int(framespeed / 60)
        plotseconds = int(framespeed - plotminutes * 60)

        framespeed_2 = int(secondneighbor_frame / self.viewer.game.position_frequency)
        plotminutes_2 = int(framespeed_2 / 60)
        plotseconds_2 = int(framespeed_2 - plotminutes_2 * 60)

        framespeed_3 = int(thirdneighbor_frame / self.viewer.game.position_frequency)
        plotminutes_3 = int(framespeed_3 / 60)
        plotseconds_3 = int(framespeed_3 - plotminutes_3 * 60)

        framespeed_4 = int(fourthneighbor_frame / self.viewer.game.position_frequency)
        plotminutes_4 = int(framespeed_4 / 60)
        plotseconds_4 = int(framespeed_4 - plotminutes_4 * 60)

        framespeed_5 = int(fifthneighbor_frame / self.viewer.game.position_frequency)
        plotminutes_5 = int(framespeed_5 / 60)
        plotseconds_5 = int(framespeed_5 - plotminutes_5 * 60)

        framespeed_6 = int(sixthneighbor_frame / self.viewer.game.position_frequency)
        plotminutes_6 = int(framespeed_6 / 60)
        plotseconds_6 = int(framespeed_6 - plotminutes_6 * 60)

        # Make framepick ready for plotting
        framepick = framepick.reshape(1, 12, 2)
        calcAdd = np.array([5250, 3400])
        calcMeters = np.array([100, 100])
        framepick += calcAdd
        framepick = framepick / calcMeters

        closest_neighbors_reshape = closest_neighbors.reshape(neighbors_count, 12, 2)
        closest_neighbors_reshape += calcAdd
        closest_neighbors_reshape = closest_neighbors_reshape / calcMeters

        # Plot
        field(ax=self.ax1, show=False)
        self.ax1.scatter(framepick[:, 0:1, 0], framepick[:, 0:1, 1], color='black', zorder=10)
        self.ax1.scatter(framepick[:, 1:, 0], framepick[:, 1:, 1], color='blue', zorder=10)
        self.ax1.set_title("Valgt situation - {0}:{1:02d}".format(currentframe_min,
                           currentframe_sec))
        self.canvas2.draw()

        # Plot nearest situations
        field(ax=self.ax2, show=False)
        self.ax2.scatter(closest_neighbors_reshape[1, 0:1, 0], closest_neighbors_reshape[1, 0:1, 1],
                         color='black', zorder=10)
        self.ax2.scatter(closest_neighbors_reshape[1, 1:, 0], closest_neighbors_reshape[1, 1:, 1],
                         color='blue', zorder=10)
        self.ax2.set_title("Lignende situation #1 {0}:{1:02d}".format(plotminutes, plotseconds))
        self.canvas3.draw()

        field(ax=self.ax3, show=False)
        self.ax3.scatter(closest_neighbors_reshape[2, 0:1, 0], closest_neighbors_reshape[2, 0:1, 1],
                         color='black', zorder=10)
        self.ax3.scatter(closest_neighbors_reshape[2, 1:, 0], closest_neighbors_reshape[2, 1:, 1],
                         color='blue', zorder=10)
        self.ax3.set_title("Lignende situation #2 {0}:{1:02d}".format(plotminutes_2, plotseconds_2))
        self.canvas4.draw()

        field(ax=self.ax4, show=False)
        self.ax4.scatter(closest_neighbors_reshape[3, 0:1, 0], closest_neighbors_reshape[3, 0:1, 1],
                         color='black', zorder=10)
        self.ax4.scatter(closest_neighbors_reshape[3, 1:, 0], closest_neighbors_reshape[3, 1:, 1],
                         color='blue', zorder=10)
        self.ax4.set_title("Lignende situation #3 {0}:{1:02d}".format(plotminutes_3, plotseconds_3))
        self.canvas5.draw()

        field(ax=self.ax5, show=False)
        self.ax5.scatter(closest_neighbors_reshape[4, 0:1, 0], closest_neighbors_reshape[4, 0:1, 1],
                         color='black', zorder=10)
        self.ax5.scatter(closest_neighbors_reshape[4, 1:, 0], closest_neighbors_reshape[4, 1:, 1],
                         color='blue', zorder=10)
        self.ax5.set_title("Lignende situation #4 {0}:{1:02d}".format(plotminutes_4, plotseconds_4))
        self.canvas6.draw()

        field(ax=self.ax6, show=False)
        self.ax6.scatter(closest_neighbors_reshape[5, 0:1, 0], closest_neighbors_reshape[5, 0:1, 1],
                         color='black', zorder=10)
        self.ax6.scatter(closest_neighbors_reshape[5, 1:, 0], closest_neighbors_reshape[5, 1:, 1],
                         color='blue', zorder=10)
        self.ax6.set_title("Lignende situation #5 {0}:{1:02d}".format(plotminutes_5, plotseconds_5))
        self.canvas7.draw()

        field(ax=self.ax7, show=False)
        self.ax7.scatter(closest_neighbors_reshape[6, 0:1, 0], closest_neighbors_reshape[6, 0:1, 1],
                         color='black', zorder=10)
        self.ax7.scatter(closest_neighbors_reshape[6, 1:, 0], closest_neighbors_reshape[6, 1:, 1],
                         color='blue', zorder=10)
        self.ax7.set_title("Lignende situation #6 {0}:{1:02d}".format(plotminutes_6, plotseconds_6))
        self.canvas8.draw()



'''
        #framepick = treeee.new_locs_home[:, self.viewer.i]
        framepick = treeee.new_locs_home[:, self.viewer.i]
        fulldatalist = treeee.fulldata
        tree = vptreealgorithm.VPTree(fulldatalist, treeee.euclidean)

        rangesearch = tree.get_all_in_range(framepick, 2000, 2050)
        print("Range search: ", rangesearch)

        neighbors = np.array(rangesearch)
        neighbors = neighbors[1:]
        print("Neighbors: ", neighbors)

        firstneighbor = neighbors[0]
        firstneighbor = firstneighbor[1]
        firstneighbor_flatten = firstneighbor.flatten()
        firstneighbor_flatten = firstneighbor.tolist()
        firstneighbor_frame = fulldatalist.tolist().index(firstneighbor_flatten)
        firstneighbor_reshape = firstneighbor.reshape(1, 11, 2)

        secondneighbor = neighbors[1]
        secondneighbor = secondneighbor[1]
        secondneighbor_reshape = secondneighbor.reshape(1, 11, 2)
        secondneighbor_flatten = secondneighbor.flatten()
        secondneighbor_flatten = secondneighbor.tolist()
        secondneighbor_frame = fulldatalist.tolist().index(secondneighbor_flatten)

        thirdneighbor = neighbors[2]
        thirdneighbor = thirdneighbor[1]
        thirdneighbor_reshape = thirdneighbor.reshape(1, 11, 2)
        thirdneighbor_flatten = thirdneighbor.flatten()
        thirdneighbor_flatten = thirdneighbor.tolist()
        thirdneighbor_frame = fulldatalist.tolist().index(thirdneighbor_flatten)

        # Make framepick ready for plotting
        framepick = framepick.reshape(1, 11, 2)
        calcAdd = np.array([5250, 3400])
        calcMeters = np.array([100, 100])
        framepick += calcAdd
        framepick = framepick / calcMeters

        firstneighbor_reshape += calcAdd
        secondneighbor_reshape += calcAdd
        thirdneighbor_reshape += calcAdd
        firstneighbor_reshape = firstneighbor_reshape / calcMeters
        secondneighbor_reshape = secondneighbor_reshape / calcMeters
        thirdneighbor_reshape = thirdneighbor_reshape / calcMeters

        # Plot
        field(ax=self.ax1, show=False)
        self.ax1.scatter(framepick[:, :, 0], framepick[:, :, 1], color='blue', zorder=10)
        self.ax1.set_title("Current frame: %i" % self.viewer.i)
        self.canvas2.draw()


        # Plot nearest situations
        field(ax=self.ax2, show=False)
        self.ax2.scatter(firstneighbor_reshape[:, :, 0], firstneighbor_reshape[:, :, 1],
                         color='blue', zorder=10)
        self.ax2.set_title("Nearest situation #1: %i" % firstneighbor_frame)
        self.canvas3.draw()

        print("NN search done in")
        print("--- %s seconds ---" % (time.time() - start_time))
'''


class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self, viewer, game, dir_path, game_id, figure2):
        super().__init__()
        self.viewer = viewer
        self.game = game
        self.dir_path = dir_path
        self.game_id = game_id
