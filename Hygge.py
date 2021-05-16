# importing the required libraries
from kloppy import TRACABSerializer, to_pandas

import numpy as np
import os
import pandas as pd
import time
import functools

import GameViewer as gw
import Game as ga


start_time = time.time()

# loading the dataset
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

with open("sorteddata/2081780.dat", "rb") as raw, \
        open("sorteddata/2081780_metadata.xml", "rb") as meta:
    new_data_set = to_pandas(serializer.deserialize(
        inputs={
            'raw_data': raw,
            'metadata': meta
        },
        options={
            'only_alive': False,
            'sample_rate': 1/100
        }
    )
    )
#home_players_positions = gw.GameViewer.prepare_players(frame=500, teamtype=gw.GameViewer.TeamType.HOME)
#print(home_players_positions)
#print("Hey", gw.GameViewer.prepare_players(500, gw.TeamType.HOME))

new_data_set.dropna(how='all')
data_set.dropna(how='all')
'''
print(type(data_set), data_set.keys())
print(type(new_data_set), new_data_set.keys())

print(data_set.iloc[:, 0] == 2)
print(data_set.iloc[0, :])
'''


'''
data_set_array = np.array(data_set)
period = data_set_array[:, 0]
locations = np.array(data_set_array[:, 4:], dtype=np.float64)
nan_array = np.isnan(locations)
not_nan_array = ~ nan_array
locations = np.array(locations[not_nan_array])
collected = np.append(period, locations)
print("collected", collected.shape)
'''

'''
data_set_dropped = data_set.drop(columns=['timestamp', 'ball_state', 'ball_owning_team_id'])
print(data_set_dropped)

data_set_dropped = data_set_dropped[data_set_dropped['period_id'] == 2]
print(data_set_dropped)
data_set_dropped = data_set_dropped.iloc[:, 1:] * -1
print(data_set_dropped)
'''
'''
print(data_set.loc[data_set['period_id'] == 2])
data_set.apply(data_set * -1, rows=data_set.loc[data_set['period_id'] == 2], columns=[data_set.iloc[:, 4:]])
print(data_set)
#= data_set.iloc[:, 4:].apply(lambda x: x*100 if x < 10 else x)
'''

data_set.loc[data_set['period_id'] == 2] = data_set.loc[data_set['period_id'] == 2].mul(-1, axis=0)
new_data_set.loc[new_data_set['period_id'] == 2] = new_data_set.loc[new_data_set['period_id'] == 2].mul(-1, axis=0)
#print(data_set)

#pd.set_option('display.max_columns', None)
#print(data_set.iloc[0:5, :])

# position of (x,y) ball
locs_ball = np.asarray(data_set.iloc[:, [4, 5]])
locs_ball2 = np.asarray(new_data_set.iloc[:, [4, 5]])
#print(locs_ball)
#print(locs_ball2)


#allplayers = data_set.loc[:, data_set.columns.str.contains("home|away")]
# Switch Home and Away if we are Away - so that we are blue in the plot
away = data_set.loc[:, data_set.columns.str.contains("ball_x|ball_y|home")]
home = data_set.loc[:, data_set.columns.str.contains('ball_x|ball_y|away')]
new_away = new_data_set.loc[:, new_data_set.columns.str.contains("ball_x|ball_y|home")]
new_home = new_data_set.loc[:, new_data_set.columns.str.contains('ball_x|ball_y|away')]
##home = data_set.loc[:,data_set.columns.str.contains("home")]
##away = data_set.loc[:,data_set.columns.str.contains("away")]

#players = max(home.shape[1] / 2, away.shape[1] / 2)

# (x,y) positions of home and away players
locs_home = np.array([np.asarray(home.iloc[:, range(j * 2, j * 2 + 2)]) for j in range(int(home.shape[1] / 2))])
locs_away = np.array([np.asarray(away.iloc[:, range(j * 2, j * 2 + 2)]) for j in range(int(away.shape[1] / 2))])

vectorAdd = np.array([5250, 3400])
vectorMeters = np.array([100, 100])
locs_home += vectorAdd
locs_home = locs_home / vectorMeters

new_locs_home = np.array([np.asarray(home.iloc[:, :])])
new_locs_home2 = np.array([np.asarray(new_home.iloc[:, :])])

new_locs_away = np.array([np.asarray(away.iloc[:, :])])
new_locs_away2 = np.array([np.asarray(new_away.iloc[:, :])])

#print("New locs home: ", new_locs_home[:, 0])
#print((new_locs_home).shape)  # (1, 141173, 28) #(1, 2884, 28)
#print((new_locs_home2).shape)  # (1, 141173, 28) #(1, 2884, 28)
rows_count = new_locs_home.shape[1]
#print("Rows count : ", rows_count)
rows_count2 = new_locs_home2.shape[1]

