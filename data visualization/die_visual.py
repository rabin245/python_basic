import pygal
from die import Die

# create a die
die = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
# hist.force_uri_protocol = 'http'

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
# hist._x_title = 'Result'
# hist._y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('data visualization/die_visual.svg')