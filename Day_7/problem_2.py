file_input = list(map(lambda s: int(s), open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_7\input.txt", "r+").read().split(",")))
max_num = int(max(file_input)); min_num = int(min(file_input)); best_fuel_cost = float("inf")
for num in range(min_num, max_num):
    fuel_cost = int()
    for i in file_input:
        fuel_cost += ((abs(num - i) * (abs(num - i) - 1)) // 2) + abs(num - i)
    if fuel_cost < best_fuel_cost: best_fuel_cost = fuel_cost
print(best_fuel_cost)