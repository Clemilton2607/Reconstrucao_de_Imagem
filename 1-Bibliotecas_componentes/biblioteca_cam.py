"Biblioteca Camera"
from picamera import PiCamera
from time import sleep

"Visalização da camera"
#camera = PiCamera()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()

"Tirar foto"
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/clemilton/Desktop/tirarFoto.jpg')
camera.stop_preview()
