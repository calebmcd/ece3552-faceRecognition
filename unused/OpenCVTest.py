import cv2
import time
from picamera import PiCamera
from picamera.array import PiRGBArray

camera = PiCamera()
rawCap = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCap, format = "bgr")
image = rawCap.array

cv2.imshow("Image", image)
cv2.waitKey(0)