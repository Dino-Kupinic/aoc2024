import re

from util.readfile import read_file

with read_file("input.txt") as file:
    program = file.read()


def p1():
    valid_ops = [(int(x), int(y)) for x, y in re.findall(r"mul\((\d+),(\d+)\)", program)]

    total = 0
    for ops in valid_ops:
        total += ops[0] * ops[1]

    print(total)


def p2():
    instructions = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", program)

    mul_enabled = True
    total = 0
    for instruction in instructions:
        if "mul" in instruction[0]:
            if mul_enabled:
                x, y = int(instruction[1]), int(instruction[2])
                total += x * y
        elif "do()" in instruction[0]:
            mul_enabled = True
        elif "don't()" in instruction[0]:
            mul_enabled = False

    print(total)


p1()
p2()
