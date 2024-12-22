import re

from util.readfile import read_file

with read_file("input.txt") as file:
    program = file.read()

valid_ops = [(int(x), int(y)) for x, y in re.findall(r"mul\((\d+),(\d+)\)", program)]

total = 0
for ops in valid_ops:
    total += ops[0] * ops[1]

print(total)