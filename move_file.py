import shutil
import os

from_dir = "C:/Users/pasup/Downloads"
to_dir = "C:/Users/pasup/Downloads/Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for traverse in list_of_files:
    name,extention = os.path.splitext(traverse)
    if extention == '':
        continue
    if extention in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + traverse
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Dcument_Files" + '/' + traverse
        if os.path.exists(path2):
            print("moving" + traverse + ".....")
            shutil.move(path1,path2)
        else:
            os.makedirs(path2)
            print("moving" + traverse + ".....")
            shutil.move(path1,path3)