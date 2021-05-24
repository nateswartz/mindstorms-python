from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import hub

B = 9
_ = 0

def set_leds(led_array, brightness, sideways):
    for x in range(0,5):
        for y in range(0,5):
            if not sideways:
                if (led_array[y][x] == B):
                    mindstorm_hub.light_matrix.set_pixel(x, y, brightness)
                else:
                    mindstorm_hub.light_matrix.set_pixel(x, y, 0)
            else:
                if (led_array[x][4-y] == 1):
                    mindstorm_hub.light_matrix.set_pixel(x, y, brightness)
                else:
                    mindstorm_hub.light_matrix.set_pixel(x, y, 0)

def draw_letter(letter, brightness):
    led_array = [[]]
    if (letter == 'a'):
        led_array = [[_,B,B,_,_], 
                     [B,_,_,B,_], 
                     [B,B,B,B,_], 
                     [B,_,_,B,_], 
                     [B,_,_,B,_]]
    if (letter == 'b'):
        led_array = [[B,B,B,_,_], 
                     [B,_,_,B,_], 
                     [B,B,B,_,_], 
                     [B,_,_,B,_], 
                     [B,B,B,_,_]]
    if (letter == 'c'):
        led_array = [[_,B,B,B,_], 
                     [B,_,_,_,_], 
                     [B,_,_,_,_], 
                     [B,_,_,_,_], 
                     [_,B,B,B,_]]
    if (letter == 'd'):
        led_array = [[B,B,B,_,_], 
                     [B,_,_,B,_], 
                     [B,_,_,B,_], 
                     [B,_,_,B,_], 
                     [B,B,B,_,_]]
    if (letter == 'e'):
        led_array = [[B,B,B,B,_],
                     [B,_,_,_,_],
                     [B,B,B,B,_],
                     [B,_,_,_,_],
                     [B,B,B,B,_]]
    if (letter == 'f'):
        led_array = [[B,B,B,B,_],
                     [B,_,_,_,_],
                     [B,B,B,B,_],
                     [B,_,_,_,_],
                     [B,_,_,_,_]]
    if (letter == 'g'):
        led_array = [[B,B,B,B,B],
                     [B,_,_,_,_],
                     [B,_,B,B,B],
                     [B,_,_,_,B],
                     [B,B,B,B,B]]
    if (letter == 'l'):
        led_array = [[B,_,_,_,_], 
                     [B,_,_,_,_], 
                     [B,_,_,_,_], 
                     [B,_,_,_,_], 
                     [B,B,B,B,_]]
    if (letter == 'n'):
        led_array = [[B,_,_,_,B], 
                     [B,B,_,_,B], 
                     [B,_,B,_,B], 
                     [B,_,_,B,B], 
                     [B,_,_,_,B]]
    if (letter == 'y'):
        led_array = [[B,_,_,_,B], 
                     [_,B,_,B,_], 
                     [_,_,B,_,_], 
                     [_,_,B,_,_], 
                     [_,_,B,_,_]]

    set_leds(led_array, brightness, False)

def fade_letter_in(letter, brightness_increment, time_interval):
    brightness = 0
    while (brightness < 100):
        draw_letter(letter, brightness)
        brightness += brightness_increment
        wait_for_seconds(time_interval)

def fade_letter_out(letter, brightness_decrement, time_interval):
    brightness = 100
    while (brightness >= 0):
        draw_letter(letter, brightness)
        brightness -= brightness_decrement
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
mindstorm_hub = MSHub()

# Write your program here.
mindstorm_hub.speaker.beep()
show_message('alba and clay', 20, 0.15)
mindstorm_hub.speaker.beep()