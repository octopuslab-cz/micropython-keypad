from . import Keymap


class Keymap4x4(Keymap):
    def __init__(self):
        super().__init__()

        self.KEYPAD = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]

        self.ROW = [0,1,2,3]
        self.COLUMN = [4,5,6,7]

        self.ENTER = 'D'
        self.BACKSPACE = 'B'


class Keymap4x4Inv(Keymap4x4):
    def __init__(self):
        super().__init__()
        self.ROW = [7,6,5,4]
        self.COLUMN = [3,2,1,0]
