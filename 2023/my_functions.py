'''
Contains all functions I create to solve the problems on Advent of Code 2023.
'''

import re

# Used in Day 1
def first_or_last_digit(string_with_num, first: bool = True):
    if not first:
        string_with_num = string_with_num[::-1]
    for char in string_with_num:
        if char.isdigit():
            num = char
            break
    return num
    

# Used in Day 1
def first_and_last_digit(string_with_num: str):
    first = first_or_last_digit(string_with_num, first = True)
    last = first_or_last_digit(string_with_num, first = False)
    first_and_last = f"{first}{last}"
    return int(first_and_last)


# Used in Day 1
def fix_string(a_string: str):
    extra_chars = {
        "oneight": "oneeight",
        "twone": "twoone",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight"
    }
    for original, fixed in extra_chars.items():
        a_string = a_string.replace(original, fixed)
    return a_string


# Used in Day 1
def find_word_num_and_replace(a_string: str):
    digits = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    for word, num in digits.items():
        a_string = a_string.replace(word, num)
    return a_string


# Used in Day 2
def find_first_num(string_with_num):
    num = int(re.findall(r'\d+', string_with_num)[0])
    return num


# Used in Day 2, Day 4
def get_game_num(game_string):
    game_num = find_first_num(game_string.split(": ")[0])
    return game_num


# Used in Day 2
def get_game_num_and_sets(game_string):
    game_num = get_game_num(game_string)
    game_sets_ = game_string.split(": ")[1].split("; ")
    game_sets = []
    for game_set_ in game_sets_:
        game_set = game_set_.split(", ")
        game_sets.append(game_set)
    return game_num, game_sets


# Used in Day 2
def update_max_in_colour_dict(colour_dict: dict = None, colour: str = "", a_string: str = ""):
    if colour in a_string:
        num = find_first_num(a_string)
        if num > colour_dict[colour]:
            colour_dict[colour] = num
            

# Used in Day 3
def join_number_indices(list_of_indices):
    number_indices_list = []
    number = []
    for index in list_of_indices:
        if not number:
            number.append(index)
        elif [index[0], index[1] - 1] in number:
            number.append(index)
        else:
            number_indices_list.append(number)
            number = [index]
    number_indices_list.append(number)
    return number_indices_list


# Used in Day 3
def get_numbers_and_symbols(list_of_strings):
    number_indices = []
    symbol_indices = []
    gear_indices = []
    for row_index, string in enumerate(list_of_strings):
        for col_index, char in enumerate(string):
            if re.match("\d", char):
                index = [row_index, col_index]
                number_indices.append(index)
            elif re.match("\*", char):
                index = [row_index, col_index]
                gear_indices.append(index)
                symbol_indices.append(index)
            elif not re.match("\.", char):
                index = [row_index, col_index]
                symbol_indices.append(index)
    return join_number_indices(number_indices), symbol_indices, gear_indices


# Used in Day 3
def get_up_down_index(original_index: list = None, up: bool = True):
    if up:
        new_index = [original_index[0]-1, original_index[1]]
    else:
        new_index = [original_index[0]+1, original_index[1]]
    return new_index


# Used in Day 3
def get_right_left_index(original_index: list = None, left: bool = True):
    if left:
        new_index = [original_index[0], original_index[1]-1]
    else:
        new_index = [original_index[0], original_index[1]+1]
    return new_index


# Used in Day 3
def order_indexes(index_list: list = None, max_row_=9, max_col_=9):
    ordered_list = []
    for r in range(max_row_+1):
        for c in range(max_col_+1):
            if [r, c] in index_list:
                ordered_list.append([r, c])
    return ordered_list


