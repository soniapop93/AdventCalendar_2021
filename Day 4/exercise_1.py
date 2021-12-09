input_list = []
bingo_list = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

with open("input.txt", "r+") as f:
    for line in f:
        new_line = []
        line = line.replace("\n", "")
        x = line.split(" ")
        for i in x:
            if "" != i:
                new_line.append(i)
        input_list.append(new_line)


print(input_list)

def iterate_matrix(input_list, bingo_list):
