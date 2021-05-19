from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

def draw_letter(letter, brightness):
    if (letter == 'a'):
        hub.light_matrix.set_pixel(0, 2, brightness)
        hub.light_matrix.set_pixel(0, 3, brightness)
        hub.light_matrix.set_pixel(1, 1, brightness)
        hub.light_matrix.set_pixel(1, 4, brightness)
        hub.light_matrix.set_pixel(2, 1, brightness)
        hub.light_matrix.set_pixel(2, 2, brightness)
        hub.light_matrix.set_pixel(2, 3, brightness)
        hub.light_matrix.set_pixel(2, 4, brightness)
        hub.light_matrix.set_pixel(3, 1, brightness)
        hub.light_matrix.set_pixel(3, 4, brightness)
        hub.light_matrix.set_pixel(4, 1, brightness)
        hub.light_matrix.set_pixel(4, 4, brightness)
    if (letter == 'l'):
        hub.light_matrix.set_pixel(0, 4, brightness)
        hub.light_matrix.set_pixel(1, 4, brightness)
        hub.light_matrix.set_pixel(2, 4, brightness)
        hub.light_matrix.set_pixel(3, 4, brightness)
        hub.light_matrix.set_pixel(4, 1, brightness)
        hub.light_matrix.set_pixel(4, 2, brightness)
        hub.light_matrix.set_pixel(4, 3, brightness)
        hub.light_matrix.set_pixel(4, 4, brightness)
    if (letter == 'b'):
        hub.light_matrix.set_pixel(0, 2, brightness)
        hub.light_matrix.set_pixel(0, 3, brightness)
        hub.light_matrix.set_pixel(0, 4, brightness)
        hub.light_matrix.set_pixel(1, 1, brightness)
        hub.light_matrix.set_pixel(1, 4, brightness)
        hub.light_matrix.set_pixel(2, 2, brightness)
        hub.light_matrix.set_pixel(2, 3, brightness)
        hub.light_matrix.set_pixel(2, 4, brightness)
        hub.light_matrix.set_pixel(3, 1, brightness)
        hub.light_matrix.set_pixel(3, 4, brightness)
        hub.light_matrix.set_pixel(4, 2, brightness)
        hub.light_matrix.set_pixel(4, 3, brightness)
        hub.light_matrix.set_pixel(4, 4, brightness)

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

# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()
show_letter('a', 20, 0.2)
show_letter('l', 20, 0.2)
show_letter('b', 20, 0.2)
show_letter('a', 20, 0.2)
hub.speaker.beep()