# Used in Day 3
def get_diagonals(original_index: list = None, max_row_=9, max_col_=9):
    diagonals = []
    # get ups and downs
    if original_index[0] == 0:
        diagonals.append(get_up_down_index(original_index, up=False))
    elif original_index[0] == max_row_:
        diagonals.append(get_up_down_index(original_index, up=True))
    else:
        diagonals.append(get_up_down_index(original_index, up=False))
        diagonals.append(get_up_down_index(original_index, up=True))
    # get lefts and rights
    if original_index[1] == 0:
        diagonals.append(get_right_left_index(original_index, left=False))
    elif original_index[1] == max_col_:
        diagonals.append(get_right_left_index(original_index, left=True))
    else:
        diagonals.append(get_right_left_index(original_index, left=False))
        diagonals.append(get_right_left_index(original_index, left=True))
    # get diagonals
    if original_index[0] == 0:
        if original_index[1] == 0:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=False))
        elif original_index[1] == max_col_:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=False))
        else:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=False))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=False))
    elif original_index[0] == max_row_:
        if original_index[1] == 0:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=True))
        elif original_index[1] == max_col_:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=True))
        else:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=True))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=True))
    else:
        if original_index[1] == 0:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=True))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=False))
        elif original_index[1] == max_col_:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=True))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=False))
        else:
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=True))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=False), up=False))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=True))
            diagonals.append(get_up_down_index(get_right_left_index(original_index, left=True), up=False))
    return order_indexes(diagonals, max_row_, max_col_)


# Used in Day 3
def find_all_diagonals(list_of_indices: list = None, max_row=9, max_col=9):
    symbol_diagonals = []
    for index in list_of_indices:
        diagonals = get_diagonals(index, max_row, max_col)
        for diagonal_index in diagonals:
            if diagonal_index not in symbol_diagonals:
                symbol_diagonals.append(diagonal_index)
    return order_indexes(symbol_diagonals, max_row, max_col)


# Used in Day 3
def find_all_gear_diagonals(list_of_indices: list = None, max_row=9, max_col=9):
    symbol_diagonals = []
    for index in list_of_indices:
        gear_diagonal_group = []
        diagonals = get_diagonals(index, max_row, max_col)
        for diagonal_index in diagonals:
            if diagonal_index not in symbol_diagonals:
                gear_diagonal_group.append(diagonal_index)
        symbol_diagonals.append(gear_diagonal_group)
    return symbol_diagonals


# Used in Day 3
def get_part_num_indices(number_indices: list = None, symbol_diagonals: list = None):
    part_num_indices = []
    for number_group in number_indices:
        num_in_diagonal = False
        for number_index in number_group:
            if number_index in symbol_diagonals:
                num_in_diagonal = True
        if num_in_diagonal:
            part_num_indices.append(number_group)
    return part_num_indices


# Used in Day 3
def find_number(string_list: list = None, number_indices: list = None):
    number = ""
    for num_index in number_indices:
        digit = string_list[num_index[0]][num_index[1]]
        number += digit
    number = int(number)
    return number


# Used in Day 3
def get_definite_gear_nums(num_list: list = None, gear_diagonals: list = None):
    num_next_to_gear_check = []
    potential_gear_nums = []
    for num_group in num_list:
        for gear_diagonal in gear_diagonals:
            if gear_diagonal in num_group:
                num_next_to_gear_check.append(True)
                potential_gear_nums.append(num_group)
                break
    definite_gear_nums = []
    if sum(num_next_to_gear_check) == 2:
        definite_gear_nums.append(potential_gear_nums)
    return definite_gear_nums


# Used in Day 3
def get_gear_product(string_list: list = None, gear_nums_indices: list = None):
    gear_number_product = 1
    for gear_num_index in gear_nums_indices:
        gear_num = find_number(string_list, gear_num_index)
        gear_number_product *= gear_num
    return gear_number_product


# Used in Day 4
def get_numbers_from_string(a_string: str, winning_or_chosen: str):
    if winning_or_chosen.lower() in ["w", "winning"]:
        number_list_ = re.split(r' +', re.split(" +\| +", a_string)[0])
    elif winning_or_chosen.lower() in ["c", "chosen"]:
        number_list_ = re.split(r' +', re.split(" +\| +", a_string)[1])
    else:
        print("fix choice")
        return
    number_list = []
    for number in number_list_:
        number_list.append(int(number))
    return number_list


