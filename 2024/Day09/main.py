"""
============================
Advent of Code 2024 - Day 09
============================

Link to the problem: https://adventofcode.com/2024/day/9
"""

import time


def generate_disk_string(data, file_block=False):
    file_index = 0
    out = []
    for i, digits in enumerate(data):
        if i % 2 == 0:
            if file_block:
                if int(digits) > 0:
                    string = [int(file_index)] * int(digits)
                    out.append(string)
            else:
                out.extend([int(file_index) for _ in range(int(digits))])
            file_index += 1
        else:
            out.extend(["." for _ in range(int(digits))])
    return out, file_index


def defragment_simple(disk):
    tail = len(disk) - 1
    for i in range(len(disk)):
        if i >= tail:
            break

        if disk[i] != ".":
            continue

        while disk[tail] == ".":
            tail -= 1

        disk[i] = disk[tail]
        disk[tail] = "."
        tail -= 1

    return disk


def defragment_blocks(disk):
    disk_reversed = disk[::-1]

    for file_block in disk_reversed:
        if file_block == ".":
            continue

        file_block_index = disk.index(file_block)

        for i in range(0, file_block_index):
            if disk[i] != ".":
                continue
            if disk[i : i + len(file_block)] == ["."] * len(file_block):
                disk[file_block_index] = ["."] * len(file_block)

                disk[i] = file_block
                disk[i + 1 : i + len(file_block)] = ["#"] * (len(file_block) - 1)
                break

    new_disk = [x for x in disk if x != "#"]
    return new_disk


def compute_checksum(disk):
    checksum = 0
    for i, file in enumerate(disk):
        if not isinstance(file, str):
            checksum += i * int(file)
    return checksum


with open("2024/Day09/09.txt") as f:
    data = f.read()

# ############ PART1 ############
start = time.time()
disk_string, max_file_index = generate_disk_string(data)
defragmented_disk = defragment_simple(disk_string)
checksum = compute_checksum(defragmented_disk)
print(f"Checksum (part 1) [{time.time() - start:.3f}s]: {checksum} \n")

# ############ PART2 ############
start = time.time()
disk_string, max_file_index = generate_disk_string(data, file_block=True)
defragmented_disk = defragment_blocks(disk_string)
flattened = [
    item
    for sublist in defragmented_disk
    for item in (sublist if isinstance(sublist, list) else [sublist])
]
checksum = compute_checksum(flattened)
print(f"Checksum (part 2) [{time.time() - start:.3f}s]: {checksum}")
