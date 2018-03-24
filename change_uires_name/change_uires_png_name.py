#!/usr/bin/python
#coding=utf-8

import os
import sys
import shutil
'''
解决问题：
    替换ui的图片名称
'''
class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")
        for char in string:
            key = '%X' % ord(char)
            temp = self.word_dict.get(key, char).split()[0][:-1].lower()
            if temp == None or temp == "":
                temp = char
            result.append(temp)
        return result


    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)

def rename_uires(path, lastName):
    py = PinYin()
    py.load_word()
    for root, dirs, files in os.walk(path):
        for f in files:
            print f
            if not f.endswith(".png"):
                continue
            rname = f[0:-4]
            words = py.hanzi2pinyin(rname)
            print words
            resstr = "";
            for wd in words:
                resstr  += wd.capitalize()

            print path
            print resstr + lastName + ".png"
            pathname = "/Users/zhijianzhang/test" + '/' + resstr + lastName + ".png";
            print pathname
            print os.path.join(root,f)
            shutil.move(os.path.join(root,f), pathname)
            resstr = ""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "./change_uires_png_name.py 路径 图片的后缀\n etc.\n./change_uires_png_name.py ~/sgCommon _sgCommon"
    else:
        rename_uires(sys.argv[1], sys.argv[2])
