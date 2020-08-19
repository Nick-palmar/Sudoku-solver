from typing import List, Union, Dict

game_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def print_board(board: List[List[int]]) -> None:
    """Outputs the game board to the console

    :param board: The current sudoku game board
    """
    for i in range(len(board)):
        print()
        if i % 3 == 0 and i != 0:
            print("-"*20)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                if j == 8:
                    print(board[i][j])
                else:
                    print("|" + str(board[i][j]), end=" ")
            else:
                print(str(board[i][j]), end=" ")


def find_spot(board: List[List[int]]) -> Union[Dict, bool]:
    """Finds an empty spot in the game board

    :param board: The current sudoku game board
    :return: A dictionary corresponding to the column and row of the empty spot. If no spots, returns false
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return {"row": i, "column": j}
    return False


def is_num_valid(board: List[List[int]], location: Dict, num: int) -> bool:
    """Determines if a current number in a spot on the baord is valid

    :param board: The current sudoku game board
    :param location: A dictionary corresponding to current [row, column] on the game board
    :param num: The current number inserted into a spot
    :return: True if the spot is valid according to game definitions, otherwise false
    """
    # check if the current row allows it
    for i in range(len(board[0])):
        if board[location["row"]][i] == num and i != location["column"]:
            return False

    # check if the current column allows it
    for j in range(len(board)):
        if board[j][location["column"]] == num and j != location["row"]:
            return False
    # check if the container allows it (not allowed to be in the same 3x3 container)
    # first find what container we are in
    row_container = location["row"] // 3
    column_container = location["column"] // 3

    # find boundary of container or first number in said container
    row_boundary = row_container * 3
    column_boundary = column_container * 3

    current_row = row_boundary
    current_column = column_boundary

    while current_row < row_boundary+3:
        while current_column < column_boundary+3:
            if board[current_row][current_column] == num and (current_row != location["row"] and current_column != location["column"]):
                return False
            current_column += 1
        current_row += 1
        current_column = column_boundary

    # passes all checks, then valid
    return True


def solve(board: List[List[int]]) -> bool:
    """Solves the board using a recursive checks

    :param board: The current sudoku game board
    :return: True is current board is complete, flase if not
    """
    # base case for recursive step
    if not find_spot(board):
        return True

    # if there is a spot, find it
    new_spot: Dict = find_spot(board)

    # try numbers
    for i in range(1, 10):
        # check if number is valid
        if is_num_valid(board, new_spot, i):
            # set number if valid
            board[new_spot["row"]][new_spot["column"]] = i
            # attempt to solve, and if solvable return true
            if solve(board):
                return True
            # if not, backtrack and change the past number back to 0, keep looping until you find a number that works
            else:
                board[new_spot["row"]][new_spot["column"]] = 0

    # board cannot be solved
    return False


print_board(game_board)
# print(find_spot(game_board))
# for i in range(1, 10):
#     print(i, end=" ")
#     print(is_num_valid(game_board, {"row": 1, "column": 7}, i))
#
# print(is_num_valid(game_board, {"row": 0, "column": 2}, 5))

print("solving")

solve(game_board)
print_board(game_board)