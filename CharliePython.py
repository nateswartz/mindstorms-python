from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import random

def getRandomColor():
    colors = ["azure","black","blue","cyan","green","orange","pink","red","violet","yellow","white"]
    random_index = random.randint(0, len(colors)-1)
    return colors[random_index]

def getRandomNumber():
    return random.randint(0, 9)

def turnLightMatrixOn(isRandomPattern):
    for x in range(5):
        for y in range(5):
            brightness = 100
            if (isRandomPattern):
                brightness = random.randint(0, 2) * 100 
            hub.light_matrix.set_pixel(x, y, brightness)


# Create your objects here.
hub = MSHub()


# Write your program here.
while True:
    hub.left_button.wait_until_pressed()
    hub.status_light.off()
    hub.light_matrix.off()
    hub.left_button.wait_until_released()
    hub.status_light.on(getRandomColor())
    turnLightMatrixOn(True)
        
