"""
My solution to Day 6 problem on Advent of Code 2023
"""

import re

boat_race = ["Time:        49     97     94     94",
             "Distance:   263   1532   1378   1851"]


# Part 1
times = [int(i) for i in re.split(r' +', re.split("\: +", boat_race[0])[1])]
distances = [int(i) for i in re.split(r' +', re.split("\: +", boat_race[1])[1])]

ways_to_win = []
for i in range(len(times)):
    time = times[i]
    max_distance = distances[i]
    wins = []
    for ms in range(1, time):
        dist = ms * (time - ms)
        if dist > max_distance:
            wins.append(True)
    ways_to_win.append(sum(wins))
margin_of_error = 1
for wins in ways_to_win:
    margin_of_error *= wins
print(margin_of_error)


# Part 2
times = re.split(r' +', re.split("\: +", boat_race[0])[1])
distances = re.split(r' +', re.split("\: +", boat_race[1])[1])

time = ""
for digits in times:
    time += digits
time = int(time)

max_distance = ""
for digits in distances:
    max_distance += digits
max_distance = int(max_distance)

wins = []
for ms in range(1, time):
    dist = ms * (time - ms)
    if dist > max_distance:
        wins.append(True)

ways_to_win = sum(wins)
print(ways_to_win)
