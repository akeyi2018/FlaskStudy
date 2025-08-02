from gpiozero import RGBLED, PWMLED
import socket
from time import sleep, time

# RGBLED（GPIOピンのBCM番号）
led = RGBLED(red=16, green=20, blue=21)

# 通信状態表示用のLED（PWMで光量制御, GPIO12）
status_led = PWMLED(12)

# UDP設定
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.1)

print(f"Listening for UDP packets on port {UDP_PORT}...")

last_received_time = time()
timeout_seconds = 1.0

def gamma_correct(val, gamma=2.2):
    return pow(val, gamma)

green_scale = 1.0  # Green を抑えたい場合
gamma = 2.2        # 視覚補正用

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            r_raw, g_raw, b_raw = map(float, data.decode().strip().split(","))
            # r = max(0.0, min(1.0, r))
            # g = max(0.0, min(1.0, g*0.5))
            # b = max(0.0, min(1.0, b))

            # 明るさ補正と視覚補正
            r = gamma_correct(max(0.0, min(1.0, r_raw)))
            g = gamma_correct(max(0.0, min(1.0, g_raw * green_scale)))
            b = gamma_correct(max(0.0, min(1.0, b_raw)))

            led.color = (r, g, b)
            last_received_time = time()
        except socket.timeout:
            pass
        except Exception as e:
            print(f"Invalid data received — {e}")

        # 通信状態に応じてステータスLEDの明るさを制御
        if time() - last_received_time > timeout_seconds:
            led.color = (0, 0, 0)
            status_led.value = 0.0  # OFF
        else:
            status_led.value = 0.2  # 50% の明るさ
        sleep(0.05)
        # led.color = (0,0,0)
        # sleep(0.02)

except KeyboardInterrupt:
    print("\n終了します")
    led.off()
    status_led.off()
    sock.close()
