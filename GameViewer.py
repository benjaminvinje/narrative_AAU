
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

from Coord import Coord
from EventType import EventType
from TeamType import TeamType

from scipy.spatial import Voronoi, voronoi_plot_2d





class GameViewer:
	def __init__(self, game):
		self.game = game
		self.fig, self.ax = plt.subplots(figsize=(12, 14))


		self.animation = None
		self.ball_plot = None
		self.home_players_plot = None
		self.away_players_plot = None
		self.referees_plot = None
		self.event_name_plot = None
		self.ball_vector_plot = None
		self.event_location_plot = None
		self.home_shirt_numbers_plots = []
		self.away_shirt_numbers_plots = []
		self.home_player_arrows_plots = []
		self.away_player_arrows_plots = []
		self.current_second = 0
		self.current_minute = 0
		self.score_board = None
		self.score_board_X = -5000
		self.score_board_Y = 4000
		self.start_frame_index = 0
		self.running = True
		self.forward = True
		self.i = 0
		self.dot_size = 230
		self.static_event_marker_size = 40
		self.events_in_last_sec = set()
		self.event_location_plot_visible = False
		self.ui_window = None
		self.home_color = '#f4a582'
		self.home_edge_color = "#ca0020"
		self.away_edge_color = "#0571b0"
		self.away_color = '#92c5de'
		self.font = "DejaVu Sans"
		self.show_reception = False
		self.x_min = -6000
		self.x_max = 6000
		self.y_min = -4000
		self.y_max = 5000


	def iterator_generator(self):
		while self.running:
			if self.forward:
				self.i += 1
				yield self.i
			else:
				self.i -= 1
				yield self.i

	def show(self, start_frame_id=0, minute=0, second=0, period=0):
		self.start_frame_index = self.select_start_index(start_frame_id, minute, second, period)
		self.i = self.start_frame_index
		self.animation = animation.FuncAnimation(self.fig, self.update_plot, init_func=self.setup_plot, interval=40,
												 blit=True, frames=self.iterator_generator())

	def setup_plot(self):
		self.ax.clear()
		initial_frame = self.game.frames[self.game.get_index_by_id(self.game.first_period_frame_id)]
		#print("ini frame", initial_frame)

		home_players_positions = self.prepare_players(frame=initial_frame, teamtype=TeamType.HOME)

		self.home_players_plot = self.ax.scatter(home_players_positions[:, 0], home_players_positions[:, 1],
												 c=self.home_color, edgecolors=self.home_edge_color, s=self.dot_size)
		#voro = np.array(home_players_positions)
		#vor = Voronoi(home_players_positions)
		#voronoi_plot_2d(vor, ax=self.ax)
		away_players_positions = self.prepare_players(frame=initial_frame, teamtype=TeamType.AWAY)
		self.away_players_plot = self.ax.scatter(away_players_positions[:, 0], away_players_positions[:, 1],
												 c=self.away_color, edgecolors=self.away_edge_color, s=self.dot_size)

		self.event_location_plot = self.ax.scatter([], [], s=1500, linewidth=3, marker="8", facecolors='none',
												   edgecolors='purple')

		# referees_positions = self.prepare_players(frame=initial_frame, teamtype=-1)
		# self.referees_plot = self.ax.scatter(referees_positions[:, 0], referees_positions[:, 1], c='#EAF039')

		ball_size = initial_frame.ball.coord.z / 5 + 10
		self.ball_plot = self.ax.scatter(initial_frame.ball.coord.x,
										 initial_frame.ball.coord.y, s=ball_size,
										 c='black')
		# self.initialize_slider()
		self.ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
		self.ax.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)

		self.pitch_plot = self.create_pitch_plot()
		self.fig.tight_layout()

		self.home_player_arrows_plots = []
		self.away_player_arrows_plots = []

		home_players = self.game.get_players_by_team_type_from_frame(TeamType.HOME, initial_frame)
		away_players = self.game.get_players_by_team_type_from_frame(TeamType.AWAY, initial_frame)
		for player in home_players:
			self.home_shirt_numbers_plots.append(
				self.ax.text(player.coord.x, player.coord.y, "", fontsize=9, ha="center", fontname=self.font))

			self.home_player_arrows_plots.append(self.ax.plot([], [], color=self.home_edge_color, zorder=-1)[0])

		for player in away_players:
			self.away_shirt_numbers_plots.append(
				self.ax.text(player.coord.x, player.coord.y, "", fontsize=9, ha="center", fontname=self.font))

			self.away_player_arrows_plots.append(self.ax.plot([], [], color=self.away_edge_color, zorder=-1)[0])

		self.event_name_plot = self.ax.text(-5000, 3500, "", fontsize=12, ha="left", fontname=self.font)
		self.ball_vector_plot = self.ax.text(-2000, 4500, "", fontsize=13, fontname=self.font)

		self.setup_score_board()

		self.ax.set_xlim([self.x_min, self.x_max])
		self.ax.set_ylim([self.y_min, self.y_max])
		self.ax.set_facecolor('xkcd:light green')
		# self.fig.patch.set_facecolor('xkcd:light green')


		return (self.home_players_plot, self.away_players_plot, self.ball_plot,
				# self.referees_plot,
				self.event_name_plot, self.score_board, self.ball_vector_plot, self.pitch_plot,)


	# updates the plot with a frame of given index i
	def update_plot(self, i):
		current_frame = self.game.frames[i]

		self.ball_plot.set_offsets([current_frame.ball.coord.x, current_frame.ball.coord.y])
		self.ball_plot.set_sizes([current_frame.ball.coord.z / 5 + 25])

		away_players_positions = self.prepare_players(frame=current_frame, teamtype=TeamType.AWAY)

		self.away_players_plot.set_offsets(away_players_positions)


		home_players_positions = self.prepare_players(frame=current_frame, teamtype=TeamType.HOME)

		self.home_players_plot.set_offsets(home_players_positions)

		if self.has_game_started(current_frame):
			self.update_score_board(current_frame)


		self.prepare_shirt_number_plots(current_frame)
		self.prepare_player_arrows_plots(current_frame)

		if i % 1000 == 0:
			print('{0}/{1}'.format(i, len(self.game.frames)))

		return self.prepare_animation_update_tuple()



	def prepare_shirt_number_plots(self, current_frame):
		home_players = self.game.get_players_by_team_type_from_frame(TeamType.HOME, current_frame)
		away_players = self.game.get_players_by_team_type_from_frame(TeamType.AWAY, current_frame)
		self.prepare_one_team_shirt_plots(home_players, self.home_shirt_numbers_plots)
		self.prepare_one_team_shirt_plots(away_players, self.away_shirt_numbers_plots)

	def prepare_one_team_shirt_plots(self, players, number_plots):
		for i in range(len(players)):
			try:
				number_plots[i].set_position(
					[players[i].coord.x, players[i].coord.y - self.dot_size / 4])
				number_plots[i].set_text(players[i].number)
			except IndexError:
				print("HeisenException")

	def prepare_player_arrows_plots(self, current_frame):
		home_players = self.game.get_players_by_team_type_from_frame(TeamType.HOME, current_frame)
		away_players = self.game.get_players_by_team_type_from_frame(TeamType.AWAY, current_frame)
		self.prepare_one_team_arrows_plots(home_players, self.home_player_arrows_plots, current_frame)
		self.prepare_one_team_arrows_plots(away_players, self.away_player_arrows_plots, current_frame)

	def prepare_one_team_arrows_plots(self, players, arrows_plots, frame):
		frame_idx = self.game.get_index_by_id(frame.id)
		for i, plot in enumerate(arrows_plots):
			if i >= len(
					players):  # if a player gets red card in the game, then len of players shortens by one and there is a possibility of trying to plor an arrow of the lost player. The arrow's coordinates are away from the pitch
				plot.set_data([-10000, -10000], [-10000, -10000])
				continue

			dx_s = []
			dy_s = []
			for j in range(0, 5):

				try:
					player = self.game.get_tracking_player_by_frame_index_and_track_player(frame_idx - j, players[i])
					prev_player = self.game.get_tracking_player_by_frame_index_and_track_player(frame_idx - j - 1,
																								players[i])
				except IndexError:
					return

				if player is None or prev_player is None:
					continue

				position = player.coord
				prev_position = prev_player.coord
				dx_s.append(position.x - prev_position.x)
				dy_s.append(position.y - prev_position.y)

			dx = np.average(dx_s)
			dy = np.average(dy_s)
			dx *= 20
			dy *= 20

			plot.set_data([players[i].coord.x, players[i].coord.x + dx], [players[i].coord.y, players[i].coord.y + dy])

	def has_game_started(self, current_frame):
		return current_frame.id > self.game.frames[self.game.get_index_by_id(self.game.first_period_frame_id)].id

	def prepare_players(self, frame, teamtype):
		positions = []
		for track_player in frame.players:
			if track_player.team_type == teamtype:
				positions.append([track_player.coord.x, track_player.coord.y])
		if len(positions) == 0:
			positions.append([0, 0])
		return np.asarray(positions)

	def prepare_animation_update_tuple(self):
		# order of adding plots to a final tuple matters. The sooner a plot will be added, the lower will be its
		# z-index on a graph (at least on linux)
		t0 = tuple(self.home_player_arrows_plots)
		t05 = tuple(self.away_player_arrows_plots)
		t1 = tuple([self.home_players_plot])
		t2 = tuple(self.home_shirt_numbers_plots)
		t3 = (self.away_players_plot,
			  # self.referees_plot,
			  self.ball_plot, self.event_name_plot, self.ball_vector_plot, self.pitch_plot,
			  self.score_board)
		t4 = tuple(self.away_shirt_numbers_plots)
		return t0 + t05 + t1 + t2 + t3 + t4

	def is_change_ball_status(self):
		return self.game.frames[self.i].ball.alive != self.game.frames[
			self.i + 1].ball.alive

	def is_change_ball_possession(self):
		return self.game.frames[self.i].ball.possession != self.game.frames[
			self.i + 1].ball.possession

	def update_score_board(self, current_frame):
		self.update_current_second(current_frame)
		currentframe = self.i / self.game.position_frequency
		minutes = int(currentframe / 60)
		seconds = int(currentframe - minutes * 60)
		home_team_text = "{0} {1}".format(self.game.get_team_by_team_type(TeamType.HOME),
										  self.game.get_goals_by_team_type_and_frame(TeamType.HOME, current_frame))
		away_team_text = "{0} {1}".format(self.game.get_team_by_team_type(TeamType.AWAY),
										  self.game.get_goals_by_team_type_and_frame(TeamType.AWAY, current_frame))
		clock_text = "{0}:{1:02d}".format(minutes, seconds)
		text = "{0}\n{1}\n{2}".format(home_team_text, away_team_text, clock_text)
		self.score_board.set_text(text)
		# update slider when a minute changes
		if self.current_minute != minutes:
			# if self.i % 25 == 0	:
			# self.disable_slider_event()
			# self.slider.set_val(minutes * 60)
			self.current_minute = minutes

	# self.enable_slider_event()

	def update_current_second(self, current_frame):
		if current_frame.id < self.game.second_period_frame_id:
			frames_num = current_frame.id - self.game.first_period_frame_id
		else:
			frames_num = current_frame.id - self.game.second_period_frame_id + 45 * 60 * self.game.position_frequency

		self.current_second = int(frames_num / self.game.position_frequency)

	'''
	def update_event(self):
		frame_events_in_last_sec = set()
		for j in range(self.game.position_frequency):
			frame_events = self.game.frames[self.i - j].frame_events
			for event in frame_events:
				frame_events_in_last_sec.add(event.id)

		self.events_in_last_sec = []
		display_text = ""
		for id in frame_events_in_last_sec:
			event = self.game.get_event_by_event_id(id)

			if event is not None:
				if event.type == EventType.RECEPTION and not self.show_reception:
					continue
				if event.type == EventType.CARRY:
					continue

				display_text += self.game.determine_event_text(event) + ";     "
				self.events_in_last_sec.append(event)

		self.event_name_plot.set_text(display_text)
		self.ui_window.select_events(self.events_in_last_sec)
'''
	def select_start_index(self, start_frame_id, minute, second, period):
		if start_frame_id == 0 and minute == 0 and second == 0:
			return self.game.get_index_by_id(self.game.first_period_frame_id)
		elif start_frame_id != 0:
			return self.game.get_index_by_id(start_frame_id)
		else:
			return self.game.get_index_by_time(minute, second, period)

	def start_or_pause_animation(self):
		if self.running:
			self.animation.event_source.stop()
		else:
			self.animation.event_source.start()

		self.running = not self.running

	def pause_animation(self):
		self.running = False
		self.animation.event_source.stop()

	def on_click(self, evt):
		print('Clicked location on the pitch: x: {0}, y: {1}'.format(evt.xdata, evt.ydata))
		print('Current frame is ', self.i)
		print('Current frame ID: ', self.game.frames[self.i].id)



	def handle_close(self, evt):
		print('Window closed during frame # {0} out of {1}'.format(self.i, len(self.game.frames)))

	def update_ball_vector(self):
		vec = self.game.frames[self.i].ball.vector
		self.ball_vector_plot.set_text("Ball Vector:[{0}, {1}, {2}]".format(vec[0], vec[1], vec[2]))


	def show_frame_by_frame_id(self, frame_id):
		self.i = self.game.get_index_by_id(frame_id)
		self.fig.canvas.draw()
		x = self.update_plot(self.i)
		for z in x:
			self.fig.draw_artist(z)


	def draw_team_rectangles(self, x, y):
		home_rect = patches.Rectangle((x - 200, y + 430), 150, 150, linewidth=1, edgecolor=self.home_edge_color,
									  facecolor=self.home_color)
		away_rect = patches.Rectangle((x - 200, y + 230), 150, 150, linewidth=1, edgecolor=self.away_edge_color,
									  facecolor=self.away_color)
		self.ax.add_patch(home_rect)
		self.ax.add_patch(away_rect)

	def draw_score_board_bg(self, x, y):
		height = 700
		width = 2000
		x1 = [x - 300, x + width, x + width, x - 300]
		y1 = [y - 100, y - 100, y + height, y + height]
		self.ax.fill(x1, y1, facecolor="white", color="#1E3277", edgecolor="#061B49", capstyle="round")

	def draw_static_events_arrows(self, events, home_colors, away_colors):
		for i, event in enumerate(events):
			color = home_colors.pop(0) if event.team.team_type == TeamType.HOME else away_colors.pop(0)
			if not event.has_end_coords():
				continue
			x = event.coord.x
			y = event.coord.y
			x_length = event.coord_end.x - event.coord.x
			y_length = event.coord_end.y - event.coord.y

			linestyle = (10, (5, 10)) if event.type == EventType.CARRY else "-"

			self.ax.arrow(x, y, x_length, y_length, head_width=100, head_length=200, fc=color, ec=color, zorder=11,
						  length_includes_head=True, ls=linestyle)

	def draw_static_events(self, events, show_text):
		x_s = []
		y_s = []
		for i, event in enumerate(events):
			x = event.coord.x
			y = event.coord.y

			x_s.append(x)
			y_s.append(y)
			if show_text:
				self.ax.text(x, y - 200, self.game.determine_short_event_text(event), fontsize=9,
							 horizontalalignment='center')

			color = self.home_edge_color if event.team.team_type == TeamType.HOME else self.away_edge_color
			z = self.ax.scatter(x, y, c=color, s=self.static_event_marker_size, zorder=10)

		self.ax.set_xlim([self.x_min, self.x_max])
		self.ax.set_ylim([self.y_min, self.y_max])


	def create_pitch_plot(self):
		w, h = self.game.get_pitch_dimensions()
		w_cm = w * 100
		h_cm = h * 100
		goal_height = 7.32 * 100
		linewidth = 3
		color = 'white'
		# https://upload.wikimedia.org/wikipedia/commons/9/96/Football_pitch_metric_and_imperial.svg
		# pitch frame
		# pitch, = self.ax.fill([-w_cm / 2, w_cm / 2, w_cm / 2, -w_cm / 2, -w_cm / 2],
		# 					  [h_cm / 2, h_cm / 2, -h_cm / 2, -h_cm / 2, h_cm / 2], c='xkcd:light green', linewidth=linewidth)
		pitch, = self.ax.plot([-w_cm / 2, w_cm / 2, w_cm / 2, -w_cm / 2, -w_cm / 2],
							  [h_cm / 2, h_cm / 2, -h_cm / 2, -h_cm / 2, h_cm / 2], c=color, linewidth=linewidth)

		# rect = patches.Rectangle((-w_cm / 2, -h_cm / 2), w_cm, h_cm, linewidth=linewidth, edgecolor='w', facecolor='xkcd:light green')

		# Add the patch to the Axes
		# self.ax.add_patch(rect)

		# middle line
		pitch, = self.ax.plot([0, 0], [-h_cm / 2, h_cm / 2], c=color, linewidth=linewidth)
		# middle circle
		theta = np.linspace(0, 2 * np.pi, 100)
		r = 9.15 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(x1, x2, c=color, linewidth=linewidth)
		pitch, self.ax.scatter([0, 0], [0, 0], c=color, s=linewidth * 2)

		# center spot
		pitch, self.ax.scatter([0, 0], [0, 0], c=color, s=linewidth * 10)

		# left penalty area
		penalty_width = 16.5 * 100
		penalty_height = 40.3 * 100
		pitch, = self.ax.plot([-w_cm / 2, -w_cm / 2 + penalty_width, -w_cm / 2 + penalty_width, -w_cm / 2, -w_cm / 2],
							  [penalty_height / 2, penalty_height / 2, - penalty_height / 2, -penalty_height / 2,
							   penalty_height / 2], c=color, linewidth=linewidth)

		# right penalty area
		pitch, = self.ax.plot([w_cm / 2, w_cm / 2 - penalty_width, w_cm / 2 - penalty_width, w_cm / 2, w_cm / 2],
							  [penalty_height / 2, penalty_height / 2, - penalty_height / 2, -penalty_height / 2,
							   penalty_height / 2], c=color, linewidth=linewidth)

		# left goalie area
		goalie_width = 5.5 * 100
		goalie_height = (goal_height + 2 * goalie_width)
		pitch, = self.ax.plot([-w_cm / 2, -w_cm / 2 + goalie_width, -w_cm / 2 + goalie_width, -w_cm / 2, -w_cm / 2],
							  [goalie_height / 2, goalie_height / 2, - goalie_height / 2, -goalie_height / 2,
							   goalie_height / 2], c=color, linewidth=linewidth)

		# right goalie area
		pitch, = self.ax.plot([w_cm / 2, w_cm / 2 - goalie_width, w_cm / 2 - goalie_width, w_cm / 2, w_cm / 2],
							  [goalie_height / 2, goalie_height / 2, - goalie_height / 2, -goalie_height / 2,
							   goalie_height / 2], c=color, linewidth=linewidth)

		penalty_spot = 11 * 100
		pitch, self.ax.scatter([-w_cm / 2 + penalty_spot, w_cm / 2 - penalty_spot], [0, 0], c=color, s=linewidth * 5)

		# left penalty area arc
		arc_const = 0.29
		theta = np.linspace(np.pi * arc_const, -np.pi * arc_const, 100)
		r = 9.15 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(-w_cm / 2 + penalty_spot + x1, x2, c=color, linewidth=linewidth)

		# right penalty area arc
		theta = np.linspace(np.pi * arc_const - np.pi, -np.pi * arc_const - np.pi, 100)
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(w_cm / 2 - penalty_spot + x1, x2, c=color, linewidth=linewidth)

		# left goal
		goal_height = 7.32 * 100
		goal_width = 2.5 * 100
		pitch, = self.ax.plot(
			[-w_cm / 2 - goal_width, -w_cm / 2, -w_cm / 2, -w_cm / 2 - goal_width, -w_cm / 2 - goal_width],
			[goal_height / 2, goal_height / 2, - goal_height / 2, -goal_height / 2,
			 goal_height / 2], c=color, linewidth=linewidth)

		# right goal
		pitch, = self.ax.plot(
			[w_cm / 2, w_cm / 2 + goal_width, w_cm / 2 + goal_width, w_cm / 2, w_cm / 2],
			[goal_height / 2, goal_height / 2, - goal_height / 2, -goal_height / 2,
			 goal_height / 2], c=color, linewidth=linewidth)

		# bottom left corner
		theta = np.linspace(0, np.pi / 2, 100)
		r = 1.5 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(-w_cm / 2 + x1, -h_cm / 2 + x2, c=color, linewidth=linewidth)
		# bottom upper corner
		theta = np.linspace(0, -np.pi / 2, 100)
		r = 1.5 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(-w_cm / 2 + x1, h_cm / 2 + x2, c=color, linewidth=linewidth)
		# bottom right corner
		theta = np.linspace(np.pi / 2, np.pi, 100)
		r = 1.5 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(w_cm / 2 + x1, -h_cm / 2 + x2, c=color, linewidth=linewidth)
		# upper right corner
		theta = np.linspace(np.pi, np.pi * 3 / 2, 100)
		r = 1.5 * 100
		x1 = r * np.cos(theta)
		x2 = r * np.sin(theta)
		pitch, = self.ax.plot(w_cm / 2 + x1, h_cm / 2 + x2, c=color, linewidth=linewidth)

		return pitch

	def setup_score_board(self):
		self.score_board = self.ax.text(self.score_board_X, self.score_board_Y, "", fontsize=12,
										fontname=self.font, color="white")

		self.draw_score_board_bg(self.score_board_X, self.score_board_Y)
		self.draw_team_rectangles(self.score_board_X, self.score_board_Y)

	def reset_pitch(self):
		self.ax.clear()
		self.ax.set_xlim([self.x_min, self.x_max])
		self.ax.set_ylim([self.y_min, self.y_max])
		self.pitch_plot = self.create_pitch_plot()
		self.setup_score_board()
