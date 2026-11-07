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

#Move the arm down
leftMotor.run_angle(900,-100)

#Start at a fast speed
robot.settings(900)

#Move the robot forward
robot.straight(260)

#Move the arm up
rightMotor.run_angle(500,140)

#Move the other arm up
leftMotor.run_angle(200,140)

#Move the arm down
leftMotor.run_angle(900,-140)

#Change the speed to slower
robot.settings(70)

#Move the robot back
robot.straight(-110)

#Move the arm down
rightMotor.run_angle(100,-120)

#Change the speed to faster
robot.settings(900)

#Move the robot back
robot.straight(-140)

#Turn left to fit in the home
robot.turn(-90)

#Move the robot back
robot.straight(-90)