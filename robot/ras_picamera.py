import picamera
from time import sleep
import datetime
import os
from glob import glob 

class remote_camera:
    def __init__(self):
        self.photofile = datetime.datetime.now().strftime("image_%Y_%m_%d_%H_%M_%S.png") 
        self.fullpath = os.path.join(os.getcwd(), 'static/img', self.photofile)
        self.target_folder = os.path.join(os.getcwd(), 'static/img/*.png')
    def take_photo(self):        
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            sleep(2)
            camera.capture(self.fullpath, resize=(320, 240))
            camera.stop_preview()

    def get_latest_modified_file_path(self):
        list_of_files = glob(self.target_folder)
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

if __name__ == '__main__':
    camera = remote_camera()
    camera.take_photo()
    print(camera.get_latest_modified_file_path())
