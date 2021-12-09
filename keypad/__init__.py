# OctopusLAB (c) 2021
# by Petr Kracik

__version__ = "0.6.0"
__license__ = "MIT"

from keypad.keymaps.matrix4x4 import Keymap4x4
from time import ticks_ms


class Keypad():
    def __init__(self, keymap = None):
        self._keymap = keymap if keymap is not None else Keymap4x4()
        self._repeat_speed = 250
        self._last_key_press = 0
        self._on_keypress_events = []


    def _on_keypress(self, key):
        for f in self._on_keypress_events:
            f(key)


    def event_keypress_add(self, function):
        self._on_keypress_events.append(function)


    def event_keypress_remove(self, function):
        if function in self._on_keypress_events:
            self._on_keypress_events.remove(function)


    def getKey(self):
        key = self.get_key()
        if key:
            print("DEPRECATED: Use get_key instead")

        return key


    def get_key(self):
        raise NotImplementedError()


    def read(self):
        while True:
            if ticks_ms() < self._last_key_press+self._repeat_speed:
                continue

            char = self.get_key()
            if not char:
                continue

            self._last_key_press = ticks_ms()
            self._on_keypress(char)
            return char


    def input(self, text=None):
        if self._keymap.ENTER is None:
            raise Exception("This keyboard does not have ENTER key, can not use input")

        if text:
            print(text, end='')

        value = ""
        while True:
            char = self.read()

            if char == self._keymap.BACKSPACE:
                if len(value) > 0:
                    value = value[:-1]
                    print('\b \b', end='')

                continue

            if char == self._keymap.ENTER:
                print()
                return value

            value += char
            print(char, end='')
