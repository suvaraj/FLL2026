from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from pybricks.hubs import PrimeHub  # Or your specific hub (e.g., EV3Hub, CityHub, etc.)

def Jungle_Tree_Lift():   

    # The drivebase can accept speeds down to zero, but is not very efficient and
    # quite erratic. Realistically, 30 is a good minimum speed
    DB_MIN_SPEED_MMSEC = 30
    
    # Lowest usable accelleration, determined by testing
    DB_MIN_ACCEL_MMSEC2: int = 5
    
    # Max and min turning speeds, determined by testing
    # These are not affected by the tire size
    DB_MIN_TURN_RATE_DEGSEC: int = 20
    DB_MIN_TURN_ACCEL_DEGSEC2: int = 10
    
    # Straight Acceleration constants
    # Anything above 800 mm/sec^2 causes wheel slippage, regardless of the
    # tire size. The mass of the 56 and 88mm robots is about the same, so the
    # force to maintain that acceleration is the same
    # For 56mm, the maximum that can be set in the settings() command is 9775.
    # For 88mm, the maximum that can be set in the settings() command is 15360.
    DB_MAX_ACCEL_MMSEC2: int = 800
    
    # For turn rates, the best speed and acceleration was determined by testing
    # It did not matter if it was on 56mm or 88mm tires, the values were the
    # same for both. 180 deg/sec for speed and 360 deg/sec^2 for acceleration
    # For 56mm, the maximum speed that can be set in the settings() command is 543
    # For 88mm, the maximum speed that can be set in the settings() command is 854.
    # For 88mm, the maximum accel that can be set in the settings() command is 17094.
    DB_MAX_TURN_RATE_DEGSEC: int = 180
    DB_MAX_TURN_ACCEL_DEGSEC2: int = 360
    
    

    hub = PrimeHub()
    # motors
    leftmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    rightmotor = Motor(Port.A)
    rightarm = Motor(Port.E)
    leftarm = Motor(Port.F)
    # robot mesurements
    wheeldimeter = 56
    axletrack = 114

    # Drivebase parameters. None of these should ever be changed by users
    if wheeldimeter == 56:
            DB_MAX_SPEED_MMSEC: int = 488
    if wheeldimeter == 88:
            DB_MAX_SPEED_MMSEC: int = 768
        # robot meaning

    robot = DriveBase(leftmotor, rightmotor, wheeldimeter, axletrack)
    robot.use_gyro(True)

    def printOrientation(label):
        pitch, roll = hub.imu.tilt()

        print(
            label,
            "distance =", robot.distance(),
            "drive angle =", robot.angle(),
            "imu heading =", hub.imu.heading(),
            "pitch =", pitch,
            "roll =", roll
        )

    def printBattery():

        # Get battery voltage in millivolts (mV)
        voltage = hub.battery.voltage()

        # Approximate voltage range for a standard hub battery (e.g., 6500mV to 8400mV)
        min_voltage = 6500
        max_voltage = 8400

        # Convert voltage to a percentage
        battery_percent = (voltage - min_voltage) * 100 / (max_voltage - min_voltage)
        battery_percent = max(0, min(100, battery_percent))  # Clamp between 0% and 100%

        # Print the results
        print(f"Voltage: {voltage} mV")
        print(f"Battery level: {battery_percent:.1f}%")
    printBattery()

    # uwprogram
        # go straight
        # All default constant percentages will be defined here
    DEFAULT_MED_MOT_SPEED_PCT = 100  # normal attachment moter speed, % value
    DEFAULT_MED_MOT_ACCEL_PCT = 80
    DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
    DEFAULT_BIG_MOT_ACCEL_PCT = 80
    DEFAULT_TURN_SPEED_PCT = 45  #
    DEFAULT_TURN_ACCEL_PCT = 45  #
    DEFAULT_STALL_PCT = 50
    # DEFAULT_STALL_PCT = 50  # not currently used
        
    def Rescale(
            val: int, in_min: int, in_max: int, out_min: int, out_max: int
        ) -> int:
            neg: int = int(val / abs(val))  # will either be 1 or -1
            val = abs(val)
            if in_max == in_min:
                return 0
            if val < in_min:
                val = in_min
            if val > in_max:
                val = in_max
            retVal: int = out_min + (val - in_min) * int(
                (out_max - out_min) / (in_max - in_min)
            )
            if retVal > out_max:
                retVal = out_max
            if retVal < out_min:
                retVal = out_min
            return retVal * neg
        
        
    def RescaleStraightSpeed(speedPct) -> int:
            return Rescale(
                speedPct,
                1,
                100,
                DB_MIN_SPEED_MMSEC,
                DB_MAX_SPEED_MMSEC,
            )
        
        
    def RescaleStraightAccel(accelPct) -> int:
            return Rescale(
                accelPct,
                1,
                100,
                DB_MIN_ACCEL_MMSEC2,
                DB_MAX_ACCEL_MMSEC2,
            )
        
        
    def RescaleTurnSpeed(turnSpeedPct) -> int:
            # print(turnSpeedPct)
            return Rescale(
                turnSpeedPct,
                1,
                100,
                DB_MIN_TURN_RATE_DEGSEC,
                DB_MAX_TURN_RATE_DEGSEC,
            )
        
        
    def RescaleTurnAccel(turnAccelPct) -> int:
            return Rescale(
                turnAccelPct,
                1,
                100,
                DB_MIN_TURN_ACCEL_DEGSEC2,
                DB_MAX_TURN_ACCEL_DEGSEC2,
            )
        
    print('RescaleStraightSpeed',RescaleStraightSpeed(DEFAULT_BIG_MOT_SPEED_PCT))
    print(RescaleStraightAccel(DEFAULT_BIG_MOT_ACCEL_PCT))
    print(RescaleTurnSpeed(DEFAULT_TURN_SPEED_PCT))
    print( RescaleTurnAccel(DEFAULT_TURN_ACCEL_PCT))
        
        #robot.settings(346,637,64,142)
    robot.settings(RescaleStraightSpeed(DEFAULT_BIG_MOT_SPEED_PCT),
                    RescaleStraightAccel(DEFAULT_BIG_MOT_ACCEL_PCT),
                    RescaleTurnSpeed(DEFAULT_TURN_SPEED_PCT),
                    RescaleTurnAccel(DEFAULT_TURN_ACCEL_PCT),)
        
        


