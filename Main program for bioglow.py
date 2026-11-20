from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from big_tree_Triangle import Jungle_Tree_Lift
from Bhagat_Ladybug_Leafcutter_Windowtopast import Bhagat_Ladybug_Leafcutter_Windowtopast
from Advik_Mission import advik
from RomitHumoungusFungus import RomitHumoungusFungus
from RomitOldTreeSeed import RomitOldTreeSeed
from Abhirvey_run import Abhirvey_run
from pybricks.tools import Matrix

hub = PrimeHub()
sensor=ColorSensor(Port.C)


detected_color = sensor.color()
ref = sensor.reflection()
hsv = sensor.hsv()
s = hsv.s
v = hsv.v

print('dedecuted color',detected_color)

print('reflection', ref)
print('hsv', hsv)
print('s', s)
print('v', v)

# Check BLACK when LEGO returns NONE
if detected_color == Color.NONE:

    if s <= 15 and v >= 10 and v <= 30:

        detected_color = Color.BLACK

# Check LIGHT GREY when LEGO returns WHITE
elif detected_color == Color.WHITE:

    if s >= 2 and s <= 15 and v >= 45 and v <= 80:

        #detected_color = Color.GRAY # this should work if needed we can use this.
        detected_color = Color.WHITE



if detected_color == Color.GREEN:#Baghat
    #Runs document
    print("Green")
    Bhagat_Ladybug_Leafcutter_Windowtopast()

if detected_color == Color.RED:#Advik
    #Runs document
    advik()
    print("Red")

if detected_color == Color.BLUE:#Aegen
    #Runs document
    print("Blue")
    Jungle_Tree_Lift()


if detected_color == Color.BLACK:#Romit R1
    #Runs document
    print("Black")
    RomitHumoungusFungus()

if detected_color == Color.WHITE:#Romit R2
    #Runs document
    print("White")
    RomitOldTreeSeed()

if detected_color == Color.YELLOW:#Abhirvey R1
    #Runs document
    print("Yellow")
    Abhirvey_run()


if detected_color == Color.NONE:#Name
        while True:
            print('Inside No color',detected_color)
            smiley = Matrix([
                [0, 100, 0, 100, 0],
                [0, 100, 0, 100, 0],
                [0, 100, 0, 0, 0],
                [100, 0, 100, 0, 100],
                [0, 100, 100, 100, 0],
            ])
            hub.display.icon(smiley)
            #hub.display.pixel(2, 4, 50)
            wait(2000)
