import arcade
import copy

# from player import Player

class Board:
    def __init__(self, game_board, width, height, margin):
        """Makes a game board

        :param game_board: The game board from the sudoku game
        :param width: Width of board box
        :param height: Height of board box
        :param margin: Margin of board box
        """
        self.board = game_board
        self.width = width
        self.height = height
        self.margin = margin
        self.original = copy.deepcopy(game_board)

    def is_num_valid(self, player) -> bool:
        """Determines if a current number in a spot on the baord is valid

        :param player: The player who is playing sudoku and is picking the numbers
        :return: True if the spot is valid according to game definitions, otherwise false
        """
        # check if the current row allows it
        for i in range(len(self.board[0])):
            if self.board[player.location["row"]][i] == player.num and i != player.location["column"]:
                return False

        # check if the current column allows it
        for j in range(len(self.board)):
            if self.board[j][player.location["column"]] == player.num and j != player.location["row"]:
                return False
        # check if the container allows it (not allowed to be in the same 3x3 container)
        # first find what container we are in
        row_container = player.location["row"] // 3
        column_container = player.location["column"] // 3

        # find boundary of container or first number in said container
        row_boundary = row_container * 3
        column_boundary = column_container * 3

        current_row = row_boundary
        current_column = column_boundary

        while current_row < row_boundary + 3:
            while current_column < column_boundary + 3:
                if self.board[current_row][current_column] == player.num and (
                        current_row != player.location["row"] and current_column != player.location["column"]):
                    return False
                current_column += 1
            current_row += 1
            current_column = column_boundary

        # passes all checks, then valid
        return True

    def draw_board(self, screen_height) -> None:
        """Draws the game board

        :param screen_height: self.height of screen
        """
        text_adjust = {"x": self.width//8, "y": self.height//3}
        drawn_vertical = [False]*2
        drawn_horizontal = [False]*2
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                # figure out box position
                box_x = (self.margin + self.width) * j + self.margin + self.width//2
                box_y = screen_height - ((self.margin + self.height) * i + self.margin + self.height // 2)

                # check to see if vertical line must be drawn
                if j % 3 == 0 and j != 8 and j != 0 and not drawn_vertical[j//3 - 1]:
                    arcade.draw_line((self.margin+self.width)*j + self.margin//2, screen_height - self.margin,
                                     (self.margin+self.width)*j + self.margin//2,
                                     screen_height - (self.margin+self.height)*len(self.board),
                                     arcade.color.BLACK, 4)
                # draw box
                arcade.draw_rectangle_outline(box_x, box_y, self.width, self.height, arcade.color.BLACK)

                # write number if there is one
                if self.board[i][j] != 0:
                    arcade.draw_text(str(self.board[i][j]), box_x - text_adjust["x"],
                                     box_y - text_adjust["y"], arcade.color.BLACK, 20)

            # check to see if horizontal line must be drawn
            if i % 3 == 0 and i != 8 and i != 0 and not drawn_horizontal[i // 3 - 1]:
                arcade.draw_line(self.margin, screen_height - ((self.margin+self.height)*i + self.margin//2),
                                 (self.margin+self.width)*len(self.board[i]),
                                 screen_height - ((self.margin+self.height)*i + self.margin//2),
                                 arcade.color.BLACK, 4)

    def insert_num(self, player) -> None:
        """Inserts a number into the board

        :param player: The person/machine playing the game
        :param screen_height: height of screen
        """
        # pos_x = (visual_x - self.width//2) // self.width
        # pos_y = (screen_height - visual_y - self.height//2) // self.height
        if self.is_num_valid(player) and self.board[player.location["row"]][player.location["column"]] == 0:
            self.board[player.location["row"]][player.location["column"]] = player.num
        # selected a 0
        elif player.num == 0 and self.original[player.location["row"]][player.location["column"]] == 0:
            self.board[player.location["row"]][player.location["column"]] = player.num