hub = PrimeHub()
# motors
leftmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightmotor = Motor(Port.A)
rightarm = Motor(Port.E)
leftarm = Motor(Port.F)
# robot mesurements
wheeldimeter = 56
axletrack = 114

robot = DriveBase(leftmotor, rightmotor, wheeldimeter, axletrack)
robot.use_gyro(True)

def printOrientation(label):
    pitch, roll = hub.imu.tilt()

    print(
        label,
        "distance =", robot.distance(),
        "drive angle =", robot.angle(),
        "imu heading =", hub.imu.heading(),
        "pitch =", pitch,
        "roll =", roll
    )

def printBattery():

    # Get battery voltage in millivolts (mV)
    voltage = hub.battery.voltage()

    # Approximate voltage range for a standard hub battery (e.g., 6500mV to 8400mV)
    min_voltage = 6500
    max_voltage = 8400

    # Convert voltage to a percentage
    battery_percent = (voltage - min_voltage) * 100 / (max_voltage - min_voltage)
    battery_percent = max(0, min(100, battery_percent))  # Clamp between 0% and 100%

    # Print the results
    print(f"Voltage: {voltage} mV")
    print(f"Battery level: {battery_percent:.1f}%")
printBattery()

    
# program starts here
robot.use_gyro(True)
#robot goes to the tree
robot.straight(270)


#robot turns to the jungle tree
robot.turn(50)
robot.straight(460)
robot.turn(-50)

#lowering collector
leftarm.run(450)
wait(800)
leftarm.stop()


#getting closer to tree to lift platform and collect seed
robot.straight(205)



#Backing up to solve the vine
robot.straight(-200)

#lowering grabber 
rightarm.run(-180)
wait(900)
rightarm.stop()
#getting closer to drag the vine
robot.straight(50)

#lifting arm for solving vine
rightarm.run(120)
wait(900)
rightarm.stop()

#going home
robot.straight(-10)
robot.turn(25)

robot.settings(900,637,64,142)
robot.straight(-690)