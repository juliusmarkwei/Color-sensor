import machine
import time
import adafruit_tcs34725

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
sensor = adafruit_tcs34725.TCS34725(i2c)

while True:
    r, g, b, _ = sensor.color_rgb_bytes
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    time.sleep(1)
