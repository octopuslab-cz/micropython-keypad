# OctopusLAB (c) 2021
# by Petr Kracik

from . import Keypad

__version__ = "0.5.0"
__license__ = "MIT"


class I2CKeypad(Keypad):
    def __init__(self, i2c, address=0x21, bussize = 8, keymap = None):
        self._i2c = i2c
        self._address = address
        self._bussize = bussize

        super().__init__(keymap)

        self._ROW_BITS = 0
        self._COLUMN_BITS = 0

        for i in self._keymap.ROW:
            self._ROW_BITS += 1 << i

        for i in self._keymap.COLUMN:
            self._COLUMN_BITS += 1 << i


    def _read_port(self):
        port_value = self._i2c.readfrom(self._address, self._bussize // 8)
        value = port_value[0]

        if self._bussize > 8:
            value += port_value[1] << 8

        return value


    def _pin_read(self, pinNum):
        mask = 0x1 << pinNum
        pinVal = self._read_port() & mask
        return 1 if pinVal == mask else 0


    def getKey(self):
        c = self._read_port()
        tmp = bytearray(self._bussize // 8)

        c |= self._ROW_BITS
        c &= ~self._COLUMN_BITS

        tmp[0] = c
        if self._bussize > 8:
            tmp[1] = c >> 8

        self._i2c.writeto(self._address, tmp)

        rowVal = -1
        for i in range(len(self._keymap.ROW)):
            tmpRead = self._pin_read(self._keymap.ROW[i])
            if tmpRead == 0:
                rowVal = i

        if rowVal < 0 or rowVal > len(self._keymap.ROW) - 1:
            return None

        c |= self._COLUMN_BITS
        c &= ~self._ROW_BITS

        tmp[0] = c
        if self._bussize > 8:
            tmp[1] = c >> 8

        self._i2c.writeto(self._address, tmp)

        colVal = -1
        for j in range(len(self._keymap.COLUMN)):
            tmpRead = self._pin_read(self._keymap.COLUMN[j])
            if tmpRead == 0:
                colVal=j

        if colVal < 0 or colVal > len(self._keymap.COLUMN) - 1:
            return None

        # Return the value of the key pressed
        return self._keymap.KEYPAD[rowVal][colVal]
