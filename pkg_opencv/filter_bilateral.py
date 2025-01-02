import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)
    
def filter_bilateral(file):
    img = cv2.imread("%s/%s" % (image_folder, file))
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 1
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后

    dst1 = cv2.bilateralFilter(img, 3, sigmaColor=20, sigmaSpace=50) # cv2的双边滤波
    dst2 = cv2.bilateralFilter(img, 5, sigmaColor=20, sigmaSpace=50) # cv2的双边滤波
    dst3 = cv2.bilateralFilter(img, 7, sigmaColor=20, sigmaSpace=50) # cv2的双边滤波
    dst4 = cv2.bilateralFilter(img, 11, sigmaColor=20, sigmaSpace=50) # cv2的双边滤波

    cv2.imshow("bilateral filter", np.hstack((img, dst1, dst2, dst3, dst4)))
    cv2.waitKey(0)
    cv2.destroyAllWindows();

if __name__ == "__main__":
    filter_bilateral("10.jpg")
    filter_bilateral("11.jpg")


### 双边滤波具有美颜效果