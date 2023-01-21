# find nextgenesolutions  in file
Name = "nextgenesolutions.com"
file = open(r"D:\Pk\commit_uk\uk\*.php",)
readfile = file.read()
if Name in readfile:
    print(Name, 'Found In File')
else:
    print(Name, 'Not Found')
