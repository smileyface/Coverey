import os

types = {".py": "python", ".c": "C/C++", ".h": "C/C++", ".cpp": "C/C++", ".hpp" : "C/C++"}
ignore_list = ["__init__", ".pyc"]

def __get_files__(path):
    fileList = dict()
    for root, dirs, files in os.walk(".", topdown=False):
       for file in files:
          fileList[(os.path.join(root, file))] = dict()
       for name in dirs:
          print(os.path.join(root, name))
    return fileList

def __get_ext__(file):
   return os.path.splitext(file)[-1]

def __is_ignored__(file):
    for ignore in ignore_list:
        if ignore in file:
            print("{0} is on the ignore list".format(file))
            return True
        if not __get_ext__(file) in types.keys():
            print("{0} is not a recognized type".format(__get_ext__(file)))
            return True
    return False

def __get_name__(file):
    return file.replace("\\", ".")[2:]

def scrap_files(Location):
    file_no = 0;
    f = __get_files__(Location)
    remove_list = []
    for file in f:
        if __is_ignored__(file):
            remove_list.append(file)
            continue
        f[file]["type"] = __get_ext__(file)
        f[file]["name"] = __get_name__(file)
        f[file]["number"] = file_no
        with open(file) as fin:
            f[file]["contents"] = fin.read()
        file_no+= 1

    for file in remove_list:
        del f[file]

    return f

def test():
    scrap_files(os.path.abspath(__file__))
