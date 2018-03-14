import os
import glob
import sys


def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  
  
folerPath1 = sys.argv[1] 
#folerPath1 = '/Users/liaoyong/svn/repository/project/demo/python/fileFilter/testfolder'
filePath1 = []
fileName1 = []
dirlist(folerPath1, filePath1);
#print(filePath1)

folerPath2 = sys.argv[2]  
#folerPath2 = '/Users/liaoyong/svn/repository/project/demo/python/fileFilter/testfolder2'
filePath2 = []
fileName2 = []
dirlist(folerPath2, filePath2);
#print(filePath2)

#遍历所有文件，获取文件名称（包括后缀）
for item in filePath1:
    fileName1.append(os.path.basename(item))

for item in filePath2:
    fileName2.append(os.path.basename(item))

#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。
for item1 in fileName1:
    for item2 in fileName2:
        if item1 == item2:
            dir = filePath1[fileName1.index(item1)]
            if dir.endswith("xml"):
                continue
            print(dir);




