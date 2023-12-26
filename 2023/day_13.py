"""
My solution to Day 13 problem on Advent of Code 2023
"""

from my_functions import find_summary


# Part 1
with open("advent_13_input.txt") as advent_13_input:
    total_summary = 0
    count = 0
    valley_map = []
    for line in advent_13_input:
        valley_row = line.strip("\n")
        if valley_row == "":
            valley_summary = find_summary(valley_map)
            total_summary += valley_summary
            valley_map = []
            count += 1
        else:
            valley_map.append(valley_row)
    valley_summary = find_summary(valley_map)
    total_summary += valley_summary
    print(total_summary)


# Part 2
with open("advent_13_input.txt") as advent_13_input:
    total_summary = 0
    count = 0
    valley_map = []
    for line in advent_13_input:
        valley_row = line.strip("\n")
        if valley_row == "":
            valley_summary = find_summary(valley_map, False)
            total_summary += valley_summary
            valley_map = []
            count += 1
        else:
            valley_map.append([val for val in valley_row])
    valley_summary = find_summary(valley_map, False)
    total_summary += valley_summary
    print(total_summary)
