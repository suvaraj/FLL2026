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

#Start at a fast speed
robot.settings(900)

#Move straight
robot.straight(620)

#Move the arm
leftMotor.run_angle(900, -240)

#Move back
robot.straight(-50)

#Turn to the other mission
robot.turn(41)

#Move straight
robot.straight(170)

#Turn the left arm
leftMotor.run_angle(900,300)

#Wait
wait(1000)

#Move the arm down
leftMotor.run_angle(900,-200)

#Move the robot back
robot.straight(-150)

#Move the arm back in
leftMotor.run_angle(900,100)

#Turn the bot
robot.turn(25)

#Move straight
robot.straight(150)

#Move the robot back
robot.straight(-150)

#Turn the bot
robot.turn(100)

#Go forward
robot.straight(80)

#Turn the right arm
rightMotor.run_angle(900,-90)

#Turn the bot
robot.turn(-90)

#Move back
robot.straight(-200)
