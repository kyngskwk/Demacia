from PIL import Image
from matplotlib import pyplot as plt
from pytesseract import *
import numpy as np
import re
import cv2
import pytesseract
# from .get_image import gameId


def change_text(gameId):
    if gameId != None:
        pytesseract.pytesseract.tesseract_cmd = r'//usr//bin//tesseract'
        # pytesseract.pytesseract.tesseract_cmd = r'\\home\\ubuntu\\tesseract'
        # --------------------------------------------------------------------
        # 이미지 구역 나누기v
        time = []
        index = 0
        text_list = []
        for i in range(2):
            image = cv2.imread('./demacia/images/frame%d.jpg' % i)

            # b,g,r = cv2.split(image)
            # image2 = cv2.merge([r,g,b])

            # plt.imshow(image2) # 이미지 좌표 표시
            # plt.xticks([])
            # plt.yticks([])
            # plt.show()

            text_list = []
            # 구역 설정 [가장 왼쪽 x좌표,가장왼쪽 y좌표,width,height]

            sections = [
                # [448,8,15,13],# 불루팀 타워
                # [844,8,15,13],# 레드팀 타워
                # [504,7,35,17],# 불루팀 골드
                # [760,7,35,17],# 레드팀 골드
                # [602,11,28,20],# 불루팀 kill
                # [662,11,27,20],# 레드팀 kill
                # [586,573,22,135], # 불루팀 cs
                # [681,573,22,135],# 레드팀 cs
                [628, 50, 7, 11],  # 분1
                [636, 50, 6, 11],  # 분2

                [645, 50, 7, 11],  # 초1
                [651, 50, 7, 11]  # 초2


            ]

            for section in sections:
                x, y, w, h = section
                img_trim = image[y:y+h, x:x+w]
                cv2.imwrite(f'org_trim{index}.jpg', img_trim)
                org_image = cv2.imread(f'org_trim{index}.jpg')
                # ------------------------------------------------------------------------------
                src = cv2.imread(f'org_trim{index}.jpg', cv2.IMREAD_COLOR)
                big_src = cv2.resize(src, None, fx=8, fy=8,
                                     interpolation=cv2.INTER_CUBIC)
                gray = cv2.cvtColor(big_src, cv2.COLOR_BGR2GRAY)

                gray = cv2.threshold(gray, 120, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)[
                    1]  # 흑백화
                binary = cv2.threshold(
                    gray, 120, 255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)[1]
                kernel = np.ones((1, 1), np.uint8)
                binary = cv2.dilate(binary, kernel, iterations=1)
                binary = cv2.erode(binary, kernel, iterations=1)
                thresh = cv2.threshold(binary, 0, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.threshold(
                    binary, 0, 255, cv2.THRESH_BINARY_INV)[1]
                resized_image = cv2.resize(thresh, (28, 28))
                cv2.imwrite(f'result{index}.jpg', resized_image)
                # print('middle')
                custom_config = r'--oem 3 --psm 6 outputbase digits'

                text = pytesseract.image_to_string(
                    thresh, config=custom_config)
                print(text)

                tmp = list(map(str, text.split('\n')))

                if len(text_list) >= 4 and tmp[0] == '4' and int(text_list[index-4]) > int(tmp[0]):
                    if index != 6:
                        tmp[0] = '6'
                text_list.append(tmp[0])
                index += 1

        for i in range(8):
            try:
                int(text_list[i])
            except ValueError:
                text_list[i] = '0'
        text_list = list(map(int, text_list))

        for i in range(4):
            if text_list[i] == 0:
                if abs(text_list[i] - text_list[i+4]) > 1:
                    if i == 1:
                        if text_list[2] > text_list[6]:
                            text_list[i] = text_list[i+4] - 1
        new_time = [[str(text_list[0])+str(text_list[1]), str(text_list[2])+str(text_list[3])],
                    [str(text_list[4])+str(text_list[5]), str(text_list[6])+str(text_list[7])]]
    else:
        # print('change_text none값')
        new_time = None
        gameId = None
    return new_time, gameId
