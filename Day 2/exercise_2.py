input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list.append(line)

print(input_list)

def count_depth(input_list):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for i in input_list:
        if "forward" in i:
            nr = i.split(" ")[1]
            horizontal_pos = horizontal_pos + int(nr)
            depth = depth + (aim * int(nr))
        elif "down" in i:
            nr = i.split(" ")[1]
            aim = aim + int(nr)
        elif "up" in i:
            nr = i.split(" ")[1]
            aim = aim - int(nr)

    result = horizontal_pos * depth
    return result

print(count_depth(input_list))