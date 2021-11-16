# micropython-keypad

Implementation for matrix keyboards and keypads.

For now support 8 and 16bit i2c expanders based on PCF8574 and PCF8575

Contributions are welcome

TODO:
 - Do more generic class
 - Implement optional non-blocking reading (use interrupt if available)
 - Read expander state before write to preserve other pin states
 - Think about solution to support more keypads (5x4, 4x4, 3x4, invert etc...)
 - Implement more interfaces (SPI expander, direct GPIO, more I2C expanders)
