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


# Used in Day 4, Day 5
def get_numbers_from_string(a_string: str, winning_or_chosen: str = "w"):
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


# Used in Day 5
def map_new_num(previous_num, map_: list = None):
    new_num = None
    for source_to_des in map_:
        des_start = source_to_des[0]
        source_start = source_to_des[1]
        range_len = source_to_des[2]
        if previous_num in range(source_start, source_start + range_len):
            step = previous_num - source_start
            new_num = des_start + step
    if not new_num:
        new_num = previous_num
    return new_num


# Used in Day 5
def get_all_maps(map_: list = None):
    combined_map = []
    current_map = []
    for line in map_:
        if not line:
            if current_map:
                combined_map.append(current_map)
                current_map = []
        elif "map" in line or "seeds" in line:
            pass
        else:
            single_map = get_numbers_from_string(line, "w")
            current_map.append(single_map)
    combined_map.append(current_map)
    return combined_map


# Used in Day 5
def get_seed_pairs_from_seed_ranges(seed_ranges: list = None):
    seed_pairs = []
    pair = []
    for seed_num in seed_ranges:
        if not pair:
            pair.append(seed_num)
        else:
            pair.append(seed_num)
            seed_pairs.append(pair)
            pair = []
    return seed_pairs


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


# Used in Day 11
def add_space_row(space_map_: list = None):
    extra_rows_ = []
    row_length = len(space_map_[0])
    for index_1, row in enumerate(space_map_):
        if row[0] == "." and len(set(row)) == 1:
            extra_rows_.append(index_1)
    # print(extra_rows)
    for index_2, line in enumerate(extra_rows_):
        space_map_.insert(index_2 + line, ["."] * row_length)
    return space_map_


# Used in Day 11
def add_space_col(space_map_: list = None):
    extra_cols_ = [index for index in range(len(space_map_[0]))]
    # print(extra_cols)
    # col_length = len(space_map_)
    for row in space_map_:
        for index_3, col in enumerate(row):
            if col == "#" and index_3 in extra_cols_:
                extra_cols_.remove(index_3)
    # print(extra_cols)
    for row in space_map_:
        for index_4, col_ in enumerate(extra_cols_):
            row.insert(index_4+col_, ".")
    return space_map_


# Used in Day 11
def get_galaxy_coords(space_map_: list = None):
    galaxy_coords_ = []
    for row_index, row in enumerate(space_map_):
        for col_index, col in enumerate(row):
            if col == "#":
                galaxy_coords_.append([row_index, col_index])
    return galaxy_coords_


# Used in Day 11
def distance_between_galaxies(galaxy_1_: list = None, galaxy_2_: list = None):
    dist = abs(galaxy_1_[0] - galaxy_2_[0]) + abs(galaxy_1_[1] - galaxy_2_[1])
    return dist


# Used in Day 11
def get_extra_rows(space_map_: list = None):
    extra_rows_ = []
    # row_length = len(space_map_[0])
    for index_1, row in enumerate(space_map_):
        if row[0] == "." and len(set(row)) == 1:
            extra_rows_.append(index_1)
    return extra_rows_


# Used in Day 11
def get_extra_cols(space_map_: list = None):
    extra_cols_ = [index for index in range(len(space_map_[0]))]
    # print(extra_cols)
    # col_length = len(space_map_)
    for row in space_map_:
        for index_3, col in enumerate(row):
            if col == "#" and index_3 in extra_cols_:
                extra_cols_.remove(index_3)
    return extra_cols_


# Used in Day 11
def distance_between_bigger_galaxies(galaxy_1_: list = None,
                                     galaxy_2_: list = None,
                                     extra_rows_: list = None,
                                     extra_cols_: list = None,
                                     larger_space: int = 2):
    extra_row_space = 0
    for val in extra_rows_:
        if galaxy_1_[0] < val < galaxy_2_[0] or galaxy_2_[0] < val < galaxy_1_[0]:
            extra_row_space += larger_space - 1

    extra_col_space = 0
    for val in extra_cols_:
        if galaxy_1_[1] < val < galaxy_2_[1] or galaxy_2_[1] < val < galaxy_1_[1]:
            extra_col_space += larger_space - 1

    dist = (abs(galaxy_1_[0] - galaxy_2_[0]) +
            abs(galaxy_1_[1] - galaxy_2_[1]) +
            extra_row_space +
            extra_col_space)
    return dist


# Hold for Day 12 functions


# Used in Day 13
def find_mirrors_in_row(valley_map: list = None):
    mirror_row = 0
    valley_rows = len(valley_map)
    for index, row in enumerate(valley_map):
        if index == 0:
            continue
        pre_index = index - 1
        if row == valley_map[pre_index]:
            rows_to_check = min(index, valley_rows - index)
            rows_worked = [True]
            for i in range(1, rows_to_check):
                if valley_map[index + i] == valley_map[pre_index - i]:
                    rows_worked.append(True)
            if sum(rows_worked) == rows_to_check:
                mirror_row = pre_index + 1
                break
    return mirror_row


# Used in Day 13
def find_summary(valley_map: list = None, non_smudged: bool = True):
    summary = 0
    if non_smudged:
        mirror_row = find_mirrors_in_row(valley_map)
    else:
        mirror_row = find_smudge_mirror_row(valley_map)
    if mirror_row:
        summary += mirror_row * 100
    if not mirror_row:
        valley_map_transposed = [list(i) for i in zip(*valley_map)]
        if non_smudged:
            mirror_col = find_mirrors_in_row(valley_map_transposed)
        else:
            mirror_col = find_smudge_mirror_row(valley_map_transposed)
        summary += mirror_col
    return summary


# Used in Day 13
def find_line_differences(line_1, line_2):
    differences = 0
    for list_1_val, list_2_val in zip(line_1, line_2):
        if list_1_val != list_2_val:
            differences += 1
    return differences


# Used in Day 13
def find_smudge_mirror_row(valley_map: list = None):
    mirror_row = 0
    valley_rows = len(valley_map)
    for index, row in enumerate(valley_map):
        if index == 0:
            continue
        pre_index = index - 1
        comparison_1 = find_line_differences(row, valley_map[pre_index])
        if comparison_1 in [0, 1]:
            comparison_diffs = [comparison_1]
            rows_to_check = min(index, valley_rows - index)
            for i in range(1, rows_to_check):
                comparison = find_line_differences(valley_map[index + i], valley_map[pre_index - i])
                comparison_diffs.append(comparison)
            if sum(comparison_diffs) == 1:
                mirror_row = pre_index + 1
                break
    return mirror_row
