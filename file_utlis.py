
import os

def get_file_lines(path):
    f = open(path)
    return f.readlines()


def write_file_lines(path, lines):
    print path
    f = open(path, 'w+')
    f.writelines(lines)


def get_file_text(path):
    f = open(path)
    return f.read()

