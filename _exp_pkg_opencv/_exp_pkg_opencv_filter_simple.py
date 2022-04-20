import os
import sys
import cv2
import numpy as np

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)

img = cv2.imread("%s/01.jpg" % image_folder)
# img = cv2.resize(img, (256, 256)) # 设置大小
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 均值滤波
# kernel = np.ones((5, 5), np.float32) / 25

# # 突出轮廓
# kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])

# 浮雕效果
kernel = np.array([[-2,1,0], [-1,1,1], [0,1,2]])

dst = cv2.filter2D(img_gray, -1, kernel=kernel)

# print("image shape: %s" % img.shape)
# print("dst shape: %s" % dst.shape)

cv2.imshow("img", np.hstack((img_gray, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows();
