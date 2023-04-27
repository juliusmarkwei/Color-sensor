import machine
import time

# Set up the GPIO pins for the color sensor
s2_pin = machine.Pin(13, machine.Pin.OUT)
s3_pin = machine.Pin(12, machine.Pin.OUT)
out_pin = machine.Pin(14, machine.Pin.IN)

# Set the frequency scaling for the sensor
s2_pin.off()
s3_pin.off()

# Define the color detection function
def detect_color():
    # Set the color to red
    s2_pin.off()
    s3_pin.off()
    # Read the output voltage
    voltage = out_pin.value()
    print("Red: ", voltage)
    time.sleep(1)

    # Set the color to green
    s2_pin.on()
    s3_pin.on()
    # Read the output voltage
    voltage = out_pin.value()
    print("Green: ", voltage)
    time.sleep(1)

    # Set the color to blue
    s2_pin.off()
    s3_pin.on()
    # Read the output voltage
    voltage = out_pin.value()
    print("Blue: ", voltage)
    time.sleep(1)

# Call the color detection function
while True:
    detect_color()
