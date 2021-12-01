file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\advent of code\day 1\view-source_https___adventofcode.com_2021_day_1_input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split("\n")
del file_input[-1]

num_of_increase = int()
for i, string in enumerate(file_input):
    file_input[i]  = int(string)



for i, number in enumerate(file_input):

    if i == len(file_input) - 3:
        break

    number_sum1 = sum(file_input[i:i+3])
    number_sum2 = sum(file_input[i+1:i+4])

    if number_sum1 < number_sum2:
        num_of_increase += 1

print(num_of_increase)