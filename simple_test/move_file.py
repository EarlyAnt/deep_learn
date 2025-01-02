import os
import shutil

rootPath = os.getcwd()
imagePath = os.getcwd() + '/image' #待处理文件夹路径


# for i in range(0, 203):
#     if (not os.path.exists(str(i))):
#         os.makedirs(str(i))

 
fileList = os.listdir(imagePath)
fileList.sort()
i = 0
for file in fileList:
    print(file)
    
    # if i % 1000 == 0:
    #     print('make dir')
    # else:
    #     print('dir name: {}'.format(i // 1000))
        
    shutil.move(imagePath + '/' + file, rootPath + '/' + str(i // 1000))
    
    i += 1
    
print('total file count: {}'.format(i))


