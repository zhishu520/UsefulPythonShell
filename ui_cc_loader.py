import os
import file_utlis

cc_h = "../RescueGirl/Classes/UIClass/CocosBuilderCardLoader.h"
cc_cpp = "../RescueGirl/Classes/UIClass/CocosBuilderLayerLoaders.cpp"

template_h_string = '\r\n#include "__ClassName.h"\r\nRG_DEFINE_CCLODER(__ClassName, LayerLoader);\r\n'
template_cpp_string = '    mNodeLoaderLibrary->registerNodeLoader("__ClassName", __ClassNameLoader::loader());\n'

__ClassName = "__ClassName"

def get_cc_loader_h(name):
    return template_h_string.replace(__ClassName, name)

def get_cc_loader_cpp(name):
    return template_cpp_string.replace(__ClassName, name)


def ui_cc_loader(name):
    h_code = get_cc_loader_h(name)
    lines = file_utlis.get_file_lines(cc_h)
    lines.insert(-3, h_code)
    file_utlis.write_file_lines(cc_h, lines)

    cpp_code = get_cc_loader_cpp(name)
    lines = file_utlis.get_file_lines(cc_cpp)
    lines.insert(-3, cpp_code)
    file_utlis.write_file_lines(cc_cpp, lines)

