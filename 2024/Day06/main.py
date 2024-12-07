"""
============================
Advent of Code 2024 - Day 06
============================

Link to the problem: https://adventofcode.com/2024/day/6
"""
import time


def split_data(data):
    lines = data
    columns = ["".join(line[i] for line in lines) for i in range(len(lines[0]))]
    return lines, columns


def print_map(data):
    print("   0 1 2 3 4 5 6 7 8 9")
    print("-----------------------")
    for i, line in enumerate(data):
        print(f"{i}|", end=" ")
        print(" ".join(line))


def find_guard(data):
    guard_position = ()

    for line in data:
        try:
            guard_pos = line.index("^")
        except ValueError:
            guard_pos = -1

        if guard_pos != -1:
            guard_position = (data.index(line), guard_pos)

    return guard_position


def mark_position(data, guard_position, direction, debug=False):
    obstacle_found = False
    guard_row, guard_col = guard_position

    if direction == "U":
        for i in range(guard_row, -1, -1):
            if data[i][guard_col] in ["#", "O"]:
                if debug:
                    print(f"Found obstacle at ({i}, {guard_col})")
                obstacle_found = True
                break
            data[i][guard_col] = "X"

        if not obstacle_found:
            return data, None, None

        new_guard_position = (i + 1, guard_position[1])
        new_dir = "R"

    elif direction == "R":
        for i in range(guard_col, len(data[0])):
            if data[guard_row][i] in ["#", "O"]:
                if debug:
                    print(f"Found obstacle at ({guard_row}, {i})")
                obstacle_found = True
                break
            data[guard_row][i] = "X"

        if not obstacle_found:
            return data, None, None

        new_guard_position = (guard_position[0], i - 1)
        new_dir = "D"

    elif direction == "D":
        for i in range(guard_row, len(data)):
            if data[i][guard_col] in ["#", "O"]:
                if debug:
                    print(f"Found obstacle at ({i}, {guard_col})")
                obstacle_found = True
                break
            data[i][guard_col] = "X"

        if not obstacle_found:
            return data, None, None

        new_guard_position = (i - 1, guard_position[1])
        new_dir = "L"

    elif direction == "L":
        for i in range(guard_col, -1, -1):
            if data[guard_row][i] in ["#", "O"]:
                if debug:
                    print(f"Found obstacle at ({guard_row}, {i})")
                obstacle_found = True
                break
            data[guard_row][i] = "X"

        if not obstacle_found:
            return data, None, None

        new_guard_position = (guard_position[0], i + 1)
        new_dir = "U"

    if debug:
        print_map(data)
        print(f"New guard position: {new_guard_position}")
        print(f"New direction: {new_dir}")

    return data, new_guard_position, new_dir


debug = False
with open("06.txt") as f:
    file_data = f.read().splitlines()

data = [list(line) for line in file_data]
guard_position = find_guard(data)

if debug:
    print_map(data)
    print(guard_position)

data, new_guard_position, new_dir = mark_position(data, guard_position, "U", debug)
while new_guard_position is not None:
    data, new_guard_position, new_dir = mark_position(
        data, new_guard_position, new_dir, debug
    )
    if new_guard_position is not None and new_guard_position == guard_position:
        print("Loop detected")
        break

    if debug:
        print("=====================================")

if debug:
    print("FINAL MAP\n")
    print_map(data)
    print()
x_count = sum(line.count("X") for line in data)
print(f"Number of 'X' in the map: {x_count}")

loop_count = 0
original_data = [list(line) for line in file_data]
dot_positions = [
    (i, j)
    for i, line in enumerate(original_data)
    for j, char in enumerate(line)
    if char == "."
]
start_time = time.time()

for dot in dot_positions:
    test_data = [list(line) for line in file_data]
    test_data[dot[0]][dot[1]] = "O"
    if debug:
        print_map(test_data)

    guard_history = {guard_position: 1}
    loop = False
    test_data, new_guard_position, new_dir = mark_position(
        test_data, guard_position, "U", False
    )
    if new_guard_position not in guard_history:
        guard_history[new_guard_position] = 1
    else:
        guard_history[new_guard_position] += 1
    while new_guard_position is not None:
        test_data, new_guard_position, new_dir = mark_position(
            test_data, new_guard_position, new_dir, False
        )
        if new_guard_position not in guard_history:
            guard_history[new_guard_position] = 1
        else:
            guard_history[new_guard_position] += 1
            if guard_history[new_guard_position] > 2:
                loop = True

        if loop:
            loop_count += 1
            break

end_time = time.time()
execution_time_part2 = end_time - start_time

print(f"Number of loops: {loop_count}")
print(f"Execution time (part 2): {execution_time_part2:.2f} seconds")
