from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#Define the wheel motors
leftWheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightWheel = Motor(Port.F, Direction.CLOCKWISE)

#Define the attachment motors
rightMotor = Motor(Port.E)
leftMotor = Motor(Port.A)

#Define the robot drivebase
robot = DriveBase(leftWheel, rightWheel, 56, 114)

#Turn on gyro
robot.use_gyro(True)

#Start at a high speed
robot.settings(900)

#Move the robot forward
robot.straight(620)

#Move the arm a litle
leftMotor.run_angle(900, 500)

#Turn the robot
robot.turn(40)

#Move the robot straight
robot.straight(100)

#Move the left arm back
leftMotor.run_angle(800, -500)

#Move the robot back
robot.straight(-100)

#Turn the robot
robot.turn(60)

#Move the robot straight
robot.straight(200)