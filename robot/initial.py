from gpiozero import LED

leds = [6,13,19,26]

for pin in leds:
    LED(pin).off()

