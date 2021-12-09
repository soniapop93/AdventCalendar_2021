input_list = []
co_list = []

with open("input.txt", "r+") as f:
    for line in f:
        line = line.replace("\n", "")
        input_list.append(line)
        co_list.append(line)


def iterate_matrix_oxigen(input_list, column_i):
    row = len(input_list)

    if len(input_list) == 1:
        return input_list

    count_0 = 0
    count_1 = 0
    for row_i in range(0, row):
        if input_list[row_i][column_i] == "0":
            count_0 = count_0 + 1
        elif input_list[row_i][column_i] == "1":
            count_1 = count_1 + 1

    remove_list = []
    for i in input_list:
        if count_0 > count_1:
            if "1" in i[column_i]:
                remove_list.append(i)
        elif count_1 > count_0:
            if "0" in i[column_i]:
                remove_list.append(i)
        elif count_1 == count_0:
            if "0" in i[column_i]:
                remove_list.append(i)

    for r in remove_list:
        input_list.remove(r)

    return iterate_matrix_oxigen(input_list, column_i + 1)


def iterate_matrix_co2(input_list, column_i):
    row = len(input_list)

    if len(input_list) == 1:
        return input_list

    count_0 = 0
    count_1 = 0
    for row_i in range(0, row):
        if input_list[row_i][column_i] == "0":
            count_0 = count_0 + 1
        elif input_list[row_i][column_i] == "1":
            count_1 = count_1 + 1

    remove_list = []
    for i in input_list:
        if count_0 > count_1:
            if "0" in i[column_i]:
                remove_list.append(i)
        elif count_1 > count_0:
            if "1" in i[column_i]:
                remove_list.append(i)
        elif count_1 == count_0:
            if "1" in i[column_i]:
                remove_list.append(i)

    for r in remove_list:
        input_list.remove(r)

    return iterate_matrix_co2(input_list, column_i + 1)


def generate_life_support_rating(oxigen, co2):
    result = int(oxigen[0], 2) * int(co2[0], 2)
    return result


oxigen = iterate_matrix_oxigen(input_list, 0)
co2 = iterate_matrix_co2(co_list, 0)

print(generate_life_support_rating(oxigen, co2))
