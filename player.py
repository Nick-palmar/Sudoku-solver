from typing import List, Dict
from board import Board
import arcade

class Player:
    def __init__(self):
        self.num = None
        self.location = None

    def select_box(self, width: int, height: int, click_x, click_y, screen_height) -> List[int]:
        """Visually selects a box that the player clicks on

        :param width: Width of box
        :param height: Height of box
        :param board: Sudoku board
        :param click_x: X position of click
        :param click_y: Y position of click
        :param screen_height: self.height of screen
        :return: List of coordinate positions for numbers to be placed
        """
        box_x = click_x//width
        box_y = (screen_height-click_y)//height
        self.location = {"row": box_y, "column": box_x}
        return [box_x*width + width//2, screen_height - (box_y*height + height//2)]

    def set_key(self, key: str) -> None:
        """Sets the selected key

         :param key: Key selected
         """
        key_dict = {48: 0,
                    49: 1,
                    50: 2,
                    51: 3,
                    52: 4,
                    53: 5,
                    54: 6,
                    55: 7,
                    56: 8,
                    57: 9}
        if 48 <= key <= 57:
            real_key = key_dict[key]
            self.num = real_key
        else:
            print("invalid key")
