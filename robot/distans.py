from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(27,17, max_distance=1, threshold_distance=0.2)

led = LED(5)

# while True:
    # print('Distance to nearest object is', sensor.distance, 'm')
    # sleep(1)

def test():
    print('Active')

sensor.when_activated = test() 
# sensor.when_in_range = led.on
# sensor.when_out_of_range = led.off

pause()