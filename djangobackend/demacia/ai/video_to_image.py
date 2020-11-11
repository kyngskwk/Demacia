import cv2
for i in range(len(videoFiles)):
    cam = cv2.VideoCapture(videoFile)
    currentFrame = 0
    while(True):
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(currentFrame + '.jpg', frame)
            currentFrame += 1
        else:
            break
    cam.release()
