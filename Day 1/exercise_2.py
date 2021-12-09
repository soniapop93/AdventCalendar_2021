input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list.append(int(line))

print(len(input_list))

def make_block_sums(input_list):
    list_sum = []
    for i in range(0, len(input_list)):
        if input_list[i] == input_list[(len(input_list)) - 2]:
            break
        sum_i = 0
        sum_i = input_list[i] + input_list[i+1] + input_list[i+2]
        list_sum.append(sum_i)

    return list_sum


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

print(make_block_sums(input_list))

sums_elem = make_block_sums(input_list)
print(counter_deep(sums_elem))