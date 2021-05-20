from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

def set_leds(led_array, brightness):
    for x in range(0,5):
        for y in range(0,5):
            if (led_array[x][y] == 1):
                hub.light_matrix.set_pixel(x, y, brightness)

def draw_letter(letter, brightness):
    led_array = [[]]
    if (letter == 'a'):
        led_array = [[0,0,1,1,0], [0,1,0,0,1], [0,1,1,1,1], [0,1,0,0,1], [0,1,0,0,1]]
    if (letter == 'b'):
        led_array = [[0,0,1,1,1], [0,1,0,0,1], [0,0,1,1,1], [0,1,0,0,1], [0,0,1,1,1]]
    if (letter == 'c'):
        led_array = [[0,1,1,1,0], [0,0,0,0,1], [0,0,0,0,1], [0,0,0,0,1], [0,1,1,1,0]]
    if (letter == 'd'):
        led_array = [[0,0,1,1,1], [0,1,0,0,1], [0,1,0,0,1], [0,1,0,0,1], [0,0,1,1,1]]
    if (letter == 'l'):
        led_array = [[0,0,0,0,1], [0,0,0,0,1], [0,0,0,0,1], [0,0,0,0,1], [0,1,1,1,1]]
    if (letter == 'n'):
        led_array = [[1,0,0,0,1], [1,0,0,1,1], [1,0,1,0,1], [1,1,0,0,1], [1,0,0,0,1]]
    if (letter == 'y'):
        led_array = [[1,0,0,0,1], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0]]

    set_leds(led_array, brightness)

def set_leds(led_array, brightness):
    for x in range(0,5):
        for y in range(0,5):
            if (led_array[x][y] == 1):
                hub.light_matrix.set_pixel(x, y, brightness)

def fade_letter_in(letter, brightness_increment, time_interval):
    hub.light_matrix.off()
    brightness = 0
    while (brightness < 100):
        brightness += brightness_increment
        draw_letter(letter, brightness)
        wait_for_seconds(time_interval)

def fade_letter_out(letter, brightness_decrement, time_interval):
    brightness = 100
    draw_letter(letter, brightness)
    while (brightness > 0):
        brightness -= brightness_decrement
        draw_letter(letter, brightness)
        wait_for_seconds(time_interval)

def show_letter(letter, brightness_change, time_interval):
    fade_letter_in(letter, brightness_change, time_interval)
    fade_letter_out(letter, brightness_change, time_interval)

def show_message(message, brightness_change, time_interval):
    for letter in message:
        if letter == ' ':
            wait_for_seconds(0.5)
        else:
            show_letter(letter, brightness_change, time_interval)

# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()
show_message('alba and clay', 20, 0.15)
hub.speaker.beep()