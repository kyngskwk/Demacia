# -*- coding: utf-8 -*-

import cv2
import change_text 
 
# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture('./람머스.mp4')
 
count = 0

length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
while(vidcap.isOpened()):
    ret, image = vidcap.read()
    if int(vidcap.get(1)) == 50:
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("./images/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1
    elif int(vidcap.get(1)) % (length-50) == 0:
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("./images/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1
    elif int(vidcap.get(1)) == (length-10):
        break

change_text.module()