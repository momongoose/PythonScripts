import glob
import os
from pathlib import Path
import time
import re
import io

directory = str(os.getcwd())
global array
array = []


def CheckFileInFolderSvc(folder):
    pathTrl = r"path"
    os.chdir(pathTrl)
    a = ""
    print(folder)
    if len(os.listdir(folder)) > 0:
        os.chdir(folder)
        try:
            for latest_file in os.listdir(folder):
                print(latest_file)
                count = 0
                with io.open(latest_file) as file:
                    for line in (file.readlines()):
                        count +=1
                        a = line
                        if line.find("Failed to copy") != -1:
                            if line not in array:
                                array.append(line)
        except:
            print(latest_file)
            print(a)
            print(count)
            print("can't open logs")
            time.sleep(50)


if __name__ == "__main__":
    if os.path.exists("IDs.txt"):
        os.remove("IDs.txt")
    Trl = r"path"
    folder_array2 = []
    for folder in Path(Trl).glob("*"):
        if str(folder).find("bad") != -1:
            CheckFileInFolderSvc(str(folder))
    try:
        os.chdir(directory)
        f = open("IDs.txt", "a")
        for item in array:
            result = re.search("Failed to copy file 'path/(.*)-DE_.PDF' to", str(item))
            print(result.group(1))
            f.write(result.group(1) + "\n")
        time.sleep(20)
        f.close()

    except:
        print("can't write to file")
        time.sleep(50)
    finally:
        f.close()
