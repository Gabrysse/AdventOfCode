"""
============================
Advent of Code 2024 - Day 07
============================

Link to the problem: https://adventofcode.com/2024/day/7
"""

def preprocess_data(data):
    equations = []
    for line in data:
        eq = line.replace(":", "").split()
        equations.append(list(map(int, eq)))
    return equations

def do_test(res, partial_res, operands, concat):
    if len(operands) == 0:
        return res == partial_res
    if partial_res > res:
        return False

    count = 0
    count += do_test(res, partial_res + operands[0], operands[1:], concat)
    count += do_test(res, partial_res * operands[0], operands[1:], concat)
    if concat:
        count += do_test(res, int(str(partial_res) + str(operands[0])), operands[1:], concat)

    return count


with open("Day07/07.txt") as f:
    data = f.read().splitlines()

equations = preprocess_data(data)

sum = 0
for eq in equations:
    test_val = eq[0]
    first_operand, other_operands = eq[1], eq[2:]
    possible_sol = do_test(test_val, first_operand, other_operands, concat=False)

    if possible_sol > 0:
        sum += test_val

print(f"Calibration result [sum, mul]: {sum}")

sum = 0
for eq in equations:
    test_val = eq[0]
    first_operand, other_operands = eq[1], eq[2:]
    possible_sol = do_test(test_val, first_operand, other_operands, concat=True)

    if possible_sol > 0:
        sum += test_val

print(f"Calibration result [sum, mul, concat]: {sum}")
