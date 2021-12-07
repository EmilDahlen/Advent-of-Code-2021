class vector:
    def __init__(self, pos1, pos2):
        self.pos0 = pos1
        self.pos1 = pos2
        self.x0 = pos1[0]
        self.y0 = pos1[1]
        self.x1 = pos2[0]
        self.y1 = pos2[1]
        self.is_straight = bool()
        if self.pos0[0] == self.pos1[0] or self.pos0[1] == self.pos1[1]:
            self.is_straight = True
    def passing(self, dictionary):
        x0 = self.x0
        x1 = self.x1
        y0 = self.y0
        y1 = self.y1
        count = int()
        if (x0 + y0) > (x1 + y1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        if x0 == x1:
            for index in range(y1 - y0 + 1):
                if (x0, y0 + index) in dictionary:
                    if dictionary[(x0, y0 + index)] == 2: pass
                    else:
                        dictionary[(x0, y0 + index)] += 1
                        count += 1
                else: dictionary[(x0, y0 + index)] = 1
        if y0 == y1: 
            for index in range(x1 - x0 + 1):
                if (x0 + index, y0) in dictionary:
                    if dictionary[(x0 + index, y0)] == 2: pass
                    else:
                        dictionary[(x0 + index, y0)] += 1
                        count += 1
                else: dictionary[(x0 + index, y0)] = 1
        return count
def split_arrow(string):
    return string.split(" -> ")
def split_comma(string):
    return string.split(",")
def string_to_integer(string):
    return int(string)
def cords_to_vector(lst):
    return vector(list(map(string_to_integer, split_comma(lst[0]))), list(map(string_to_integer, split_comma(lst[1]))))
with open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_5\input.txt", "r+") as file: file_input = file.read().split("\n"); del file_input[-1]; file_input = map(split_arrow, file_input); file_input = map(cords_to_vector, file_input); vectors = list(file_input)
squares = dict()
count =  int()
for v in vectors: count += v.passing(squares)
print(count)