# remove nan's
nan_array = np.isnan(new_locs_home)
nan_array2 = np.isnan(new_locs_home2)
nan_array_away = np.isnan(new_locs_away)
nan_array_away2 = np.isnan(new_locs_away2)

not_nan_array = ~ nan_array
not_nan_array2 = ~ nan_array2
not_nan_array_away = ~ nan_array_away
not_nan_array_away2 = ~ nan_array_away2

new_locs_home = new_locs_home[not_nan_array]
new_locs_home2 = new_locs_home2[not_nan_array2]
new_locs_away = new_locs_away[not_nan_array_away]
new_locs_away2 = new_locs_away2[not_nan_array_away2]

#print(new_locs_home)
#print((new_locs_home).shape)  # (3105806,) #(,71064) #(,55832)

new_locs_home = new_locs_home.reshape(rows_count, 24)
new_locs_home2 = new_locs_home2.reshape(rows_count2, 24)
new_locs_away = new_locs_away.reshape(rows_count, 24)
new_locs_away2 = new_locs_away2.reshape(rows_count2, 24)

#print("Hej: ", new_locs_home)
#print((new_locs_home).shape)
#print("Hej 2: ", new_locs_home)
#print((new_locs_home2).shape)

# reshape to keep it a 2D array
# new_locs_home = new_locs_home.reshape(1, 141173, 22)
# new_locs_home = new_locs_home.reshape(1, 2884, 22)

# convert to int
new_locs_home = np.array(new_locs_home).astype(int)
new_locs_home2 = np.array(new_locs_home2).astype(int)
new_locs_away = np.array(new_locs_away).astype(int)
new_locs_away2 = np.array(new_locs_away2).astype(int)
from scipy.spatial.distance import squareform, euclidean
from scipy import spatial

rows_count = new_locs_home.shape[0]
rows_count_away = new_locs_away.shape[0]
rows_count2 = new_locs_home2.shape[0]
rows_count_away2 = new_locs_away2.shape[0]
#print("Rows count : ", rows_count)
#print("Rows count new: ", rows_count2)

'''
hhyg = new_locs_home.reshape(11,rows_count, 2)
print("hhyg shape: ", hhyg.shape)
print("hhyg", hhyg[:, 0])
for i in range(hhyg):
    spatial.distance.cdist(hhyg[:, i], hhyg[:, i], 'euclidean')
print("dist: ", hhyg[:,0])'''

# new_locs_home = np.delete(new_locs_home, np.argwhere(new_locs_home >= 0))
new_locs_home = new_locs_home.reshape(1, rows_count, 24)
new_locs_home2 = new_locs_home2.reshape(1, rows_count2, 24)
new_locs_away = new_locs_away.reshape(1, rows_count_away, 24)
new_locs_away2 = new_locs_away2.reshape(1, rows_count_away2, 24)
#print("New locs home: ", new_locs_home)
#print("New locs home shape: ", (new_locs_home).shape)  # (1, 141173, 22) #(1, 2884, 28)


# -- Get a row from GameViewer --


# -- Get 1 random row --
random_indices_2 = 0
random_rows_2 = new_locs_home[:, random_indices_2]
random_rows_away = new_locs_away[:, random_indices_2]
# print(random_rows_2)
# print((random_rows_2).shape) #(1, 10, 28)
random_rows_2 = random_rows_2.reshape(1, 24)  # (1,22)
random_rows_away = random_rows_away.reshape(1, 24)
# print(random_rows_2)
# print((random_rows_2).shape)

# full_data = new_locs_home.reshape(141173, 22)
full_data = new_locs_home.reshape(rows_count, 24)  # (2884, 22)
full_data2 = new_locs_home2.reshape(rows_count2, 24)
full_data_away = new_locs_away.reshape(rows_count_away, 24)
full_data_away2 = new_locs_away2.reshape(rows_count_away2, 24)


from sklearn.neighbors import KDTree

sample = random_rows_2
sample_away = random_rows_away
neighbors_count = 4

print("Data: ", full_data)
print("Sample row number: ", random_indices_2)
print("Sample row: ", sample)
tree = KDTree(full_data2)
tree_away = KDTree(full_data_away2)
dist, ind = tree.query(sample, k=neighbors_count)
dist_away, ind_away = tree_away.query(sample_away, k=neighbors_count)
closest_neighbors = full_data2[ind.tolist()[0]]
closest_neighbors_away = full_data_away2[ind_away.tolist()[0]]

print("Three closest neighbors : ", closest_neighbors)
print("NN search done in")
print("--- %s seconds ---" % (time.time() - start_time))
print(closest_neighbors)

print("kig her", closest_neighbors[0, 0:2])

