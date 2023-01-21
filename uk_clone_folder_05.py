# checking nextgen string in file of uk clone folder
import glob
import os

a = 'nextgenesolutions.com'
folder_path = glob.glob(r"D:\Pk\commit_uk\uk\vendor\*.php",)
print(len(folder_path))
for file in folder_path:
    f = open(file, 'r', encoding='utf8')
    readfile = f.read()
    if a in readfile:
        print(a, 'Found In File')
        print(file)
    else:
        print(a, 'Not Found')



















# for path in glob.glob(".php".format(folder_path),recursive=True):
# 	f = os.stat(folder_path).st_size/1024
# 	print(folder_path, f)
