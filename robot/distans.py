from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(27,17, max_distance=1, threshold_distance=0.1)

led = LED(5)

# while True:
    # print('Distance to nearest object is', sensor.distance, 'm')
    # sleep(1)

def test1():
    print('Active')

def test2():
    print('Deactive')

# sensor.when_in_range = led.on
# sensor.when_out_of_range = led.off
sensor.when_activated = led.off
sensor.when_deactivated = led.on

pause()