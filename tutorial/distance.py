from gpiozero import DistanceSensor, LED, Servo
from signal import pause
from time import sleep

sensor = DistanceSensor(echo=17, trigger=27, max_distance=1, threshold_distance=0.1)
led = LED(5)
# sv = Servo(18)
# sv.min()
# sleep(0.1)

def move_max():
    sv = Servo(18)
    sv.max()
    sleep(0.2)
    led.on()
    # sv.min()
    # sv.closed()

def move_mid():
    sv = Servo(18)
    sv.mid()
    sleep(0.2)
    led.off()
    # sv.min()
    # sv.closed()

sensor.when_in_range = move_max
sensor.when_out_of_range = move_mid

pause()