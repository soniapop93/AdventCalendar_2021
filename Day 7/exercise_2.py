input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list = line.split(",")


def horizontal_pos(input_list, x):
    list_fuel = []
    for i in range(0,len(input_list)):
        range_fuel = abs(int(input_list[i]) - x)
        sum_fuel = sum(range(1,range_fuel+1))
        list_fuel.append(sum_fuel)

    return sum(list_fuel)

def generate_result(input_list):
    result_list = []

    for i in range(1,len(input_list)):
        x = horizontal_pos(input_list, i)

        result_list.append(x)

    return min(result_list)

print(generate_result(input_list))
