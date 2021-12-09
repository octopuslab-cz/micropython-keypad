from time import ticks_ms
from keypad.i2ckeypad import I2CKeypad
from machine import Pin, I2C


I2C_SDA = 22
I2C_SCL = 21

KP_ADDRESS = 0x25
KP_INTERRUPT = 39

i2c = I2C(0, scl=Pin(I2C_SDA), sda=Pin(I2C_SCL), freq=400000)
kp = I2CKeypad(i2c, KP_ADDRESS, 16)

displayNum = ""
while True:
    try:
        value = kp.input("Enter value: ")
    except OSError as e:
        print("Error while get key")
        print(e)

    print(value)
