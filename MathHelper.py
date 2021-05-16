import math

import numpy as np
import time


def cart2sph(x, y, z):
	hxy = np.hypot(x, y)
	r = np.hypot(hxy, z)
	el = np.arctan2(z, hxy)
	az = np.arctan2(y, x)
	return az, el, r


def sph2cart(az, el, r):
	rcos_theta = r * np.cos(el)
	x = rcos_theta * np.cos(az)
	y = rcos_theta * np.sin(az)
	z = r * np.sin(el)
	return x, y, z


def dist_between(coord1, coord2):
	# players have always Z=0. so for dist(player, player) z_factor will be equal to 0.
	#  In case dist(player, ball) the distance function disregards first 2 meters of ball altitude
	player_height = 200  # cm
	z_factor = max(player_height, coord1.z - coord2.z) - player_height
	return math.sqrt((coord1.x - coord2.x) ** 2 + (coord1.y - coord2.y) ** 2 + z_factor ** 2)


def vector_length(vector):
	n_array = np.array(vector)
	return np.linalg.norm(n_array)


def normalize_vector(vector):
	x = np.array(vector)
	x = x / x.max()
	return x


def flip_array_values(vector):
	vector = np.array(vector)
	vector = vector.max() - vector
	return vector


def calculate_ball_movement(frame1, frame2):
	vector = np.array([frame1.ball.coord.x - frame2.ball.coord.x, frame1.ball.coord.y - frame2.ball.coord.y,
					   frame1.ball.coord.z - frame2.ball.coord.z])
	speed = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
	return speed, vector


def calculate_event_time_since_period_start(event):
	sec = event.sec
	minute = event.min
	period = event.period_id
	total_sec = minute * 60 + sec - (period - 1) * 45 * 60
	return total_sec


def differentiate_vector(vector):
	result = []
	result.append(vector[1] - vector[0])
	for i in range(len(vector) - 1):
		result.append(vector[i + 1] - vector[i])
	return result


def cut_values_above(threshold, vector):
	ret = []
	for val in vector:
		if val < threshold:
			ret.append(val)
		else:
			ret.append(0)
	return ret


def smooth_vector(vector):
	avg_range = 6
	ret_vector = []
	# padding
	for _ in range(int(avg_range / 2)):
		ret_vector.append(vector[0])

	for i in range(int(avg_range / 2), int(len(vector) - avg_range / 2)):
		sum = 0
		for j in range(int(i - avg_range / 2), int(i + avg_range / 2)):
			sum += vector[j]
		ret_vector.append(sum / avg_range)

	# padding
	for _ in range(int(avg_range / 2)):
		ret_vector.append(vector[-1])

	return np.array(ret_vector)


def hex_to_RGB(hex):
	''' "#FFFFFF" -> [255,255,255] '''
	# Pass 16 to the integer function for change of base
	return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
	''' [255,255,255] -> "#FFFFFF" '''
	# Components need to be integers for hex to make sense
	RGB = [int(x) for x in RGB]
	return "#" + "".join(["0{0:x}".format(v) if v < 16 else
						  "{0:x}".format(v) for v in RGB])


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
	''' returns a gradient list of (n) colors between
	  two hex colors. start_hex and finish_hex
	  should be the full six-digit color string,
	  inlcuding the number sign ("#FFFFFF") '''
	# Starting and ending colors in RGB form
	s = hex_to_RGB(start_hex)
	f = hex_to_RGB(finish_hex)
	# Initilize a list of the output colors with the starting color
	RGB_list = [s]
	# Calcuate a color at each evenly spaced value of t from 1 to n
	for t in range(1, n):
		# Interpolate RGB vector for color at the current value of t
		curr_vector = [
			int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
			for j in range(3)
		]
		# Add it to our list of output colors
		RGB_list.append(curr_vector)

	return color_dict(RGB_list)


def color_dict(gradient):
	''' Takes in a list of RGB sub-lists and returns dictionary of
	  colors in RGB and hex form for use in a graphing function
	  defined later on '''
	return {"hex": [RGB_to_hex(RGB) for RGB in gradient],
			"r": [RGB[0] for RGB in gradient],
			"g": [RGB[1] for RGB in gradient],
			"b": [RGB[2] for RGB in gradient]}
