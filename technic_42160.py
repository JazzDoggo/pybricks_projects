from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, Car
from pybricks.tools import wait, StopWatch

hub = TechnicHub()

# Set up all devices.
steering = Motor(Port.D, Direction.CLOCKWISE)
front = Motor(Port.B, Direction.CLOCKWISE)
rear = Motor(Port.A, Direction.CLOCKWISE)
car = Car(steering, [front, rear])
xbox = XboxController()

# The main program starts here.
while True:
    # Control steering using the left joystick.
    car.steer(xbox.joystick_left()[0])
    # Control drive power using the trigger buttons.
    car.drive_power(xbox.triggers()[1] - xbox.triggers()[0])
    wait(50)
