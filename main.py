import video
import time
import sys
import numpy as np
import cv2
import time

# while (True):
#     # try:
#     # print(1)
#     video = video.Video()
#     time.sleep(1.0)  # let camera autofocus + autosaturation settle
#     # video.nextFrame()
#     # video.testBackgroundFrame()

while True:
    video_test = video.Video()
    print(video_test)
    while 1:
        try:
            # get next frame of video
            video_test.nextFrame()
            # video.testBackgroundFrame()  # press n to delete background?
            video_test.updateBackground()
            video_test.compare()
            video_test.showFrame()
            video_test.testSettings()
            # video.destroyNow()
            # k = cv2.waitKey(30) & 0xff
            # if video.testDestroy():
            #         # if k == 27:
        except AttributeError:

            video_test = video.Video()
            print(video_test)
            continue
# except BaseException:
#
#     continue
