# OctopusLAB (c) 2021
# by Petr Kracik

from . import Keypad

__version__ = "0.3.1"
__license__ = "MIT"


class I2CKeypad(Keypad):
    def __init__(self, i2c, address=0x21, bussize = 8, keymap = None):
        self._i2c = i2c
        self._address = address
        self._bussize = bussize
        super().__init__(keymap)


    def pin_read(self, pinNum):
        mask = 0x1 << pinNum

        value = self._i2c.readfrom(self._address, self._bussize // 8)
        pinVal = value[0]

        if self._bussize > 8:
            pinVal += value[1] << 8

        pinVal &= mask
        if (pinVal == mask):
            return 1
        else:
            return 0


    def getKey(self):
        c = 0
        tmp = bytearray(self._bussize // 8)

        for i in self._keymap.ROW:
            c += 1 << i

        tmp[0] = c
        if self._bussize > 8:
            tmp[1] = c >> 8

        self._i2c.writeto(self._address, tmp)

        rowVal = -1
        for i in range(len(self._keymap.ROW)):
            tmpRead = self.pin_read(self._keymap.ROW[i])
            if tmpRead == 0:
                rowVal = i

        if rowVal < 0 or rowVal > len(self._keymap.ROW) - 1:
            return None

        c = 0
        for i in self._keymap.COLUMN:
            c += 1 << i

        tmp[0] = c
        if self._bussize > 8:
            tmp[1] = c >> 8

        self._i2c.writeto(self._address, tmp)

        colVal = -1
        for j in range(len(self._keymap.COLUMN)):
            tmpRead = self.pin_read(self._keymap.COLUMN[j])
            if tmpRead == 0:
                colVal=j

        if colVal < 0 or colVal > len(self._keymap.COLUMN) - 1:
            return None

        # Return the value of the key pressed
        return self._keymap.KEYPAD[rowVal][colVal]
