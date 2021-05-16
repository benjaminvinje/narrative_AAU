import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import pandas as pd
import numpy as np
from kloppy import TRACABSerializer, to_pandas
import time

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('qt5agg')



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        serializer = TRACABSerializer()

        with open("sorteddata/2081780.dat", "rb") as raw, \
                open("sorteddata/2081780_metadata.xml", "rb") as meta:
            data_set = to_pandas(serializer.deserialize(
                inputs={
                    'raw_data': raw,
                    'metadata': meta
                },
                options={
                    'only_alive': False
                }
            )
            )
        print("Finished reading", len(data_set))

        data_set.loc[(data_set['period_id'] == 2, data_set.columns.str.contains("away|home"))] = data_set.loc[
            (data_set['period_id'] == 2, data_set.columns.str.contains("away|home"))].mul(-1, axis=0)
        print(data_set)

        print(data_set.shape)

        data_set.dropna(how='all')
        data_set_arr = np.asarray(data_set.iloc[:, 4:])
        nan_array = np.isnan(data_set_arr)
        not_nan_array = ~ nan_array
        data_set_arr = data_set_arr[not_nan_array]
        print(data_set_arr)
        # nan_array = pd.isnull(data_set.array([np.nan, 0], dtype=float))
        # print(nan_array)

        rows_count = data_set.shape[0]
        column_count = data_set.shape[1] - 20
        print(rows_count)
        print(column_count)

        data_set_arr = data_set_arr.reshape(rows_count, column_count)
        # print(data_set_arr)

        split = np.array_split(data_set_arr, 500)
        split = np.asarray(split)
        print(split)

        # ball_movement = data_set.iloc[:, 4:6]
        ball_movement = split[0][:, 0:2]
        print(ball_movement)

        from random import randint
        randomno = []
        for i in range(0, 10):
            randomno.append(randint(0, 500))
        print(randomno)

        # ball_movement_fltx = ball_movement[0:250, 0]
        # ball_movement_flty = ball_movement[0:250, 1]
        # print(ball_movement_fltx)

        # ball_movement_x = ball_int[0:250, 0]
        # ball_movement_y = ball_int[0:250, 1]
        # print(ball_movement_x)
        # print(ball_movement_y)

        #self.figure = Figure()
        #self.canvas = FigureCanvas(self.figure)
        #self.canvas.setVisible(False)
        #self.ax1 = self.figure2.add_subplot(111)

        '''
        plt.plot(split[randno][:, 0], split[randno][:, 1])

        from mplsoccer.pitch import Pitch
        pitch = Pitch(pitch_type='tracab', pitch_width=68, pitch_length=105)
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.scatter(split[randno][:, 0], split[randno][:, 1],
                   color='black', zorder=10)
        pitch.draw(ax=ax)
        '''

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        from mplsoccer.pitch import Pitch
        self.pitch = Pitch(pitch_type='tracab', pitch_width=68, pitch_length=105)
        self.fig, self.ax = self.pitch.draw()

        #self.ax = plt.gca()
        for i in range(10):
            self.ax.scatter(split[i][:, 0], split[i][:, 1],
                   zorder=10)
        print(self.ax is plt.gca())

        self.xy = plt.ginput(6)
        self.x = [p[0] for p in self.xy]
        self.y = [p[1] for p in self.xy]
        self.ax.plot(self.x, self.y)
        print(self.xy)

        plt.tight_layout()
        plt.axis("on")
        self.ax.figure.canvas.draw()


        '''
        sc = Figure(self, width=5, height=4, dpi=100)
        sc.ax = plt.gca()
        sc.xy = plt.ginput(6)
        sc.x = [p[0] for p in sc.xy]
        sc.y = [p[1] for p in sc.xy]
        sc.line = plt.plot(sc.x, sc.y)
        sc.ax.figure.canvas.draw()

        self.setCentralWidget(sc)
        print(sc.xy)

        self.show()
        '''

    # def draw_line(self):
    #     ax = plt.gca()
    #     xy = plt.ginput(6)
    #
    #     x = [p[0] for p in xy]
    #     y = [p[1] for p in xy]
    #     line = plt.plot(x, y)
    #     ax.figure.canvas.draw()
    #
    #     self.lines.append(line)

        #print(self.lines[0])

    from scipy.cluster.hierarchy import dendrogram, linkage
    from matplotlib import pyplot as plt

    linked = linkage(split, 'single')

    labelList = range(1, 11)

    plt.figure(figsize=(10, 7))
    dendrogram(linked,
               orientation='top',
               labels=labelList,
               distance_sort='descending',
               show_leaf_counts=True)
    plt.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()

'''    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
   # window.draw_line()
    sys.exit(app.exec())

'''

