from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(27,17)

# led = LED(5)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)

# sensor.when_activated
# sensor.when_in_range = led.on
# sensor.when_out_of_range = led.off

# pause()