import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(__file__)
print("current file path: %s" % os.path.dirname(__file__))
image_folder = "%s/image/filter" % os.path.dirname(__file__)
print("image folder path: %s" % image_folder)
    
def oper_laplacian(file):
    img = cv2.imread("%s/%s" % (image_folder, file))
    width = img.shape[0]
    height = img.shape[1]
    print("width: %s, height: %s" % (width, height))
    scale = 1
    img = cv2.resize(img, (height//scale, width//scale)) # resize方法的dsize参数的顺序是高在前，宽在后
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    dst = cv2.Laplacian(img, -1, ksize=3) # cv2的拉普拉斯算子
    dst_gray = cv2.Laplacian(img_gray, -1, ksize=3) # cv2的拉普拉斯算子
    
    # plt显示图像
    imgs = (img, dst, img_gray, dst_gray)
    fig = plt.figure(figsize=(12, 3))
    plt.title = "laplacian"
    num = len(imgs)
    for i, img in enumerate(imgs):
        ax = fig.add_subplot(1, num, i + 1)
        ax.imshow(img, interpolation="none")
    plt.show()
    
    # # cv2显示图像
    # cv2.imshow("img", np.hstack((img, dst)))
    # cv2.imshow("img_gray", np.hstack((img_gray, dst_gray)))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    oper_laplacian("04.png")

### 拉普拉斯算子，用来找出图像中物资的边界，效果比索贝尔算子好，也比沙尔算子好

