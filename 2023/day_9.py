"""
My solution to Day 9 problem on Advent of Code 2023
"""

from my_functions import find_next_or_prev_value


# Part 1
with open("advent_9_input.txt") as advent_9_input:
    sum_of_next_values = 0
    for seq in advent_9_input:
        history_seq = [eval(value) for value in seq.split(" ")]
        # print(history_seq)
        next_value = find_next_or_prev_value(history_seq, True)
        # print(next_value)
        sum_of_next_values += next_value
    print(sum_of_next_values)

# Part 2
with open("advent_9_input.txt") as advent_9_input:
    sum_of_prev_values = 0
    for seq in advent_9_input:
        history_seq = [eval(value) for value in seq.split(" ")]
        # print(history_seq)
        prev_value = find_next_or_prev_value(history_seq, False)
        # print(next_value)
        sum_of_prev_values += prev_value
    print(sum_of_prev_values)
  
