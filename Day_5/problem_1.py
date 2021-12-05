class vector:

    def __init__(self, pos1, pos2):
        self.pos0 = pos1
        self.pos1 = pos2
        self.is_straight = bool()
        if self.pos0[0] == self.pos1[0] or self.pos0[1] == self.pos1[1]:
            self.is_straight = True

    def straight_passing(self, dictionary, count):
        print("1")
        if sum(self.pos1) > sum(self.pos0):
                self.pos1, self.pos0 = self.pos0, self.pos1
        if self.pos0[0] == self.pos1[0]:
            for index in range(self.pos0[0] - self.pos1[0]):
                if dictionary[(self.pos0[0] + index, self.pos0[1])] >= 2: count += 1; pass
                dictionary[(self.pos0[0] + index, self.pos0[1])] += 1
        if self.pos0[1] == self.pos1[1]:
            for index in range(self.pos1[1] - self.pos0[1]):
                if dictionary[(self.pos0[0], self.pos0[1] + index)] >= 2: count += 1; pass
                dictionary[(self.pos0[0], self.pos0[1] + index)] += 1

    def show(self):
        print(f"{self.pos0} + {self.pos1}")

def split_arrow(string):
    return string.split(" -> ")

def split_comma(string):
    return string.split(",")

def string_to_integer(string):
    return int(string)

def cords_to_vector(lst):
    return vector(list(map(string_to_integer, split_comma(lst[0]))), list(map(string_to_integer, split_comma(lst[1]))))


file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_5\input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split("\n")
    del file_input[-1]
    file_input = map(split_arrow, file_input)
    file_input = map(cords_to_vector, file_input)
    vectors = list(file_input)

squares = dict()
count =  int()

for vectr in vectors:
    vectr.show()
    if not vectr.is_straight: pass
    vectr.straight_passing(squares, count)
print(count)
