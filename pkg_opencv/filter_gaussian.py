import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)
    
def filter_gaussian():
    img = cv2.imread("%s/02.jpg" % image_folder)
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 1
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后

    dst1 = cv2.GaussianBlur(img, (3, 3), sigmaX=100) # cv2的高斯滤波
    dst2 = cv2.GaussianBlur(img, (5, 5), sigmaX=100) # cv2的高斯滤波
    dst3 = cv2.GaussianBlur(img, (7, 7), sigmaX=100) # cv2的高斯滤波
    dst4 = cv2.GaussianBlur(img, (9, 9), sigmaX=100) # cv2的高斯滤波

    cv2.imshow("gaussian filter", np.hstack((img, dst1, dst2, dst3, dst4)))
    cv2.waitKey(0)
    cv2.destroyAllWindows();

if __name__ == "__main__":
    filter_gaussian()


### 高斯滤波主要用来过滤图片上的噪声，但不适合椒盐噪声