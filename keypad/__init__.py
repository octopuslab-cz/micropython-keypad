# OctopusLAB (c) 2021
# by Petr Kracik

__version__ = "0.3.1"
__license__ = "MIT"


class Keypad():
    def __init__(self, keypad = None, pins=None):
        self._KEYPAD = keypad if keypad is not None else [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]

        self._ROW=pins[0] if pins is not None else [0,1,2,3]
        self._COLUMN=pins[1] if pins is not None else [4,5,6,7]


    def getKey(self):
        raise NotImplementedError()
