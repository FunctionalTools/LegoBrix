#!/usr/bin/env python3

#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()

color_sensor_in1 = ColorSensor(INPUT_1)
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
gyro_sensor_in3 = GyroSensor(INPUT_3)
gps_sensor_in4 = GPSSensor(INPUT_4)
pen_in5 = Pen(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts

tank_drive.on_for_rotations(20, 20, 1)
tank_drive.on_for_rotations(0, 20, 0.55)
tank_drive.on_for_rotations(20, 20, 1.7)
tank_drive.on_for_rotations(20, 0, 1.25)
tank_drive.on_for_rotations(20, 20, 1)
time.sleep(1)
for count in range(5):
    tank_drive.on_for_rotations(20, 20, (-0.5))
    tank_drive.on_for_rotations(20, 20, 0.5)
    time.sleep(1)
tank_drive.on_for_rotations(20, 20, (-1))
tank_drive.on_for_rotations(20, 0, -0.57)
tank_drive.on_for_rotations(20, 20, (-2))
tank_drive.on_for_rotations(20, 0, 1.25)
tank_drive.on_for_rotations(20, 20, (1))
tank_drive.on_for_rotations(0, 20, 1.25)
for count in range(6):
    tank_drive.on_for_rotations(20, 20, (0.1))
    time.sleep(1)
tank_drive.on_for_rotations(20, 20, (-1))
tank_drive.on_for_rotations(20, 0, (-0.055))
