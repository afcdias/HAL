import numpy
from PIL import ImageGrab
import cv2
import time
#import chilimangoes

clock = time.time()
fps = 0
while(True):
    fps += 1
    if(time.time() - clock > 1):
        print('{} FPS'.format(fps))
        fps = 0
        clock = time.time()

    screen = numpy.array(ImageGrab.grab())
    cv2.imshow('test', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    cv2.waitKey(1)

    #cv2.imshow('test', numpy.array(ImageGrab.grab(bbox = (0,0,800,600))))
    #cv2.imshow('window', numpy.array(chilimangoes.grab_screen))