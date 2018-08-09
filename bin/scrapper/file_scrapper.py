import os

types = {".py": "python", ".pyc":"python", ".c": "C/C++", ".h": "C/C++", ".cpp": "C/C++", ".hpp" : "C/C++"}
ignore_list = {".py": ["__init__"], ".pyc": ["__init__"]}

def __get_files__(path):
    fileList = dict()
    for root, dirs, files in os.walk(".", topdown=False):
       for file in files:
          fileList[(os.path.join(root, file))] = dict()
       for name in dirs:
          print(os.path.join(root, name))
    return fileList

def __get_ext__(files):
    for file in files:
        files[file]["type"] = os.path.splitext(file)[-1]
    return files

def clean_files(files):
    remove_list = []
    for file in files:
        if f in ignore_list[files[file]["type"]]:
            remove_list.append(file)
    for x in remove_list:
        del files[x]
    return files

def __get_name__(files):
    for file in files:
        files[file]["name"] = file.replace("\\", ".")[2:]
        f = files[file]["name"].split(".")[-2]
    return files



def scrap_files(Location):
    f = __get_files__(Location)
    f = __get_ext__(f)
    f = __get_name__(f)
    #f = clean_files(f) TODO: Future development (Issue #9)

def test():
    scrap_files(os.path.abspath(__file__))
