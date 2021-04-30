from flask import render_template, Flask, Response
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

app = Flask(__name__)

def take_photo_2():
    stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)

@app.route('/video_feed')
def video_feed():
   #imgタグに埋め込まれるResponseオブジェクトを返す
   return Response(take_photo_2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
   user = {'username': 'FZ50'}
   return render_template('index.html', title='home', user=user)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)