def split_to_boards(file_input):
    boards = dict()
    temp_board = list()
    for index in range(len(file_input) + 1):

        temp_board.append([file_input[index - 1], bool()])

        if index % 25 == 0 and index != 0:
            boards[f"{(index) // 25}"] = temp_board
            temp_board = list()
    
    return boards

def check_win(lst):

    dct = dict()
    temp_lst = list()

    for index, number in enumerate(lst):

        temp_lst.append(number)
        
        if (index + 1) % 5 == 0 and index != 0:
            dct[f"{index // 5}"] = temp_lst
            temp_lst = list()

    for i, _ in enumerate(dct):

        if dct[str(i)][0][1] and dct[str(i)][1][1] and dct[str(i)][2][1] and dct[str(i)][3][1] and dct[str(i)][4][1]:
            return True
        
        if dct["0"][i][1] and dct["1"][i][1] and dct["2"][i][1] and dct["3"][i][1] and dct["4"][i][1]:
            return True
    
    return False

def compare(boards, numbers):

    win_sequence = list()
    win_number = list()

    for number in numbers:

        for index, _ in enumerate(boards):

            for pair_number in boards[str(index + 1)]:

                if pair_number[0] == number:
                    pair_number[1] = True

                if check_win(boards[str(index + 1)]) == True:
                    if (index + 1) not in win_sequence:
                        win_sequence.append(index + 1)
                        win_number.append(number)

    return win_sequence[-1], int(win_number[-1])

def get_score(latest_number, number_list, board):

    new_board = list()
    picked_numbers = list()

    for i in range(number_list.index(str(latest_number)) + 1):
        picked_numbers.append(number_list[i])

    for number in board:
        if number[0] not in picked_numbers:
            number[1] = False
            
        number[0] = int(number[0])
        if number[1]:
            number[0] = 0
        
        new_board.append(number[0])

    print(board)

    return sum(new_board) * latest_number

file_location = r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_4\input.txt"

with open(file_location, "r+") as file:
    file_input = file.read().split()

numbers = file_input[0].split(",")
file_input.pop(0)

boards = split_to_boards(file_input)
board, latest_number = compare(boards, numbers)

print(get_score(latest_number, numbers, boards[str(board)]))