from typing import List, Dict


class Player:
    def __init__(self, location, key):
        """Makes a player object

        :param location: Location chosen by the player
        :param key: Key (corresponsing to a number) chosen by the player
        """
        self.set_key(key)
        self.set_location(location)

    def select_box(self, width: int, height: int, click_x, click_y, screen_height) -> List[int]:
        """Visually selects a box that the player clicks on

        :param width: Width of box
        :param height: Height of box
        :param click_x: X position of click
        :param click_y: Y position of click
        :param screen_height: self.height of screen
        :return: List of coordinate positions for numbers to be placed
        """
        box_x = click_x//width
        box_y = (screen_height-click_y)//height
        self.set_location({"row": box_y, "column": box_x})
        return [box_x*width + width//2, screen_height - (box_y*height + height//2)]

    def set_key(self, key: int) -> None:
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
        if key is not None:
            if 48 <= key <= 57:
                real_key = key_dict[key]
                self.num = real_key
            else:
                print("invalid key")
        else:
            self.num = None

    def set_location(self, new_location) -> None:
        """Sets the new location if avaliable

        :param new_location: New location of empty spot or none
        """
        if new_location is not None:
            self.location = new_location
        else:
            self.location = None