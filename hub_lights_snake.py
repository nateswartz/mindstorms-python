from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import random

snake_head = (2, 0)
snake_mid = (1, 0)
snake_tail = (0, 0)
last_direction = 'none'

def is_section_valid(section):
    return section[0] >= 0 and section[0] < 5 and section[1] >= 0 and section[1] < 5

def draw_snake_section(coordinates, charlie_transform):
    start_x = 0
    start_y = 0
    if charlie_transform:
        temp_x = coordinates[1]
        start_y = 4 - coordinates[0]
        start_x = temp_x
    hub.light_matrix.set_pixel(start_x, start_y)

def draw_snake(charlie_transform):
    hub.light_matrix.off()
    draw_snake_section(snake_head, charlie_transform)
    draw_snake_section(snake_mid, charlie_transform)
    draw_snake_section(snake_tail, charlie_transform)

def is_reverse(direction, last_direction):
    if direction == 'right' and last_direction == 'left':
        return True
    if direction == 'left' and last_direction == 'right':
        return True
    if direction == 'up' and last_direction == 'down':
        return True
    if direction == 'down' and last_direction == 'up':
        return True
    return False

def try_move_snake(direction):
    global snake_tail
    global snake_mid
    global snake_head
    global last_direction

    potential_head = snake_head
    potential_mid = snake_mid
    potential_tail = snake_tail
    potential_last_direction = last_direction

    if is_reverse(direction, last_direction):
        tmp_head = potential_head
        potential_head = potential_tail
        potential_tail = tmp_head

    potential_tail = potential_mid
    potential_mid = potential_head
    if direction == 'right':
        potential_head = (potential_head[0] + 1, potential_head[1])
        potential_last_direction = 'right'
    if direction == 'down':
        potential_head = (potential_head[0], potential_head[1] + 1)
        potential_last_direction = 'down'
    if direction == 'left':
        potential_head = (potential_head[0] - 1, potential_head[1])
        potential_last_direction = 'left'
    if direction == 'up':
        potential_head = (potential_head[0], potential_head[1] - 1)
        potential_last_direction = 'up'

    if is_section_valid(potential_head) and is_section_valid(potential_mid) and is_section_valid(potential_tail):
        last_direction = potential_last_direction
        snake_head = potential_head
        snake_mid = potential_mid
        snake_tail = potential_tail
        return True
    return False

def snake_travel(direction):
    try_move_snake(direction)
    draw_snake(True)
    wait_for_seconds(0.8)

def start():
    draw_snake(True)
    wait_for_seconds(0.8)

    while True:
        random_number = random.randint(0, 3)
        direction = 'none'
        if (random_number == 0):
            direction = 'right'
        if (random_number == 1):
            direction = 'left'
        if (random_number == 2):
            direction = 'up'
        if (random_number == 3):
            direction = 'down'
        snake_travel(direction)


# Create your objects here.
hub = MSHub()



# Write your program here.
hub.speaker.beep()
start()