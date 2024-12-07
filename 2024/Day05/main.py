"""
============================
Advent of Code 2024 - Day 05
============================

Link to the problem: https://adventofcode.com/2024/day/5
"""


def parse_data(data):
    rule_dict = {}
    print_order = []

    for line in data:
        if line == "":
            continue
        if "|" in line:
            first, second = line.split("|")
            if first in rule_dict:
                rule_dict[first].append(second)
            else:
                rule_dict[first] = [second]

        if "," in line:
            print_order.append(line.split(","))

    return rule_dict, print_order


def validity_check(rule_dict, update):
    for i in range(len(update)):
        if update[i] in rule_dict.keys():
            # check = [next_elem in rule_dict[update[i]] for next_elem in update[i + 1 :]]
            check_prec = [prev_elem in rule_dict[update[i]] for prev_elem in update[:i]]

            if any(check_prec):
                # print(i, update[i], check_prec)

                return False, check_prec, i

    return True, None, None


def fix_sequence(update, index, check):
    new_update = update[: (index - 1)]
    new_update += [update[index], update[len(check) - 1]]
    if len(new_update) != len(update):
        new_update += update[len(check) + 1 :]

    return new_update


with open("05.txt") as f:
    data = f.read().splitlines()

rule_dict, print_order = parse_data(data)

sum = 0
sum_fixed = 0
for i, update in enumerate(print_order):
    valid, check, index = validity_check(rule_dict, update)
    if valid:
        sum += int(update[len(update) // 2])
    else:
        new_update = fix_sequence(update, index, check)
        valid, check, index = validity_check(rule_dict, new_update)
        while not valid:
            new_update = fix_sequence(new_update, index, check)
            valid, check, index = validity_check(rule_dict, new_update)

        sum_fixed += int(new_update[len(new_update) // 2])

print(f"Sum of middle elements: {sum}")
print(f"Sum of middle elements (fixed): {sum_fixed}")
