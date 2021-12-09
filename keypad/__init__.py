# OctopusLAB (c) 2021
# by Petr Kracik

__version__ = "0.5.0"
__license__ = "MIT"

from keypad.keymaps.matrix4x4 import Keymap4x4


class Keypad():
    def __init__(self, keymap = None):
        self._keymap = keymap if keymap is not None else Keymap4x4()


    def getKey(self):
        key = self.get_key()
        if key:
            print("DEPRECATED: Use get_key instead")

        return key


    def get_key(self):
        raise NotImplementedError()
