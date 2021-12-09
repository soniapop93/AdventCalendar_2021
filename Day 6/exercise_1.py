input_list = [3,4,3,1,2]


def generate_fish(days, input_list):
    list_res = []
    new_fish_list = []

    for i in input_list:
        nr = i
        for day in range(1, days):

            nr = nr - 1
            if nr < 0:
                nr = nr + 7
                print("After " + str(day) + " days: " + str(nr))
                list_res.append(nr)
                new_fish_list.append(8)

            elif nr >= 0 and nr != 6:
                print("After " + str(day) + " days: " + str(nr))
                list_res.append(nr)

    # for j in list_res:
    #     if j == 6:
    #         list_res.append(8)

    print(new_fish_list)




print(generate_fish(18, input_list))