import os
import cv2
import numpy
import matplotlib.pyplot as plt

dir_this = os.path.dirname(__file__)

#opencv模板匹配----单目标匹配
def _single_match():
    plt.figure(figsize=(12, 8))
    
    dir_hair = '{}/Version 1.0'.format(dir_this)
    print('->root path: %s' % dir_this)
    sub_folder_list = sorted(os.listdir(dir_hair))
    hair_style_count = len(sub_folder_list)
    for i in range(len(sub_folder_list)):
        sub_folder = sub_folder_list[i]
        if not (sub_folder.startswith('.')):
            sub_folder = '{}/{}/'.format(dir_hair, sub_folder)
            print('->sub_folder: %s' % sub_folder)
            
            file_list = sorted(os.listdir(sub_folder))
            template_count = len(file_list)
            for j in range(len(file_list)):
                file = '{}/{}'.format(sub_folder, file_list[j])
                print('->file: %s/%s' % (sub_folder, file))
                
                #读取目标图片
                if j == 0:
                    target = cv2.imread(file)
                    target_copy = target.copy()
                    
                    plt.subplot(hair_style_count, template_count, (i * template_count + j + 1)), plt.imshow(target)
                    plt.title('ori: {}'.format(file_list[j])), plt.xticks([]), plt.yticks([])
                else:
                    #读取模板图片
                    template = cv2.imread(file)
                    
                    #获得模板图片的高宽尺寸
                    theight, twidth = template.shape[:2]
                    
                    # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
                    
                    method = cv2.TM_SQDIFF_NORMED
                    img = target_copy.copy()
                    # Apply template Matching
                    res = cv2.matchTemplate(img, template, method)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    print('->[%s], min_val: %f, max_val: %f' % (file_list[j], min_val, max_val))

                    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                        top_left = min_loc
                    else:
                        top_left = max_loc
                    bottom_right = (top_left[0] + twidth, top_left[1] + theight)

                    # if min_val <= 0.3:
                    cv2.rectangle(img, top_left, bottom_right, 255, 2)
                    
                    plt.subplot(hair_style_count, template_count, (i * template_count + j + 1)), plt.imshow(template, cmap = 'gray')
                    plt.title('{} [{}]'.format(file_list[j].split('.')[0], round(min_val, 1))), plt.xticks([]), plt.yticks([])

    plt.suptitle('Image Matching')
    # plt.subplots_adjust(wspace=0.8, hspace=0.8)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    _single_match()