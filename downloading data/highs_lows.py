import csv
from datetime import datetime
from matplotlib import pyplot as plt

# # Get dates and high temps from file
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)

#     # for index, column_header in enumerate(header_row):
#     #     print(index, column_header
#     dates, highs = [], list()
#     for row in reader:
#         current_date = datetime.strptime(row[0], '%Y-%m-%d')
#         dates.append(current_date)

#         high = int(row[1])
#         highs.append(high)

# # Plot data
# fig = plt.figure(dpi = 128, figsize=(8,5))
# plt.plot(dates, highs, c = 'red')

# # Format plot
# plt.title('Daily high temperatirues, July 2014', fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (F)', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)

# plt.show()


# Get dates, high and low temps from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data
fig = plt.figure(dpi=130, figsize=(8, 5))
# fig = plt.figure()
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = 'Daily high and low temperatirues - 2014\nDeath Valley, CA'
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
