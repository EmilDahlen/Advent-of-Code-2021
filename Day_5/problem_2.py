class vector:
    def __init__(self, pos0, pos1):
        self.x0 = pos0[0]
        self.y0 = pos0[1]
        self.x1 = pos1[0]
        self.y1 = pos1[1]
        self.is_straight = bool()
        if self.x0 == self.x1 or self.y0 == self.y1:
            self.is_straight = True
    def passing(self, dictionary):
        x0 = self.x0
        x1 = self.x1
        y0 = self.y0
        y1 = self.y1
        count = int()
        x_step = get_increment(x0, x1)
        y_step = get_increment(y0, y1)
        while True:
            if (x0, y0) in dictionary:
                if dictionary[(x0, y0)] == 2:
                    pass
                else:
                    dictionary[(x0, y0)] += 1
                    count += 1
            else: dictionary[(x0, y0)] = 1
            if x0 == x1 and y0 == y1: break
            x0 += x_step
            y0 += y_step
        return count
def get_increment(integer0, integer1):
    if integer0 < integer1:
        return 1
    if integer0 > integer1:
        return -1
    return 0
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