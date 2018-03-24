#!/usr/bin/python
# -*- coding: utf-8 -*-  

import os
import sys
import re

reload(sys)  
sys.setdefaultencoding('utf8')  


pXiaoGuoTu = re.compile(ur'[\u4E00-\u9FA5]+\.(jpg|jpeg|png)')
pPng  = re.compile(r'\w+\.(png|jpg)')
pPlist  = re.compile(r'\w*\.plist')

pngPath = "../RescueGirl/Resources/UIResources/"
plistDictPath = "../RescueGirl/Resources/UIResources/ccbResources/";

def find_png_in_dir(png):
    for root, dirs, files in os.walk(pngPath):
        for f in files:
            if(f == png or f == f.replace(".png", ".pvr.ccz")):
                print(u"\033[0;32m%-80s  已经找到\033[0m"%(png))
                return
    print(u"\033[0;31m%-80s  没有找到\033[0m"%(png))

if __name__ == "__main__":
    path = sys.argv[1]
    content = open(path).readlines()

    for i in range(len(content)):

        # 带中文的效果图
        XGTMatch = pXiaoGuoTu.search(content[i].decode("utf-8"))
        if XGTMatch:
            print(u"\033[0;31m%-80s  没有找到\033[0m"%(XGTMatch.group()))
            continue

        match =  pPng.search(content[i])
        if match :
            result = match.group()
            if result == "grayimage.png" or result == "blackimage.png":
                continue

            plistMatch = pPlist.search(content[i-1])

            if plistMatch:
                plistResult = plistMatch.group()
                path = plistDictPath + plistResult
                plistContent = open(path).read()
                if plistContent.find(result) == -1:
                    print(u"\033[0;31m%-80s  没有找到\033[0m"%(plistResult+":"+result))
                else:
                    print(u"\033[0;32m%-80s  已经找到\033[0m"%(plistResult+":"+result))
            else :
                find_png_in_dir(result)
