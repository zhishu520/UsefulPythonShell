#!/usr/bin/python
#coding=utf-8

import os
import sys
import shutil

'''
解决问题：
    协议替换
'''

target = "../RescueGirl/"

def replace_file(src, target ):
    file_name = src.split(r'/')[-1]
    isFind = False
    for root, dirs, files in os.walk(target):
        for f in files:
            if(f == file_name):
                isFind = True
                fpath = root +'/'+f
                print(src + " ---> " + fpath)
                shutil.copyfile(src, fpath)

    if not isFind:
        print("没有找到文件，请手动添加 ："+file_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("后面要加publish的资源")
    else:
        f = sys.argv[1]

        if os.path.isfile(f) :
            replace_file(f, target)
        elif os.path.isdir(f) :
            for root, dirs, files in os.walk(f):
                for f in files:
                    if not f.endswith(".cpp") and not f.endswith(".h"):
                        print(f + ": 文件不是以.cpp 和 .h为扩展名")
                        continue

                    ff =  os.path.join(root,f)
                    replace_file(ff, target)