import matplotlib.pyplot as plt
from matplotsoccer import field
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = r'C:\FFMpeg\bin\ffmpeg.exe'

start_time = time.time()

colMap = 'PuOr'
match = 'distance.mp4'

tt = data_set['timestamp']

jitter = 1e-12  # to avoid division by zero when players are standing still

sample_reshape = sample.reshape(1, 12, 2)
sample_away_reshape = sample_away.reshape(1, 12, 2)
closest_neighbors_reshape = closest_neighbors.reshape(neighbors_count, 12, 2)
closest_neighbors_away_reshape = closest_neighbors_away.reshape(neighbors_count, 12, 2)

print("kig b", sample_reshape)
print(closest_neighbors_reshape)
print((sample_reshape).shape)  # (1, 14, 2)
print((closest_neighbors_reshape).shape)


vectorAdd = np.array([5250, 3400])
vectorMeters = np.array([100, 100])

sample_reshape += vectorAdd
sample_reshape = sample_reshape / vectorMeters
sample_away_reshape += vectorAdd
sample_away_reshape = sample_away_reshape / vectorMeters
print("Sample reshape : ", sample_reshape)

closest_neighbors_reshape += vectorAdd
closest_neighbors_reshape = closest_neighbors_reshape / vectorMeters
closest_neighbors_away_reshape += vectorAdd
closest_neighbors_away_reshape = closest_neighbors_away_reshape / vectorMeters
print("Closest neighbor reshape : ", closest_neighbors_reshape)


print("X coords Closest #1: ", closest_neighbors_reshape[0, :, 0])
print("Y coords closest #1: ", closest_neighbors_reshape[0, :, 1])
print(sample_away_reshape[:, 0:1, 0], sample_away_reshape[:, 0:1, 1])

print("X coords Closest #2: ", closest_neighbors_away_reshape[1, :, 0])
print("Y coords closest #2: ", closest_neighbors_away_reshape[1, :, 1])
print(closest_neighbors_away_reshape[1, 0:1, 0], closest_neighbors_away_reshape[1, 0:1, 1])

print("X coords Closest #3: ", closest_neighbors_away_reshape[2, :, 0])
print("Y coords closest #3: ", closest_neighbors_away_reshape[2, :, 1])
print(closest_neighbors_away_reshape[2, 0:1, 0], closest_neighbors_away_reshape[2, 0:1, 1])

print("X coords Closest #4: ", closest_neighbors_away_reshape[3, :, 0])
print("Y coords closest #4: ", closest_neighbors_away_reshape[3, :, 1])
print(closest_neighbors_away_reshape[3, 0:1, 0], closest_neighbors_away_reshape[3, 0:1, 1])


fig, subs = plt.subplots(2, 2)
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

field(ax=subs[0][0], show=False)
subs[0][0].scatter(sample_away_reshape[:, 0:1, 0], sample_away_reshape[:, 0:1, 1],
                   color='black', zorder=10)
subs[0][0].scatter(sample_away_reshape[:, 1:, 0], sample_away_reshape[:, 1:, 1],
                   color='red', zorder=10)
subs[0][0].set_title("Random Sample - frame %i" % random_indices_2)

field(ax=subs[0][1], show=False)
subs[0][1].scatter(closest_neighbors_away_reshape[1, 0:1, 0], closest_neighbors_away_reshape[1, 0:1, 1],
                   color='black', zorder=10)
subs[0][1].scatter(closest_neighbors_away_reshape[1, 1:, 0], closest_neighbors_away_reshape[1, 1:, 1],
                   color='red', zorder=10)
subs[0][1].set_title("N#1 - frame %i" % ind[0, 1])

field(ax=subs[1][0], show=False)
subs[1][0].scatter(closest_neighbors_away_reshape[2, 0:1, 0], closest_neighbors_away_reshape[2, 0:1, 1],
                   color='black', zorder=10)
subs[1][0].scatter(closest_neighbors_away_reshape[2, 1:, 0], closest_neighbors_reshape[2, 1:, 1],
                   color='red', zorder=10)
subs[1][0].set_title("N#2 - frame %i" % ind[0, 2])

field(ax=subs[1][1], show=False)
subs[1][1].scatter(closest_neighbors_away_reshape[3, 0:1, 0], closest_neighbors_away_reshape[3, 0:1, 1],
                   color='black', zorder=10)
subs[1][1].scatter(closest_neighbors_away_reshape[3, 1:, 0], closest_neighbors_away_reshape[3, 1:, 1],
                   color='red', zorder=10)
subs[1][1].set_title("N#3 - frame %i" % ind[0, 3])

plt.tight_layout()
plt.axis("on")
plt.show()

#voro = np.array(home_players_positions)
#vor = Voronoi(voro)
#voronoi_plot_2d(vor, ax=self.ax)