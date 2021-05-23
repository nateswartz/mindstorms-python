from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()

# Write your program here.
arm = Motor('C')
wheels = MotorPair('A', 'B')

arm.run_for_degrees(-60, 20)
wait_for_seconds(1)
arm.run_for_degrees(60, 20)

wheels.start()
wait_for_seconds(0.5)
wheels.stop()
hub.speaker.beep()