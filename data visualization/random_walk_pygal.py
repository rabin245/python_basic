from random import Random
import pygal
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

scatter_plot = pygal.XY(stroke=False)
scatter_plot.title = 'Random Walk Using pygal'
coords = list(zip(rw.x_values, rw.y_values))

scatter_plot.add('Random Walk', coords)
scatter_plot.render_to_file('data visualization/random_walk_pygal.svg')