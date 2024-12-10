"""
============================
Advent of Code 2024 - Day 10
============================

Link to the problem: https://adventofcode.com/2024/day/10
"""

import time


def preprocess_data(data):
    output = []
    start_positions = []
    end_positions = []
    for i, line in enumerate(data):
        new_line = []
        for j, elem in enumerate(line):
            new_line.append(int(elem))
            if elem == "0":
                start_positions.append((i, j))
            elif elem == "9":
                end_positions.append((i, j))

        output.append(new_line)

    return output, start_positions, end_positions


def check__next_position(map, curr_value, visited, nex_pos, direction):
    if nex_pos in visited:
        return False

    if direction == "U" and nex_pos[0] >= 0:
        next_value = map[nex_pos[0]][nex_pos[1]]
        if next_value == curr_value + 1:
            return True
    elif direction == "D" and nex_pos[0] < len(map):
        next_value = map[nex_pos[0]][nex_pos[1]]
        if next_value == curr_value + 1:
            return True
    elif direction == "L" and nex_pos[1] >= 0:
        next_value = map[nex_pos[0]][nex_pos[1]]
        if next_value == curr_value + 1:
            return True
    elif direction == "R" and nex_pos[1] < len(map[0]):
        next_value = map[nex_pos[0]][nex_pos[1]]
        if next_value == curr_value + 1:
            return True

    return False


def search_path(map, current, visited=[]):
    current_value = map[current[0]][current[1]]
    visited.append(current)

    if current_value == 9:
        return [(current[0], current[1])]

    path = []
    if check__next_position(
        map, current_value, visited, (current[0] - 1, current[1]), "U"
    ):
        p_up = search_path(map, (current[0] - 1, current[1]), visited)
        if find_all_paths:
            visited.pop(-1)

        if p_up:
            path.extend(p_up)
    if check__next_position(
        map, current_value, visited, (current[0] + 1, current[1]), "D"
    ):
        p_down = search_path(map, (current[0] + 1, current[1]), visited)
        if find_all_paths:
            visited.pop(-1)

        if p_down:
            path.extend(p_down)
    if check__next_position(
        map, current_value, visited, (current[0], current[1] - 1), "L"
    ):
        p_left = search_path(map, (current[0], current[1] - 1), visited)
        if find_all_paths:
            visited.pop(-1)

        if p_left:
            path.extend(p_left)
    if check__next_position(
        map, current_value, visited, (current[0], current[1] + 1), "R"
    ):
        p_right = search_path(map, (current[0], current[1] + 1), visited)
        if find_all_paths:
            visited.pop(-1)

        if p_right:
            path.extend(p_right)

    return path


with open("2024/Day10/10.txt") as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

map, start_pos, end_pos = preprocess_data(data)

# ############ PART1 ############
start_time = time.time()
sum = 0
find_all_paths = False
for start in start_pos:
    path = search_path(map, start, [])
    sum += len(path)

print(f"Sum of trailheads' scores (part 1) [{time.time() - start_time:.3f}s]: {sum}")

# ############ PART2 ############
start_time = time.time()
sum = 0
find_all_paths = True
for start in start_pos:
    path = search_path(map, start, [])
    sum += len(path)

print(f"Sum of trailheads' ratings (part 2) [{time.time() - start_time:.3f}s]: {sum}")
