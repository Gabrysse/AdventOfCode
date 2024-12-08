"""
============================
Advent of Code 2024 - Day 08
============================

Link to the problem: https://adventofcode.com/2024/day/8
"""

from collections import Counter
import itertools


def check_antinode(antinode, n_lines, n_columns):
    return n_lines > antinode[0] >= 0 and n_columns > antinode[1] >= 0


with open("Day08/08.txt") as f:
    data = f.read().splitlines()

data = [list(l) for l in data]
lines = len(data)
columns = len(data[0])

char_pos = {}
for row_index, line in enumerate(data):
    for column_index, char in enumerate(line):
        if char not in [".", "\n"]:
            if char in char_pos:
                char_pos[char].append((row_index, column_index))
            else:
                char_pos[char] = [(row_index, column_index)]
char_pos = {k: v for k, v in char_pos.items() if len(v) >= 2}

total_antinodes_part1 = []
total_antinodes_part2 = []
for char, pos in char_pos.items():
    antenna_pairs = list(itertools.combinations(pos, 2))

    for pair in antenna_pairs:
        total_antinodes_part2.extend(pair)

        x1, y1 = pair[0]
        x2, y2 = pair[1]
        row_diff, col_diff = x2 - x1, y2 - y1

        antinode1 = (x1 - row_diff, y1 - col_diff)
        antinode2 = (x2 + row_diff, y2 + col_diff)

        if check_antinode(antinode1, lines, columns):
            total_antinodes_part1.append(antinode1)
            total_antinodes_part2.append(antinode1)
        if check_antinode(antinode2, lines, columns):
            total_antinodes_part1.append(antinode2)
            total_antinodes_part2.append(antinode2)

        while True:
            output = []
            a1 = (antinode1[0] - row_diff, antinode1[1] - col_diff)
            a2 = (antinode2[0] + row_diff, antinode2[1] + col_diff)

            if check_antinode(a1, lines, columns):
                output.append(a1)
                antinode1 = a1
            if check_antinode(a2, lines, columns):
                output.append(a2)
                antinode2 = a2

            if output == []:
                break

            total_antinodes_part2.extend(output)

total_antinodes_part1 = list(set(total_antinodes_part1))
print(f"Total antinodes (part 1): {len(total_antinodes_part1)}")

total_antinodes_part2 = list(set(total_antinodes_part2))
print(f"Total antinodes (part 2): {len(total_antinodes_part2)}")
