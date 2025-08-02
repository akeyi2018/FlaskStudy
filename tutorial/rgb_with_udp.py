import socket
from gpiozero import RGBLED
from time import sleep, time

# GPIOピン（BCM番号）
led = RGBLED(red=16, green=20, blue=21)

# UDP設定
UDP_IP = "0.0.0.0"  # すべてのインターフェースで受信
UDP_PORT = 5005     # 任意のポート番号（送信側と一致させる）

# ソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.1)  # 非ブロッキングに近く（0.1秒待って何もなければ次へ）

print(f"Listening for UDP packets on port {UDP_PORT}...")

last_received_time = time()
timeout_seconds = 1.0  # 1秒以上受信がなければLEDを消す

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            r, g, b = map(float, data.decode().strip().split(","))
            r = max(0.0, min(1.0, r))
            g = max(0.0, min(1.0, g))
            b = max(0.0, min(1.0, b))
            led.color = (r, g, b)
            last_received_time = time()
            # print(f"Received RGB: {r:.2f}, {g:.2f}, {b:.2f}")
        except socket.timeout:
            pass  # 受信なしでもエラーとしない
        except Exception as e:
            print(f"Invalid data received — {e}")

        # 一定時間受信がない場合はLEDをオフに
        if time() - last_received_time > timeout_seconds:
            led.color = (0, 0, 0)

        sleep(0.05)  # 過負荷防止

except KeyboardInterrupt:
    print("\n終了します")
    led.off()
    sock.close()
