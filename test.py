from time import ticks_ms
from keypad.i2ckeypad import I2CKeypad
from machine import Pin, I2C


I2C_SDA = 22
I2C_SCL = 21

KP_ADDRESS = 0x25
KP_INTERRUPT = 39

i2c = I2C(scl=Pin(I2C_SDA), sda=Pin(I2C_SCL), freq=400000)
kp = I2CKeypad(i2c, KP_ADDRESS, 16)

def on_keypress(key):
    print("Pressed {}".format(key))

kp.event_keypress_add(on_keypress)

displayNum = ""
char = None
print("Test read method with callback")
while char != "D":
    try:
        char = kp.read()
    except OSError as e:
        print("Error while get key")
        print(e)

kp.event_keypress_remove(on_keypress)

print("Test input method")
while True:
    try:
        value = kp.input()
    except OSError as e:
        print("Error while get key")
        print(e)

    print(value)
