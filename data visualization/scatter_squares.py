import matplotlib.pyplot as plt

# plt.scatter(2,4, s = 200)     # s = size
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]


# plt.scatter(x_values, y_values, c = 'red', s = 40)
# plt.scatter(x_values, y_values, c = (0,0,0.8), s = 40)

# colormap (series of colors in gradient)
plt.scatter(x_values, y_values, c= y_values, cmap = plt.cm.Blues, edgecolor = 'none', s=40)

# set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()

# saving plots
plt.savefig('squares_plt.png', bbox_inches = 'tight')