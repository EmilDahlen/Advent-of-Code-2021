rows = open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_9\input.txt", "r+").read().split()

risk_sum = int()

for row_index, row in enumerate(rows):
    for number_index, number in enumerate(row):
        value_dict = dict()

        if not row_index == 0: value_dict["up"] = int(rows[row_index - 1][number_index])

        if not row_index == (len(rows) - 1): value_dict["down"] = int(rows[row_index + 1][number_index])

        if not number_index == 0: value_dict["left"] = int(row[number_index - 1])

        if not number_index == (len(row) - 1): value_dict["right"] = int(row[number_index + 1])

        if all(i > int(number) for i in value_dict.values()):
            print(value_dict)
            print(number)
            risk_sum += int(number) + 1

print(risk_sum)