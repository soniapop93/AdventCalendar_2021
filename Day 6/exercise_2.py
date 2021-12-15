# read_list = []
# input_list = []
#
# with open("input.txt", "r+") as f:
#     for line in f:
#         line = line.replace("\n", "")
#         read_list = line.split(",")
#
# for elem in read_list:
#     input_list.append(int(elem))

input_list = [3,4,3,1,2]

print(input_list)

def generate_fishes(input_list, days):
    for day in range(0, days):
        for count, item in zip(range(0, len(input_list)) , input_list):
            if item == 0:
                input_list[count] = 7
                input_list.append(9)

        for count in range(0, len(input_list)):
            input_list[count] = input_list[count] - 1

    # return len(input_list)
    count = 0
    for x in input_list:
        count = count + 1
    print(count)

print(generate_fishes(input_list,150))