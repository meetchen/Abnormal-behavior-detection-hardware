import video
import time
import sys
import numpy as np
import cv2
import time

video = video.Video()
time.sleep(1.0)  # let camera autofocus + autosaturation settle
video.nextFrame()
video.testBackgroundFrame()

while 1:
    try:
        # get next frame of video
        video.nextFrame()
        video.testBackgroundFrame()  # press n to delete background?
        video.updateBackground()
        video.compare()
        video.showFrame()
        video.testSettings()
        k = cv2.waitKey(30) & 0xff
        if video.testDestroy():
            # if k == 27:
            break
    except:
        pass

# video.release()
cv2.destroyAllWindows()
sys.exit()
