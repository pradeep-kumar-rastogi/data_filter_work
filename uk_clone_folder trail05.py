import os
name = "nextgenesolutions.com"
folder_path = r"D:\Pk\commit_uk\uk\vendor"
for file in folder_path:
    if ".php" in file:
        print(file)
for root, dirs, files in os.walk(folder_path):
    print(str(root)+" "+str(dirs)+" "+str(files))
    print(root)
    if name in folder_path:
        print(name, 'Found In File')
        print(files)
    else:
        print(name, 'Not Found')

# import os
# def listdir(dir):
#     filename = os.listdir(dir)
#     for filenames in filename:
#         print("filenames:--", filenames)
#         # print("folderPath:", os.path.abspath(os.path.join(dir, filenames)), sep="\n")
#         if '.php' in filenames:
#             print(filenames)
#             file = open(filenames, "r")
#
#             readfile = file.read()
#
#             if name in readfile:
#                 print(name, 'Found In File')
#                 print(filenames)
#             else:
#                 print(name, 'Not Found')
#
#
# if __name__ == "__main__":
#     listdir(folder_path)
