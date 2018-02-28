import numpy as np
import matplotlib.pylab as plt
import os

FILTER_WIDTH = 500;

def getDirFileList(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    fileList = []
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            f = open(path+"/"+file); #打开文件
            iter_f = iter(f); #创建迭代器
            filePath = path+"/"+file;
            result = filePath.endswith("png");
            if result :
                fileList.append(filePath)
    return fileList

path = "/Users/liaoyong/svn/repository/project/demo/python/studyproject" #文件夹目录
fileList = getDirFileList(path);

for filePath in fileList:
    # 加载图像
    im = plt.imread(filePath) # 加载当前文件夹中名为BTD.jpg的图片
    if im.shape[0] > FILTER_WIDTH or im.shape[1] > FILTER_WIDTH :
        print("尺寸:" + str(im.shape) + ",path:" + filePath)
    # (4608, 2592, 3)即(y轴像素点数， x轴像素点数，图像通道数)
    # 这里用的是RGB三通道图像，通道数为3




