"""
============================
Advent of Code 2024 - Day 03
============================

Link to the problem: https://adventofcode.com/2024/day/3
"""

import re

with open('03.txt') as f:
    data = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)

total = 0
for match in matches:
    numbers = match.replace("mul(", "").replace(")", "").split(",")
    total += (int(numbers[0]) * int(numbers[1]))

print(f"Total (part. 1): {total}")


pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, data)

total = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
        continue
    elif match == "don't()":
        enabled = False
        continue

    if enabled:
        numbers = match.replace("mul(", "").replace(")", "").split(",")
        total += (int(numbers[0]) * int(numbers[1]))

print(f"Total (part. 2): {total}")