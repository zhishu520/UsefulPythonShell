#!/usr/bin/python
#coding=utf-8

import os
import sys
import shutil
# sudo pip install PIL
from PIL import Image

'''
解决问题：
    大图资源的替换和添加
'''

def scaleHalf(f):
    im = Image.open(f)
    w, h = im.size
    im_ss = im.resize((int(w * 0.5), int(h * 0.5)))
    im_ss.save(f)

target = "../srcTexture"
resTarget = "../RescueGirl/Resources/UIResources"
ccbTarget = "../../sgCocosUp/RGMainUILayer/Resources/resources-auto"
defalutResPath = "../RescueGirl/Resources/UIResources/NoAlphaOpt/"

def publish_replace(src, target, isScaleHalf = False):
    file_name = src.split(r'/')[-1]
    isFind = False
    for root, dirs, files in os.walk(target):
        for f in files:
            if(f == file_name or f == file_name.replace(".png",".pvr.ccz")):
                isFind = True
                fpath = root +'/'+f
                if f == file_name.replace(".png", ".pvr.ccz"):
                    shutil.move(fpath, fpath.replace(".pvr.ccz", ".png"))
                    fpath= fpath.replace(".pvr.ccz", ".png")

                shutil.copyfile(src, fpath)
                if(isScaleHalf):
                    scaleHalf(fpath)

    if not isFind:
        if isScaleHalf:
            fpath = target + '/NoAlphaOpt/'+file_name
        else:
            fpath = target + '/'+file_name
        shutil.copyfile(src, fpath)
        if(isScaleHalf):
            scaleHalf(fpath)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("后面要加publish的资源")
    else:
        publish_replace(sys.argv[1], target, True)
        publish_replace(sys.argv[1], resTarget, True)
        publish_replace(sys.argv[1], ccbTarget)

