from . import Keymap


class MPR121Keymap(Keymap):
    def __init__(self):
        super().__init__()

        self.KEYPAD = ['O', '9', '6', '3',
                       '0', '8', '5', '2',
                       'X', '7', '4', '1']

        self.ENTER = 'O'
        self.BACKSPACE = 'X'
