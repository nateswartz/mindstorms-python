from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


def wave_arm(arm, iterations, distance, speed):
    for i in range(iterations):
        arm.run_to_position(distance, 'shortest path', speed)
        arm.run_to_position(0, 'shortest path', speed)

def charlie_happy():
    hub.light_matrix.set_pixel(0,0,70)
    hub.light_matrix.set_pixel(0,1,70)
    hub.light_matrix.set_pixel(0,3,70)
    hub.light_matrix.set_pixel(0,4,70)

    hub.light_matrix.set_pixel(2,0,100)
    hub.light_matrix.set_pixel(2,1,100)
    hub.light_matrix.set_pixel(2,3,100)
    hub.light_matrix.set_pixel(2,4,100)

    hub.light_matrix.set_pixel(3,0,100)
    hub.light_matrix.set_pixel(3,1,100)
    hub.light_matrix.set_pixel(3,3,100)
    hub.light_matrix.set_pixel(3,4,100)



# Create your objects here.
hub = MSHub()
right_arm = Motor('B')
left_arm = Motor('F')
arms = MotorPair('B', 'F')


# Write your program here.
charlie_happy()
hub.speaker.beep()
arms.move(-80, 'degrees', 0, 80)
arms.move(80, 'degrees', 0, 80)
wave_arm(right_arm, 2, 100, 80)
wave_arm(left_arm, 2, 260, 80)


# Reset to neutral
right_arm.run_to_position(0, 'shortest path', 30)
left_arm.run_to_position(0, 'shortest path', 30)
