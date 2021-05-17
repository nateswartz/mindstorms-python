from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import random

snake_head = (3, 0)
snake_front_mid = (2, 0)
snake_back_mid = (1, 0)
snake_tail = (0, 0)
last_direction = 'right'

def is_section_valid(section):
    return section[0] >= 0 and section[0] < 5 and section[1] >= 0 and section[1] < 5

def draw_snake_section(coordinates, brightness, charlie_transform):
    start_x = 0
    start_y = 0
    if charlie_transform:
        temp_x = coordinates[1]
        start_y = 4 - coordinates[0]
        start_x = temp_x
    hub.light_matrix.set_pixel(start_x, start_y, brightness)

def draw_snake(charlie_transform):
    hub.light_matrix.off()
    draw_snake_section(snake_head, 100, charlie_transform)
    draw_snake_section(snake_front_mid, 90, charlie_transform)
    draw_snake_section(snake_back_mid, 80, charlie_transform)
    draw_snake_section(snake_tail, 70, charlie_transform)

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
    global snake_front_mid
    global snake_back_mid
    global snake_head
    global last_direction

    potential_head = snake_head
    potential_front_mid = snake_front_mid
    potential_back_mid = snake_back_mid
    potential_tail = snake_tail
    potential_last_direction = last_direction

    # don't allow complete reversal of direction
    if is_reverse(direction, last_direction):
        return False

    potential_tail = potential_back_mid
    potential_back_mid = potential_front_mid
    potential_front_mid = potential_head
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

    # don't allow head to move where the tail currently exists
    if potential_head == snake_tail:
        return False

    # avoid exceeding boundaries of LED grid
    if is_section_valid(potential_head) and is_section_valid(potential_front_mid) and is_section_valid(potential_back_mid) and is_section_valid(potential_tail):
        last_direction = potential_last_direction
        snake_head = potential_head
        snake_front_mid = potential_front_mid
        snake_back_mid = potential_back_mid
        snake_tail = potential_tail
        return True
    return False

def snake_travel(direction):
    success = try_move_snake(direction)
    if not success:
        return False
    draw_snake(True)
    wait_for_seconds(0.8)
    return True

def reset_snake():
    global snake_head
    global snake_front_mid
    global snake_back_mid
    global snake_tail
    global last_direction

    snake_head = (3, 0)
    snake_front_mid = (2, 0)
    snake_back_mid = (1, 0)
    snake_tail = (0, 0)
    last_direction = 'right'

def start():
    draw_snake(True)
    wait_for_seconds(0.8)
    failed_move_attempts = 0

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
        success = snake_travel(direction)
        if not success:
            failed_move_attempts += 1
        else:
            failed_move_attempts = 0
        if failed_move_attempts >= 20:
            hub.speaker.beep()
            wait_for_seconds(0.2)
            hub.speaker.beep()
            wait_for_seconds(0.2)
            hub.light_matrix.off()
            return

# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()
while True:
    reset_snake()
    start()