from util.readfile import read_file

left_list = []
right_list = []

with read_file("input.txt") as file:
    for line in file:
        words = line.split()
        left_list.append(int(words[0]))
        right_list.append(int(words[1]))

left_list.sort()
right_list.sort()

distances = []
for index, num in enumerate(left_list):
    distances.append(abs(num - right_list[index]))

print(sum(distances))