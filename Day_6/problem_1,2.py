def sim(n, dct):
    for _ in range(n): dct[0], dct[1], dct[2], dct[3], dct[4], dct[5], dct[6], dct[7], dct[8] = dct[1], dct[2], dct[3], dct[4], dct[5], dct[6], dct[7] + dct[0], dct[8], dct[0]
    return sum(dct.values())
with open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_6\input.txt", "r+") as file: file_input = file.read().split(","); dct = dict(); 
for i in range(9): dct[i] = int()
for fish in file_input: dct[int(fish)] += 1
print(f"{sim(80, dct)}\n{sim(256, dct)}")