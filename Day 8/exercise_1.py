input_list = []

with open("input.txt", "r+") as f:
    for line in f:
        splited_line = line.split(" | ")[1].replace("\n","")
        input_list.append(splited_line)

print(input_list)

def generate_output_values(input_list):
    count = 0

    for input in input_list:
        splited_input = input.split(" ")
        for item in splited_input:
            if len(item) in [2, 4, 3, 7]:
                count += 1
    return count

print(generate_output_values(input_list))