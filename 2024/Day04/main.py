"""
============================
Advent of Code 2024 - Day 04
============================

Link to the problem: https://adventofcode.com/2024/day/4
"""

def find_xmas(m):
    counter = 0
    for l_num, line in enumerate(m):
        for i in range(len(line)):
            if line[i] == "X" or line[i] == "S":
                # Check row
                if line[i : i + 4] in ["XMAS", "SAMX"]:
                    counter += 1

                # Check column
                string_col = "".join([column[i] for column in m[l_num : l_num + 4]])
                if string_col in ["XMAS", "SAMX"]:
                    counter += 1

                # Check diagonals
                if l_num <= len(m) - 4:
                    if i <= len(line) - 4:
                        diag1 = "".join([m[l_num + k][i + k] for k in range(4)])
                        if diag1 in ["XMAS", "SAMX"]:
                            counter += 1
                    if i >= 3:
                        diag2 = "".join([m[l_num + k][i - k] for k in range(4)])
                        if diag2 in ["XMAS", "SAMX"]:
                            counter += 1
    print(f"XMAS word counting: {counter}")

def find_x_mas(m):
    counter = 0
    for l_num, line in enumerate(m):
        for i in range(len(line)):
            if line[i] == "M" or line[i] == "S":
                diag1 = ""
                diag2 = ""
                if l_num <= len(m) - 3:
                    if i <= len(line) - 3:
                        diag1 = "".join([m[l_num + k][i + k] for k in range(3)])
                    if diag1 in ["MAS", "SAM"]:
                        diag2 = "".join([m[l_num + k][i + 2 - k] for k in range(3)])

                        if diag2 in ["MAS", "SAM"]:
                            counter += 1

    print(f"X-MAS word counting: {counter}")


with open("04.txt") as f:
    data = f.read().splitlines()

find_xmas(data)
find_x_mas(data)
