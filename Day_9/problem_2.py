from time import sleep

def map_basin(rows, cords_list, start_cord, max_x, max_y):
    unexplored_cords = [0]
    next_round = list(); next_round.append(start_cord)
    explored_cords = list()
    basin_size = int()

    if next_round[0] in cords_list: return False

    while len(unexplored_cords) != 0:

        unexplored_cords = next_round
        next_round = list()

        #print(f"ue{len(unexplored_cords)}\ne{len(explored_cords)}\n") ################################

        for cord in unexplored_cords:

            cords_list.append(cord)

            explored_cords.append(cord)

            number = int(rows[get_row_index(cord)][get_number_index(cord)])

            if number == 9: pass
            else:

                basin_size += 1
                for checked_cord in check_sides(cord, max_x, max_y, rows):

                    if checked_cord in unexplored_cords or checked_cord in explored_cords or checked_cord in next_round: pass
                    else: 
                        next_round.append(checked_cord)

                #print(f"ue{len(unexplored_cords)}\ne{len(explored_cords)}\n______________") ################################


    return basin_size

def check_sides(cord, max_x, max_y, rows):
    return_list = list()

    if not cord[1] == 0: return_list.append((cord[0], cord[1] - 1))

    if not cord[1] == max_y: return_list.append((cord[0], cord[1] + 1))

    if not cord[0] == 0: return_list.append((cord[0] - 1, cord[1]))

    if not cord[0] == max_x: return_list.append((cord[0] + 1, cord[1]))

    return return_list

def get_cord(row_index, number_index):
    return (int(number_index), int(row_index))

def get_row_index(cord):
    return cord[1]

def get_number_index(cord):
    return cord[0]

rows = open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_9\input.txt", "r+").read().split()

risk_sum = int()
cords_list = list()
max_x = len(rows[0]) - 1
max_y = len(rows) - 1

all_basin_sizes = list()

for row_index, row in enumerate(rows):
    for number_index, number in enumerate(row):

        #print(cords_list)

        basin_size = map_basin(rows, cords_list, get_cord(row_index, number_index), max_x, max_y)

        if not isinstance(basin_size, bool): all_basin_sizes.append(basin_size)

all_basin_sizes.sort()
print(all_basin_sizes[-1] * all_basin_sizes[-2] * all_basin_sizes[-3])
#print(cords_list)
#print(all_basin_sizes)