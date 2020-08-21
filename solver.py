from player import Player
from board import Board
from typing import List, Union, Dict


class Solver(Player):
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
        new_spot = Solver.find_spot(board.board)

        # try numbers
        for i in range(1, 10):
            # get relative key values, values begin a 48 for key value of 0
            key = i + 48
            # check if number is valid
            # variable contains is valid and a player object in a dictionary
            validity = board.is_num_valid(new_spot, key)
            if validity["valid"]:
                # set number if valid
                board.insert_num(validity)
                # attempt to solve, and if solvable return true
                if self.solve(board):
                    return True
                # if not, backtrack and change the past number back to 0
                # keep looping until you find a number that works
                else:
                    # change number back to zero, key of 48 is a zero
                    validity["player"].set_key(48)
                    # take off stack since back track
                    board.insert_num(validity)

        return False
