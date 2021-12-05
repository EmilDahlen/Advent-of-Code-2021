file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_3\input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split("\n")
del file_input[-1]

def func(file_input):

    gamma = ""
    epsilon = ""

    for number_pos, _ in enumerate(file_input[0]):

        ones = int()
        zeros = int()

        for number in file_input:
            
            if int(number[number_pos]) == 1:
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            gamma += "1"
            epsilon += "0"

        else: 
            gamma += "0"
            epsilon += "1"
        
    return int(gamma, 2) * int(epsilon, 2)


print(func(file_input))