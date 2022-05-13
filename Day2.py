import numbers
import re

# Part 1:
print("Day 2 Part 1:\n")
# Loop & REGEX

with open('Day2.txt', 'r') as Day2:
    Day2_Data = Day2.read().splitlines()
Day2.close()

forward = 0
depth = 0

for lines in Day2_Data:
    number = re.findall(r'\d', lines)[-1]
    if 'forward' in lines:
         forward += int(number)
    elif 'up' in lines:
        depth -= int(number)
    else:
        depth += int(number)

print(f"Total Forward: {forward}")
print(f"Total Depth: {depth}")
print("Forward & Depth: ", forward*depth)


# Part 2:
print("\nDay 2 Part 2:\n")

with open('Day2.txt', 'r') as Day2:
    Day2_Data = Day2.read().splitlines()
Day2.close()

forward2 = 0
depth2 = 0
aim = 0

for lines in Day2_Data:
    number = re.findall(r'\d', lines)[-1]
    if 'forward' in lines:
         forward2 += int(number)
         depth2 += int(number) * aim
    elif 'up' in lines:
        aim -= int(number)
    else:
        aim += int(number)

print(f"Total Forward: {forward2}")
print(f"Total Depth: {depth2}")
print(f"Total Aim: {aim}")
print("Forward & Depth: ", forward2*depth2)