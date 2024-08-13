# OctopusLAB (c) 2024
# by Petr Kracik

import mpr121
from keypad.keymaps.mpr121keymap import MPR121Keymap
from . import Keypad

__version__ = "0.0.1"
__license__ = "MIT"


class MPR121Keypad(Keypad):
    def __init__(self, i2c, address=0x5A, keymap = None):
        self._keymap = keymap if keymap is not None else MPR121Keymap()
        self._i2c = i2c
        self._address = address
        self._mpr = mpr121.MPR121(i2c, address)

        super().__init__(self._keymap)


    def get_key(self):
        for i in range(12):
            if self._mpr.is_touched(i):
                return self._keymap.KEYPAD[i]
