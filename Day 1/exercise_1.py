input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list.append(int(line))

def counter_deep(input_list):
    increased = 0
    decreased = 0

    for i in range(0, len(input_list)):
        if input_list[i] == input_list[(len(input_list)) - 1]:
            break
        if input_list[i] > input_list[i + 1]:
            decreased = decreased + 1
        elif input_list[i] < input_list[i + 1]:
            increased = increased + 1

    result = "Increased: " + str(increased) + " --- " + "Deacresed: " + str(decreased)
    return result

print(counter_deep(input_list))