# from pybricks.hubs import TechnicHub
# from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
# from pybricks.robotics import DriveBase
# from pybricks.tools import wait, StopWatch

# hub = TechnicHub()

from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
steering = Motor(Port.B, Direction.CLOCKWISE)
drive = Motor(Port.D, Direction.CLOCKWISE)
car = Car(steering, drive)
xbox = XboxController()


# The main program starts here.
while True:
    # Control steering using the left joystick.
    car.steer(xbox.joystick_left()[0])
    # Control drive power using the trigger buttons.
    car.drive_power(xbox.triggers()[1] - xbox.triggers()[0])
    wait(50)
