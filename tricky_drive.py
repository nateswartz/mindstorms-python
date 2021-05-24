from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()

# Write your program here.
arm = Motor('C')
wheels = MotorPair('A', 'B')

# Arms up and down
arm.run_for_degrees(-60, 20)
wait_for_seconds(1)
arm.run_for_degrees(60, 20)

# Go straight, back up
wheels.start(speed=30)
wait_for_seconds(0.5)
wheels.stop()
wheels.start(speed=-30)
wait_for_seconds(0.5)
wheels.stop()

# Spin in circles
wheels.move(2, 'rotations', steering=100)
wheels.move(2, 'rotations', steering=-100)

hub.speaker.beep()
