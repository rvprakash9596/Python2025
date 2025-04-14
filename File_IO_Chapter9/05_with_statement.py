
# f=open("File_IO_Chapter9/myFile.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this below;

with open("File_IO_Chapter9/myFile.txt") as f:
    print(f.readline())
# you don't have to explicitly close the file , it closes automatically




