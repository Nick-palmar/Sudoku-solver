import arcade
from board import Board
from player import Player
from solver import Solver
from typing import List

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Sudoku"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None
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

        self.player = Player()
        self.time = 0
        self.writing = False
        self.solver = Solver()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.board.draw_board(self.height)
        # draw the time
        self.draw_time()

        if self.select_pos:
            arcade.draw_rectangle_outline(self.select_pos[0], self.select_pos[1],
                                          self.box_width, self.box_height, arcade.color.DARK_GREEN, 3)

        if self.writing:
            self.board.insert_num(self.player)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.time += delta_time
        self.solver.solve(self.board)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if self.select_pos:
            self.writing = True
            self.player.set_key(key)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.select_pos = self.player.select_box(self.box_width, self.box_height, x, y, self.height)
        self.writing = False

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

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
