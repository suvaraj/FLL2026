
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


sensor = ColorSensor(Port.C)

def detect_color():

    default_color = sensor.color()
    hsv = sensor.hsv()
    s = hsv.s
    v = hsv.v

    # Check BLACK when LEGO returns NONE
    if default_color == Color.NONE:

        if s <= 15 and v >= 10 and v <= 30:

            return "BLACK"

    # Check LIGHT GREY when LEGO returns WHITE
    elif default_color == Color.WHITE:

        if s >= 2 and s <= 15 and v >= 45 and v <= 80:

            return "LIGHT GREY"

    # Keep original LEGO detection
    return default_color


while True:
    print("Detected:", detect_color())
    wait(200)
