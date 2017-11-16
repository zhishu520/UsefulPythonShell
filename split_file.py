
#!/usr/bin/env python
#--*-- coding:utf-8 --*--
import os
class SplitFiles():
    def __init__(self, file_name ):
        self.file_name = file_name

    def split_file(self, line_count):
        self.line_count = line_count
        if self.file_name and os.path.exists(self.file_name):
            try:
                with open(self.file_name) as f :
                    temp_count = 0
                    temp_content = []
                    part_num = 0
                    for line in f:
                        if temp_count < self.line_count[part_num]:
                            temp_count += 1
                        else :
                            self.write_file(part_num+1, temp_content)
                            part_num += 1
                            temp_count = 1
                            temp_content = []
                        temp_content.append(line)
                    else :
                        self.write_file(part_num+1, temp_content)
            except IOError as err:
                print(err)
        else:
            print("%s is not a validate file" % self.file_name)

    def get_part_file_name(self, part_num):
        temp_path = os.path.dirname(self.file_name)
        part_file_name = temp_path
        if not os.path.exists(temp_path) :
            os.makedirs(temp_path)
        part_file_name += os.sep +  str(part_num) + ".txt"
        return part_file_name

    def write_file(self, part_num, *line_content):
        part_file_name = self.get_part_file_name(part_num)
        print(line_content)
        try :
            with open(part_file_name, "w") as part_file:
                part_file.writelines(line_content[0])
        except IOError as err:
            print(err)
if __name__ == "__main__":
    sf = SplitFiles("/Users/zhijianzhang/moxian/xxx7/data")
    sf.split_file([200,200,200,200,100,200,200,200,200,100,200,200,200,200,100,200,200,200,200,100,200,200,200,200,100])
