#!/usr/bin/python

import sys
import ui_cc_loader

ui_path = "../RescueGirl/Classes/UIClass/"
ccb_path = "../../sgCocosUp/RGMainUILayer/Resources/"

def get_file_text(path):
    with open(path, 'r') as r:
        data = r.read()
        r.close()
    return data


def write_file_text(path, content):
    with open(path, 'w') as w:
        w.write(content)
        w.close()


def copy_code(path, source, dist):
    hSourcePath = path + source + ".h"
    hDistPath = path + dist + ".h"
    cppSourcePath = path + source + ".cpp"
    cppDistPath = path + dist + ".cpp"
    ccbSourcePath = ccb_path + source + ".ccb"
    ccbDistPath = ccb_path + dist + ".ccb"

    hText = get_file_text(hSourcePath)
    write_file_text(hDistPath, hText.replace(source, dist))

    cppText = get_file_text(cppSourcePath)
    write_file_text(cppDistPath, cppText.replace(source, dist))

    ccbText = get_file_text(ccbSourcePath)
    write_file_text(ccbDistPath, ccbText.replace(source, dist))

    ui_cc_loader.ui_cc_loader(dist)
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "./copy_code.py SourceClassName DistClassName"
    else:
        copy_code(ui_path, sys.argv[1], sys.argv[2])
