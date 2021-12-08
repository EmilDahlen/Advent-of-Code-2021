def check_numbers_of_known(inp):
    number_of_known = int()
    for display in inp:
        _, output = display.split(" | ")
        output = output.split(" ")
        for segment in output:
            if len(segment) < 5 or len(segment) == 7:
                number_of_known += 1
    return number_of_known
file_input = open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_8\input.txt", "r+").read().split("\n")
print(check_numbers_of_known(file_input))