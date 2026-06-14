#opening a file - open(filename with full path,mode)
# Modes can be r(read),x(create),w(overwrite),a(append),t(textfile),b(binaryfile like image,audio,video)
#rt is the default mode or t is default

#open gives the pointer to beginning of file object
file_handler = open("practice.txt",'tr')
print(file_handler)
#Read operation
# print(file_handler.read())        #reads entire file
# print(type(file_handler.read()))  #returns a string
#print(file_handler.read(10))       #reads first 10 characters

#readline() - prints one line and go to next one
# line1 = file_handler.readline()
# line2 = file_handler.readline()
# line3 = file_handler.readline()
# line4 = file_handler.readline()
# print(f"Line1: {line1}")
# print(f"Line2: {line2}")
# print(f"Line3: {line3}") #Empty string means end of file
# print(f"Line4: {line4}")

#readlines() - gives list of all the lines
lines = file_handler.readlines()
print(lines)

for line in lines:
    print(line.strip())


#Close a file
file_handler.close()

#x mode creates new file and gives error if already file exists

#create and write into file
#w mode creates a new file if file does not exist or if exists it will delete content just after opening
fh = open("file1.txt",'wt')
fh.write("hello world\n")
fh.write("Next Line")
fh.write("\nThis is for file handling purposes.")

fh.close()
#After closing no read/write operation can be performed

#a mode also creates a new file if it doesn't exist
# otherwise it will start writing from end of file

fh1 = open("file1.txt",'at')
fh1.write("hello world\n")
fh1.write("Next Line")
fh1.write("New append")

fh1.close()

#with - handles automatic file closure
with open("practice.txt",'rt') as fh:
    contents = fh.read()
print(contents)

with open("practice1.txt",'wt') as fh:
    fh.write("hello world\n")
    fh.write("Next Line")

#To check if file exists or not
#os.path.exists()

import os
file_name = "practice.txt"
# file_name = "C:/Users/rajat/OneDrive/Desktop/Pycharm_Learn_Python/practice.txt" can also be given
if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")

#Another method to check file exists or not
#pathlib.Path.exists()

from pathlib import Path
file_name = Path("practice.txt")
# file_name = Path("C:/Users/rajat/OneDrive/Desktop/Pycharm_Learn_Python/practice.txt") can also be given
if file_name.exists():
    print("file exists")
else:
    print("file does not exist...Creating file")
    fh=open(file_name,'xt')
    fh.write("OK")
    fh.close()