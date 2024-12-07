"""
============================
Advent of Code 2024 - Day 01
============================

Link to the problem: https://adventofcode.com/2024/day/1
"""

from collections import Counter

with open('01.txt') as f:
    data = f.read().splitlines()

distance = 0
i = 0
left = []
right = []
for d in data:
    loc_id1, loc_id2 = [id.strip() for id in d.split()]
    left.append(int(loc_id1))
    right.append(int(loc_id2))

left.sort()
right.sort()
for l, r in zip(left, right):
    distance += abs(l - r)

print(f"Distance: {distance}")

right_counter = Counter(right)
sim = 0
for l in left:
    sim += l * right_counter[l]

print(f"Similarity: {sim}")