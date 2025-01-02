import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)
    
def oper_scharr(file):
    img = cv2.imread("%s/%s" % (image_folder, file))
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 1
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    dst1 = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0) # cv2的沙尔算子
    dst2 = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1) # cv2的沙尔算子
    # add = cv2.add(dst1, dst2) # 图像叠加方法一
    add = cv2.addWeighted(dst1, 0.5, dst2, 0.5, gamma=0) # 图像叠加方法二

    cv2.imshow("img", img)
    # cv2.imshow("dst1", dst1)
    # cv2.imshow("dst2", dst2)
    # cv2.imshow("add", add)
    cv2.imshow("list", np.hstack((dst1, dst2, add)))
    cv2.waitKey(0)
    cv2.destroyAllWindows();

if __name__ == "__main__":
    oper_scharr("04.png")

### 沙尔算子，用来找出图像中物资的边界，效果比索贝尔算子好

