input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list = line.split(",")

print(input_list)

def horizontal_pos(input_list, x):
    list_fuel = []
    for i in range(0,len(input_list)):
        list_fuel.append(abs(int(input_list[i]) - x))

    return sum(list_fuel)


def generate_result(input_list):
    result_list = []

    for i in input_list:
        x = horizontal_pos(input_list, int(i))
        result_list.append(x)

    return min(result_list)

print(generate_result(input_list))