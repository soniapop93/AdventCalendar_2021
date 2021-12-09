input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list.append(line)
    f.close()


def reverse_matrix(input_list):
    rows = len(input_list)
    columns = len(input_list[0])

    new_list = []
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(input_list[j][i])
        new_list.append(row)

    return new_list


def generate_gamma_binary(new_list):
    new_number = []

    for i in new_list:
        count_0 = i.count('0')
        count_1 = i.count('1')
        if count_0 > count_1:
            new_number.append("0")
        elif count_0 < count_1:
            new_number.append("1")

    return new_number

def generate_epsilon_binary(new_list):
    new_number = []

    for i in new_list:
        count_0 = i.count('0')
        count_1 = i.count('1')
        if count_0 > count_1:
            new_number.append("1")
        elif count_0 < count_1:
            new_number.append("0")

    return new_number


def generate_power_consumption(new_gamma, new_epsilon):
    str_gamma = ""
    str_epsilon = ""

    for i in new_gamma:
        str_gamma = str_gamma + i

    for i in new_epsilon:
        str_epsilon = str_epsilon + i

    gamma = int(str_gamma,2)
    epsilon = int(str_epsilon,2)

    result = gamma * epsilon

    return result




new_list = reverse_matrix(input_list)
new_gamma = generate_gamma_binary(new_list)
new_epsilon = generate_epsilon_binary(new_list)
print(generate_power_consumption(new_gamma, new_epsilon))