# Used in Day 4
def get_num_of_wins(chosen_nums, winning_nums):
    num_of_wins = 0
    for chosen_num in chosen_nums:
        if chosen_num in winning_nums:
            num_of_wins += 1
    return num_of_wins


# Hold for Day 5 functions


# Used in Day 9
def find_diff(a_list: list = None):
    diff_list = []
    for i in range(len(a_list)-1):
        diff_list.append(a_list[i+1] - a_list[i])
    return diff_list


# Used in Day 9
def find_next_or_prev_value(sequence: list = None, next_: bool = True):
    sequence_diffs = {0: [[], sequence]}
    count = 1
    while True:
        sequence_diffs[count] = [sequence_diffs[count-1][1], find_diff(sequence_diffs[count-1][1])]
        if len(set(sequence_diffs[count][1])) == 1:
            if next_:
                for index in range(count, 0, -1):
                    sequence_diffs[index-1][1].append(sequence_diffs[index-1][1][-1] + sequence_diffs[index][1][-1])
                return sequence_diffs[0][1][-1]
            else:
                for index in range(count, 0, -1):
                    sequence_diffs[index-1][1].insert(0, sequence_diffs[index-1][1][0] - sequence_diffs[index][1][0])
                return sequence_diffs[0][1][0]
        count += 1
        if count > 1000:
            print("over 1000 diffs")
            break


# Used in Day 10
def find_new_position_and_direction(a_map: list = None, current_position: list = None, current_direction: str = "N"):
    new_position = ""
    new_direction = ""
    if current_direction == "N":
        new_position = [current_position[0]-1, current_position[1]]
        if a_map[new_position[0]][new_position[1]] == "7":
            new_direction = "W"
        elif a_map[new_position[0]][new_position[1]] == "|":
            new_direction = "N"
        elif a_map[new_position[0]][new_position[1]] == "F":
            new_direction = "E"
        elif a_map[new_position[0]][new_position[1]] == "S":
            new_direction = "N"
    elif current_direction == "E":
        new_position = [current_position[0], current_position[1]+1]
        if a_map[new_position[0]][new_position[1]] == "J":
            new_direction = "N"
        elif a_map[new_position[0]][new_position[1]] == "-":
            new_direction = "E"
        elif a_map[new_position[0]][new_position[1]] == "7":
            new_direction = "S"
        elif a_map[new_position[0]][new_position[1]] == "S":
            new_direction = "E"
    elif current_direction == "S":
        new_position = [current_position[0]+1, current_position[1]]
        if a_map[new_position[0]][new_position[1]] == "L":
            new_direction = "E"
        elif a_map[new_position[0]][new_position[1]] == "|":
            new_direction = "S"
        elif a_map[new_position[0]][new_position[1]] == "J":
            new_direction = "W"
        elif a_map[new_position[0]][new_position[1]] == "S":
            new_direction = "S"
    elif current_direction == "W":
        new_position = [current_position[0], current_position[1]-1]
        if a_map[new_position[0]][new_position[1]] == "F":
            new_direction = "S"
        elif a_map[new_position[0]][new_position[1]] == "-":
            new_direction = "W"
        elif a_map[new_position[0]][new_position[1]] == "L":
            new_direction = "N"
        elif a_map[new_position[0]][new_position[1]] == "S":
            new_direction = "W"
    return new_position, new_direction


# Used in Day 10
def find_s_position(a_map: list = None):
    for row, map_string in enumerate(a_map):
        if "S" in map_string:
            col = map_string.index("S")
            return [row, col]


# Used in Day 10
def polygon_area(vertices_list: list = None):
    # adapted from geeksforgeeks.org
    x_coords = [coord[0] for coord in vertices_list]
    y_coords = [coord[1] for coord in vertices_list]
    n = len(x_coords)
    # Initialize area
    total_area = 0.0

    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0, n):
        total_area += (x_coords[j] + x_coords[i]) * (y_coords[j] - y_coords[i])
        j = i  # j is previous vertex to i

    # Return absolute value
    return int(abs(total_area / 2.0))
