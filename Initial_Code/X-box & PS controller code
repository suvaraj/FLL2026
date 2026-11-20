from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# Initialize the SPIKE Prime hub
hub = PrimeHub()

# Initialize your motors (change ports to match your setup)
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Attachment motors (adjust ports if needed)
attachment_left = Motor(Port.F)
attachment_right = Motor(Port.E)


# Connect to the Xbox controller
# Make sure your controller is in pairing mode the first time you run this!
controller = XboxController()
print("XB",controller.name)

while True:
    # Read left and right stick values (-100 to 100)
    # Different games/drives use different axes; adjust as needed
    sticks = controller.joystick_left()
    x_axis = sticks[1]  # Forward / Backward
    y_axis = controller.joystick_right()[0]  # Turning / Steering

        # --- DRIVE CONTROLS ---
    # joystick_left() returns (x, y); index [1] is forward/backward
    # joystick_right() returns (x, y); index [0] is left/right turning
    drive_speed = controller.joystick_left()[1]
    turn_speed = controller.joystick_right()[0]

    # Simple arcade/tank drive calculation
    left_speed = y_axis + x_axis
    right_speed = y_axis - x_axis

    left_motor.dc(left_speed)
    right_motor.dc(right_speed)


    # --- ATTACHMENT CONTROLS (LT & RT) ---
    # triggers() returns (lt, rt) from 0 to 100 based on trigger pressure
    lt, rt = controller.triggers()

    # Spin each attachment motor proportionally to how hard you press the trigger
    attachment_left.dc(lt)
    attachment_right.dc(rt)



    wait(50)
