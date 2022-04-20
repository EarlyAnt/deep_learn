import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)
    
def filter_box():
    img = cv2.imread("%s/01.jpg" % image_folder)
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 3
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后

    dst1 = cv2.boxFilter(img, -1, (3, 3), normalize=True) # cv2的盒子滤波
    dst2 = cv2.boxFilter(img, -1, (5, 5), normalize=True) # cv2的盒子滤波
    dst3 = cv2.boxFilter(img, -1, (7, 7), normalize=True) # cv2的盒子滤波
    dst4 = cv2.boxFilter(img, -1, (9, 9), normalize=True) # cv2的盒子滤波

    cv2.imshow("box filter", np.hstack((img, dst1, dst2, dst3, dst4)))
    cv2.waitKey(0)
    cv2.destroyAllWindows();
    
def filter_avg():
    img = cv2.imread("%s/01.jpg" % image_folder)
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 3
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后

    dst1 = cv2.blur(img, (3, 3)) # cv2的均值滤波
    dst2 = cv2.blur(img, (5, 5)) # cv2的均值滤波
    dst3 = cv2.blur(img, (7, 7)) # cv2的均值滤波
    dst4 = cv2.blur(img, (9, 9)) # cv2的均值滤波

    cv2.imshow("avg filter", np.hstack((img, dst1, dst2, dst3, dst4)))
    cv2.waitKey(0)
    cv2.destroyAllWindows();
    
if __name__ == "__main__":
    filter_box()
    filter_avg()
