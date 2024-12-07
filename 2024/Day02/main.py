"""
============================
Advent of Code 2024 - Day 02
============================

Link to the problem: https://adventofcode.com/2024/day/2
"""

def check_safety(list):
    increasing = False
    decreasing = False
    if list[0] < list[1]:
        increasing = True
    elif list[0] > list[1]:
        decreasing = True
    else:  # Case 3: two adjacent numbers are the same
        return False

    safe = True
    for i in range(len(list)):
        if i != len(list) - 1:
            if list[i] == list[i+1]:  # Case 3: two adjacent numbers are the same
                safe = False
                break
            elif decreasing and list[i] < list[i+1]: # Case 1: decreasing original but now increasing
                safe = False
                break
            elif increasing and list[i] > list[i+1]: # Case 2: increasing original but now decreasing
                safe = False
                break
            else:
                if abs(list[i] - list[i+1]) > 3:
                    safe = False
        
    return safe

def try_remove_one(list, index):
    new_list = list.copy()
    new_list.pop(index)
    return new_list

with open('02.txt') as f:
    data = f.read().splitlines()

safe_reports = 0
for line in data:
    report = [int(elem) for elem in line.split()]

    report_status = check_safety(report)
    if report_status:
        safe_reports += 1
    else:
        for i in range(len(report)):
            reduced_report = try_remove_one(report, i)
            report_status = check_safety(reduced_report)

            if report_status:
                safe_reports += 1
                break

print(f"Safe reports: {safe_reports}")