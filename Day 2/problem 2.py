file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day 2\view-source_https___adventofcode.com_2021_day_2_input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split("\n")
del file_input[-1]

def func(file_input):

    forward = int()
    down = int()
    aim = int()

    for movment in file_input:

        if "down" in movment:
            aim += int(movment[-1])

        if "up" in movment:
            aim -= int(movment[-1])

        if "forward" in movment:
            forward += int(movment[-1])
            down += int(movment[-1]) * aim

    return forward * down

print(func(file_input))