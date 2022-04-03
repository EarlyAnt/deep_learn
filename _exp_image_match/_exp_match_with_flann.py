import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import walk
from os.path import join

dir_this = os.path.dirname(__file__)
dir_hair = '{}/Version 1.0'.format(dir_this)
# print('->root path: %s' % dir_this)

def create_descriptors(folder):
    sub_folder_list = sorted(os.listdir(dir_hair))
    for i in range(len(sub_folder_list)):
        sub_folder = sub_folder_list[i]
        if not (sub_folder.startswith('.')):
            sub_folder = '{}/{}'.format(dir_hair, sub_folder)
            # print('->sub_folder: %s' % sub_folder)
            
            file_list = sorted(os.listdir(sub_folder))
            for j in range(len(file_list)):
                file = '{}/{}'.format(sub_folder, file_list[j])
                # print('->file: %s/%s' % (sub_folder, file))
                
                if '.jpg' in file or '.png' in file or '.jpeg' in file:
                    save_descriptor(sub_folder, file, cv2.SIFT_create())

def save_descriptor(folder, image_path, feature_detector):
    # 检查npy文件的目录是否存在
    npy_folder = folder + '_npy'
    if not os.path.exists(npy_folder):
        os.mkdir(npy_folder)
        
    # 判断图片是否为npy格式
    if image_path.endswith("npy"):
        return
    
    descriptor_file = image_path.replace('jpg', 'npy').replace('jpeg', 'npy').replace(folder, npy_folder)
    if os.path.exists(descriptor_file):
        print('->npy file %s existed' % descriptor_file)
        return

    # 读取图片并检查特征
    img = cv2.imread(join(folder, image_path), 0)
    keypoints, descriptors = feature_detector.detectAndCompute(img, None)
    # 设置文件名并将特征数据保存到npy文件
    np.save(join(folder, descriptor_file), descriptors)
    
def match_image_each_group():
    sub_folder_list = sorted(os.listdir(dir_hair))
    for i in range(len(sub_folder_list)):
        sub_folder = sub_folder_list[i]
        if not sub_folder.startswith('.') and not sub_folder.__contains__('_npy'):
            sub_folder = '{}/{}'.format(dir_hair, sub_folder)
            # print('->sub_folder: %s' % sub_folder)
            
            image_file_list = sorted(os.listdir(sub_folder))
            image_file = '{}/{}'.format(sub_folder, image_file_list[0])
            query = cv2.imread(image_file, 0)
            print('->image file: %s' % image_file)

            descriptors = []
            npy_folder = sub_folder + '_npy'
            npy_file_list = sorted(os.listdir(npy_folder))
            for j in range(len(npy_file_list)):
                file = '{}/{}'.format(npy_folder, npy_file_list[j])
                # print('->file: %s/%s' % (npy_folder, file))
                
                # 获取特征数据文件名
                if '.npy' in file:
                    descriptors.append(file)

            # 使用SIFT算法检查图像的关键点和描述符
            sift = cv2.SIFT_create()
            query_kp, query_ds = sift.detectAndCompute(query, None)

            # 创建FLANN匹配器
            index_params = dict(algorithm=0, trees=5)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)

            potential_culprits = {}
            for d in descriptors:
                # 将图像query与特征数据文件的数据进行匹配
                matches = flann.knnMatch(query_ds, np.load(d), k=2)
                # 清除错误匹配
                good = []
                for m, n in matches:
                    if m.distance < 0.7 * n.distance:
                        good.append(m)
                # 输出每张图片与目标图片的匹配数目
                print("img is %s ! matching rate is (%d)" % (d, len(good)))
                potential_culprits[d] = len(good)

            # 获取最多匹配数目的图片
            max_matches = None
            potential_suspect = None
            for culprit, matches in potential_culprits.items():
                if max_matches == None or matches > max_matches:
                    max_matches = matches
                    potential_suspect = culprit

            print("potential suspect is %s \n" % potential_suspect)
    
def match_image_all_group():
    sub_folder_list = sorted(os.listdir(dir_hair))
    image_file = '{}/01/001.jpg'.format(dir_hair)
    query = cv2.imread(image_file, 0)
    print('->image file: %s' % image_file)
    for i in range(len(sub_folder_list)):
        sub_folder = sub_folder_list[i]
        if not sub_folder.startswith('.') and not sub_folder.__contains__('_npy'):
            sub_folder = '{}/{}'.format(dir_hair, sub_folder)
            # print('->sub_folder: %s' % sub_folder)
            
            # image_file_list = sorted(os.listdir(sub_folder))
            # image_file = '{}/{}'.format(sub_folder, image_file_list[0])
            # query = cv2.imread(image_file, 0)
            # print('->image file: %s' % image_file)

            descriptors = []
            npy_folder = sub_folder + '_npy'
            npy_file_list = sorted(os.listdir(npy_folder))
            for j in range(len(npy_file_list)):
                file = '{}/{}'.format(npy_folder, npy_file_list[j])
                # print('->file: %s/%s' % (npy_folder, file))
                
                # 获取特征数据文件名
                if '.npy' in file:
                    descriptors.append(file)

            # 使用SIFT算法检查图像的关键点和描述符
            sift = cv2.SIFT_create()
            query_kp, query_ds = sift.detectAndCompute(query, None)

            # 创建FLANN匹配器
            index_params = dict(algorithm=0, trees=5)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)

            potential_culprits = {}
            for d in descriptors:
                # 将图像query与特征数据文件的数据进行匹配
                other_ds = np.load(d)
                matches = flann.knnMatch(query_ds, other_ds, k=2)
                # 清除错误匹配
                good = []
                for m, n in matches:
                    if m.distance < 0.7 * n.distance:
                        good.append(m)
                # 输出每张图片与目标图片的匹配数目
                print("img is %s ! matching rate is (%d)" % (d, len(good)))
                potential_culprits[d] = len(good)

            # 获取最多匹配数目的图片
            max_matches = None
            potential_suspect = None
            for culprit, matches in potential_culprits.items():
                if max_matches == None or matches > max_matches:
                    max_matches = matches
                    potential_suspect = culprit

            print("potential suspect is %s \n" % potential_suspect)
    
def _open_npy_file():
    data = np.load('{}/Version 1.0/01/001.npy'.format(dir_this))
    print(data)

def _clear_invalid_file():
    sub_folder_list = sorted(os.listdir(dir_hair))
    for i in range(len(sub_folder_list)):
        sub_folder = sub_folder_list[i]
        if not (sub_folder.startswith('.')):
            sub_folder = '{}/{}'.format(dir_hair, sub_folder)
            # print('->sub_folder: %s' % sub_folder)
            if sub_folder.__contains__('DS_Store'):
                    print('->remove invalid folder')
                    os.remove(sub_folder)
            
            file_list = sorted(os.listdir(sub_folder))
            for j in range(len(file_list)):
                file = '{}/{}'.format(sub_folder, file_list[j])
                # print('->file: %s/%s' % (sub_folder, file))
                if file.__contains__('DS_Store'):
                    print('->remove invalid file')
                    os.remove(file)

if __name__=='__main__':
    # # 查看图片特征数据
    # _open_npy_file()
    
    # # 清楚无效文件
    # _clear_invalid_file()
    
    # # 保存图片特征数据
    # create_descriptors(dir_hair)
    
    # # 匹配图像(每组图片之间的匹配)
    # match_image_each_group()
    
    # 匹配图像(某张图片与所有图片的匹配)
    match_image_all_group();




''' 参考资料
1.Python 使用Opencv实现图像特征检测与匹配
https://blog.csdn.net/HuangZhang_123/article/details/80660688


'''