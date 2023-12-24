"""
My solution to Day 10 problem on Advent of Code 2023
Note: Part 2 was solved with the help of the subreddit; recommending the shoelace formula and Pick's theorem.
"""

from my_functions import find_s_position
from my_functions import find_new_position_and_direction
from my_functions import polygon_area


# Part 1
with open("advent_10_input.txt") as advent_10_input:
    full_map = [line for line in advent_10_input]
    s_position = find_s_position(full_map)
    count = 0
    while True:
        if count == 0:
            for direction in ["N", "E", "S", "W"]:
                new_position_, new_direction_ = find_new_position_and_direction(full_map, s_position, direction)
                if new_position_:
                    break
        else:
            new_position_, new_direction_ = find_new_position_and_direction(full_map, new_position_, new_direction_)
        count += 1
        if new_position_ == s_position:
            print(f"Farthest point: {int(count / 2)}")
            break

        if count == 100000:
            print("Gone too far")
            break


# Part 2
with open("advent_10_input.txt") as advent_10_input:
    full_map = [line for line in advent_10_input]
    s_position = find_s_position(full_map)
    loop_list = []
    vertices = []
    count = 0
    while True:
        if count == 0:
            for direction in ["N", "E", "S", "W"]:
                new_position_, new_direction_ = find_new_position_and_direction(full_map, s_position, direction)
                if new_position_:
                    s_direction = direction
                    break
        else:
            new_position_, new_direction_ = find_new_position_and_direction(full_map, new_position_, new_direction_)
        count += 1
        loop_list.append(new_position_)

        if full_map[new_position_[0]][new_position_[1]] in ["F", "7", "J", "L"]:
            vertices.append(new_position_)

        if new_position_ == s_position:
            if new_direction_ != s_direction:
                vertices.append(new_position_)
            break

        if count == 100000:
            print("Gone too far")
            break
    area = polygon_area(vertices)
    interior_points = int(area - len(loop_list) / 2 + 1)
    print(f"Number of interior points: {interior_points}")
