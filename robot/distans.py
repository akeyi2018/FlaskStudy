from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(17,27, max_distance=1, threshold_distance=0.2)
led = LED(5)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()