file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_3\input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split()

def o2(file_input):

    for number_pos, _ in enumerate(file_input[0]):

        ones = int()
        zeros = int()

        keep_list = list()

        for number in file_input:
            
            if int(number[number_pos]) == 1:
                ones += 1
            else:
                zeros += 1

        if ones >= zeros:
            for number in file_input:

                if int(number[number_pos]) == 1:
                    keep_list.append(number)

        else: 
            for number in file_input:

                if int(number[number_pos]) == 0:
                    keep_list.append(number)

        file_input = keep_list

        if len(file_input) == 1: return int(file_input[0], 2)

    return

def co2(file_input):

    for number_pos, _ in enumerate(file_input[0]):

        ones = int()
        zeros = int()

        keep_list = list()

        for number in file_input:
            
            if int(number[number_pos]) == 1:
                ones += 1
            else:
                zeros += 1

        if ones < zeros:
            for number in file_input:

                if int(number[number_pos]) == 1:
                    keep_list.append(number)

        else: 
            for number in file_input:

                if int(number[number_pos]) == 0:
                    keep_list.append(number)

        file_input = keep_list

        if len(file_input) == 1: return int(file_input[0], 2)

    return

print(o2(file_input) * co2(file_input))