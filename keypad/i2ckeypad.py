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


    def _pin_value(self, pin_num, port_value):
        mask = 0x1 << pin_num
        pin_val = port_value & mask
        return 1 if pin_val == mask else 0


    def get_key(self):
        tmp = bytearray(self._bussize // 8)

        port_value = self._read_port()
        port_value |= self._ROW_BITS
        port_value &= ~self._COLUMN_BITS

        tmp[0] = port_value
        if self._bussize > 8:
            tmp[1] = port_value >> 8

        self._i2c.writeto(self._address, tmp)
        port_value = self._read_port()

        rowVal = -1
        for i in range(len(self._keymap.ROW)):
            if self._pin_value(self._keymap.ROW[i], port_value) == 0:
                rowVal = i
                break
        else:
            return None

        port_value |= self._COLUMN_BITS
        port_value &= ~self._ROW_BITS

        tmp[0] = port_value
        if self._bussize > 8:
            tmp[1] = port_value >> 8

        self._i2c.writeto(self._address, tmp)
        port_value = self._read_port()

        colVal = -1
        for j in range(len(self._keymap.COLUMN)):
            if self._pin_value(self._keymap.COLUMN[j], port_value) == 0:
                colVal=j
                break
        else:
            return None

        # Return the value of the key pressed
        return self._keymap.KEYPAD[rowVal][colVal]
