from gpiozero import PWMLED
import socket
from time import sleep, time

# 各バンドに対応するPWM LED（GPIOピンのBCM番号）
led_pins = [21, 20, 16, 26, 19, 13, 6, 5]
led_list = [PWMLED(pin) for pin in led_pins]

# 通信状態表示用ステータスLED（PWMで光量制御, GPIO12）
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

green_scale = 1.0  # 緑を弱めたいときは 0.5 などに調整
gamma = 2.2        # 視覚補正のガンマ値

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            parts = data.decode().strip().split(",")
            if len(parts) != 8:
                print("Invalid packet length")
                continue

            # 8バンド分の値を読み込み、ガンマ補正・クランプ
            values = []
            for i, raw in enumerate(parts):
                try:
                    val = float(raw)
                    val = max(0.0, min(1.0, val))
                    val = gamma_correct(val, gamma)
                    values.append(val)
                except ValueError:
                    values.append(0.0)

            # 各LEDに出力
            for led, val in zip(led_list, values):
                led.value = val

            last_received_time = time()

        except socket.timeout:
            pass
        except Exception as e:
            print(f"Invalid data received — {e}")

        # 通信状態に応じた status_led の点灯制御
        if time() - last_received_time > timeout_seconds:
            for led in led_list:
                led.value = 0.0  # 全LED OFF
            status_led.value = 0.0
        else:
            status_led.value = 0.2  # 通信がある間はON

        sleep(0.05)

except KeyboardInterrupt:
    print("\n終了します")
    for led in led_list:
        led.off()
    status_led.off()
    sock.close()
