from player import Player
from board import Board
from typing import List, Union, Dict


class Solver(Player):
    def __init__(self):
        # for memory
        self.my_stack = []
    @classmethod
    def find_spot(cls, board: List[List[int]]) -> Union[Dict, bool]:
        """Finds an empty spot in the game board

        :param board: The current sudoku game board
        :return: A dictionary corresponding to the column and row of the empty spot. If no spots, returns false
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return {"row": i, "column": j}
        return False

    def solve(self, board: Board) -> bool:
        """Solves the board using a recursive checks

        :param board: The current sudoku game board
        :return: True is current board is complete, false if not
        """
        # base case for recursive step
        if not Solver.find_spot(board.board):
            return True

        # if there is a spot, find it
        self.location = Solver.find_spot(board.board)
        # remember the location
        self.my_stack.append(self.location)
        # print(self.location)
        # print(self.num)

        # try numbers
        for i in range(1, 10):
            self.set_key(i+48)
            print(self.location)
            print(self.num)
            # check if number is valid
            if board.is_num_valid(self):
                # set number if valid
                board.insert_num(self)
                # attempt to solve, and if solvable return true
                if self.solve(board):
                    return True
                # if not, backtrack and change the past number back to 0, keep looping until you find a number that works
                else:
                    self.num = 0
                    # take off stack since back track
                    self.location = self.my_stack.pop()
                    board.insert_num(self)

        # board cannot be solved
        # first remove last unsolveable element
        # if board.board[self.location["row"]][self.location["column"]] == 0 and len(self.my_stack) > 0:
        #     self.my_stack.pop()
        # else:
        #     self.location = Solver.find_spot(board.board)

        # then get the next element
        if len(self.my_stack) > 0:
            self.location = self.my_stack.pop()
        else:
            self.location = Solver.find_spot(board.board)
        return False
