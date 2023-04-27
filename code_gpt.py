import machine
import time

# Define pin assignments
S0_PIN = 25
S1_PIN = 26
S2_PIN = 32
S3_PIN = 33
OUT_PIN = 4

# Initialize pin objects
s0 = machine.Pin(S0_PIN, machine.Pin.OUT)
s1 = machine.Pin(S1_PIN, machine.Pin.OUT)
s2 = machine.Pin(S2_PIN, machine.Pin.OUT)
s3 = machine.Pin(S3_PIN, machine.Pin.OUT)
out = machine.Pin(OUT_PIN, machine.Pin.IN)

# Set pin initial values
s0.value(0)
s1.value(0)
s2.value(0)
s3.value(0)

# Define color filter and frequency scaling values
FILTER_RED = 0
FILTER_GREEN = 1
FILTER_BLUE = 2
FILTER_CLEAR = 3
FREQ_SCALING_2 = 0
FREQ_SCALING_20 = 1
FREQ_SCALING_100 = 2
FREQ_SCALING_400 = 3

# Function to read frequency from color sensor
def read_frequency(filter_color, freq_scaling):
    # Set color filter
    if filter_color == FILTER_RED:
        s2.value(0)
        s3.value(0)
    elif filter_color == FILTER_BLUE:
        s2.value(1)
        s3.value(0)
    elif filter_color == FILTER_CLEAR:
        s2.value(0)
        s3.value(1)
    else: # Green filter
        s2.value(1)
        s3.value(1)
    
    # Set frequency scaling
    if freq_scaling == FREQ_SCALING_2:
        s0.value(0)
        s1.value(0)
    elif freq_scaling == FREQ_SCALING_20:
        s0.value(1)
        s1.value(0)
    elif freq_scaling == FREQ_SCALING_100:
        s0.value(0)
        s1.value(1)
    else: # 400 scaling
        s0.value(1)
        s1.value(1)
    
    # Read frequency output
    return out.value()

# Example usage
while True:
    red_freq = read_frequency(FILTER_RED, FREQ_SCALING_20)
    print("Red frequency: ", red_freq)
    green_freq = read_frequency(FILTER_GREEN, FREQ_SCALING_20)
    print("Green frequency: ", green_freq)
    blue_freq = read_frequency(FILTER_BLUE, FREQ_SCALING_20)
    print("Blue frequency: ", blue_freq)
    clear_freq = read_frequency(FILTER_CLEAR, FREQ_SCALING_20)
    print("Clear frequency: ", clear_freq)
    time.sleep(1)
