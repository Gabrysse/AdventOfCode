"""
============================
Advent of Code 2024 - Day 11
============================

Link to the problem: https://adventofcode.com/2024/day/11
"""

import time


def preprocess_data(data):
    output = {}
    for line in data.split():
        value = int(line.strip())
        if value not in output:
            output[value] = 1
        else:
            output[value] += 1
    return output


def blinking(data):
    new_data = {}
    for value, n_elements in data.items():
        if value == 0:
            if 1 not in new_data:
                new_data[1] = 1 * n_elements
            else:
                new_data[1] += 1 * n_elements
        elif len(str(value)) % 2 == 0:
            value = str(value)
            stone1 = value[: len(value) // 2]
            stone2 = value[len(value) // 2 :]
            for stone in [int(stone1), int(stone2)]:
                if stone not in new_data:
                    new_data[stone] = 1 * n_elements
                else:
                    new_data[stone] += 1 * n_elements
        else:
            stone = value * 2024
            if stone not in new_data:
                new_data[stone] = 1 * n_elements
            else:
                new_data[stone] += 1 * n_elements

    return new_data


with open("2024/Day11/11.txt") as f:
    original_data = f.read()

data = preprocess_data(original_data)

# ############ PART1 ############
start = time.time()
blink_numbers = 25
for i in range(blink_numbers):
    data = blinking(data)

stone_lenght = sum(data.values())
print(f"Stone lenght (part 1) [{time.time() - start:.3f}s]: {stone_lenght}")

# ############ PART2 ############
data = preprocess_data(original_data)
start = time.time()
blink_numbers = 75
for i in range(blink_numbers):
    data = blinking(data)

stone_lenght = sum(data.values())
print(f"Stone lenght (part 2) [{time.time() - start:.3f}s]: {stone_lenght}")
