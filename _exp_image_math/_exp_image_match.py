import os
import cv2
import numpy
import matplotlib.pyplot as plt

dir_this = os.path.dirname(__file__)

#opencv模板匹配----单目标匹配
def _single_match_1():
    #读取目标图片
    target = cv2.imread("{}/hui/hui.jpg".format(dir_this))
    target_copy = target.copy()
    #读取模板图片
    template_name = 'yan2.png'
    template = cv2.imread("{}/hui/{}".format(dir_this, template_name))
    
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]
    methods.sort()

    plt.figure(figsize=(16, 9))
    method_count = len(methods)
    for i in range(len(methods)):
        method = methods[i]
        img = target_copy.copy()

        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)

        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        
        plt.subplot(method_count, 2, (i * 2 + 1)), plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result {}'.format(i)), plt.xticks([]), plt.yticks([])
        plt.subplot(method_count, 2, (i * 2 + 2)), plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point {}'.format(i)), plt.xticks([]), plt.yticks([])
    plt.suptitle('Image Matching [{}]'.format(template_name))
    plt.show()

#opencv模板匹配----单目标匹配
def _single_match_2():
    #读取目标图片
    target = cv2.imread("{}/hui/hui.jpg".format(dir_this))
    target_copy = target.copy()
    
    template_list = ['yan1.png', 'yan2.png', 'yan3.png', 'yan4.png']
    template_count = len(template_list)
    plt.figure(figsize=(16, 9))
    for i in range(len(template_list)):
        #读取模板图片
        template = cv2.imread("{}/hui/{}".format(dir_this, template_list[i]))
        
        #获得模板图片的高宽尺寸
        theight, twidth = template.shape[:2]
        
        # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
        
        method = cv2.TM_SQDIFF_NORMED
        img = target_copy.copy()
        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print('->[%s], min_val: %f, max_val: %f' % (template_list[i], min_val, max_val))

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)

        if min_val <= 0.3:
            cv2.rectangle(img, top_left, bottom_right, 255, 2)
        
        plt.subplot(template_count, 3, (i * 3 + 1)), plt.imshow(template)
        plt.title('Template {}'.format(template_list[i])), plt.xticks([]), plt.yticks([])
        plt.subplot(template_count, 3, (i * 3 + 2)), plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(template_count, 3, (i * 3 + 3)), plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point {} [{}]'.format(template_list[i], min_val)), plt.xticks([]), plt.yticks([])
    plt.suptitle('Image Matching')
    plt.show()

#opencv模板匹配----多目标匹配
def _multi_match():
    #读取目标图片
    target = cv2.imread("target.jpg")
    #读取模板图片
    template = cv2.imread("template.jpg")
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    #cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #绘制矩形边框，将匹配区域标注出来
    #min_loc：矩形定点
    #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(min_val)
    #初始化位置参数
    temp_loc = min_loc
    other_loc = min_loc
    numOfloc = 1
    #第一次筛选----规定匹配阈值，将满足阈值的从result中提取出来
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法设置匹配阈值为0.01
    threshold = 0.01
    loc = numpy.where(result<threshold)
    #遍历提取出来的位置
    for other_loc in zip(*loc[::-1]):
        #第二次筛选----将位置偏移小于5个像素的结果舍去
        if (temp_loc[0]+5<other_loc[0])or(temp_loc[1]+5<other_loc[1]):
            numOfloc = numOfloc + 1
            temp_loc = other_loc
            cv2.rectangle(target,other_loc,(other_loc[0]+twidth,other_loc[1]+theight),(0,0,225),2)
    str_numOfloc = str(numOfloc)
    #显示结果,并将匹配值显示在标题栏上
    strText = "MatchResult----MatchingValue="+strmin_val+"----NumberOfPosition="+str_numOfloc
    cv2.imshow(strText,target)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # _single_match_1()
    _single_match_2()
    # _multi_match()