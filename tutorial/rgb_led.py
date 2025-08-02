from gpiozero import RGBLED
from time import sleep
import random

# GPIOピンの設定（red=21, green=20, blue=16）
led = RGBLED(red=21, green=20, blue=16)

try:
    while True:
        # RGB各値を0.0〜1.0の範囲でランダム生成
        r = random.uniform(0, 1)
        g = random.uniform(0, 1)
        b = random.uniform(0, 1)

        # print(f"R: {r:.2f}, G: {g:.2f}, B: {b:.2f}")
        led.color = (r, g, b)  # LEDの色を変更
        sleep(0.2)  # 1秒ごとに色を変更
        led.off()
        sleep(0.1)
except KeyboardInterrupt:
    led.off()
    print("LEDをオフにして終了しました")