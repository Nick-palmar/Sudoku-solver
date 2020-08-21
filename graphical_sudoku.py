import arcade
from board import Board
from player import Player
from solver import Solver

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Sudoku"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)
        self.board = [[]]
        self.player = None
        self.time = None
        self.box_width = None
        self.box_height = None
        self.margin = None
        self.select_pos = None
        self.writing = None
        self.num = None
        self.solver = None
        self.mark_time = None
        self.solved = False
        self.index = None
        self.output_done = None
        self.lap_time = None
        self.draw_new_frame = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.box_width = 40
        self.box_height = 40
        self.margin = 0
        # Create your sprites and sprite lists here
        self.board = Board([
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ], self.box_width, self.box_height, self.margin)

        self.player = Player(None, None)
        self.time = 0
        self.lap_time = 0
        self.mark_time = 0.1
        self.writing = False
        self.solver = Solver(None, None)
        self.index = 0
        self.output_done = False
        self.draw_new_frame = False

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        # draw the time
        self.draw_time()

        self.select_board()
        # draw the board
        self.board.draw_board(self.height)
        # removed, for player functionality
        # if self.select_pos:
        #     arcade.draw_rectangle_outline(self.select_pos[0], self.select_pos[1],
        #                                   self.box_width, self.box_height, arcade.color.DARK_GREEN, 3)

    def select_board(self) -> None:
        """Selects what board to output
        """
        if not self.solved or self.output_done:
            self.board.drawing_board = self.board.board
        else:
            if self.draw_new_frame:
                # on the last frame, set to constant final frame
                if self.index + 1 == len(self.board.all_boards):
                    self.output_done = True
                    self.board.drawing_board = self.board.board
                else:
                    # not on last frame, draw a new step in the process
                    self.board.drawing_board = self.board.all_boards[self.index]
                    self.index += 1
                self.draw_new_frame = False
            else:
                self.board.drawing_board = self.board.all_boards[self.index]

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.time += delta_time
        self.lap_time += delta_time

        if self.mark_time <= self.time:
            self.draw_new_frame = True
            self.mark_time += 0.1

    # removed, for player functionality
    # def on_key_press(self, key, key_modifiers):
    #     """
    #     Called whenever a key on the keyboard is pressed.
    #     """
    #     if self.select_pos:
    #         self.writing = True
    #         self.player.set_key(key)

    # removed, for player functionality
    # def on_mouse_press(self, x, y, button, key_modifiers):
    #     """
    #     Called when the user presses a mouse button.
    #     """
    #     self.select_pos = self.player.select_box(self.box_width, self.box_height, x, y, self.height)
    #     self.writing = False

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        while not self.solved:
            self.solved = self.solver.solve(self.board)
            print("done solving")

    def draw_time(self):
        minute = round(self.time // 60)
        seconds = round(self.time % 60)

        if seconds < 10:
            arcade.draw_text(str(minute) + ":0" + str(seconds), self.width - self.box_width, self.box_height // 4,
                             arcade.color.BLACK, 15)
        else:
            arcade.draw_text(str(minute) + ":" + str(seconds), self.width - self.box_width, self.box_height // 4,
                             arcade.color.BLACK, 15)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
