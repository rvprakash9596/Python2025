# readline() : returns only single line
# readlines(): returns all lines in a list


f=open("File_IO_Chapter9/file1.txt")

# lines=f.readlines() # returns all sentence in a list
# print(lines)
# print(type(lines))



# line1=f.readline()
# print(line1,type(line1)) # returns only first line

# line2=f.readline()
# print(line2,type(line2)) # returns only second line

# line3=f.readline()
# print(line3,type(line3)) # returns only third line 

# line4=f.readline()
# print(line4,type(line4)) # returns only Fourth line 


# line5=f.readline()
# print(line5,type(line5)) # returns empty string
# f.close()


# do same task using Loop

line=open("File_IO_Chapter9/file1.txt")
while(line != ""):
    print(line)
    line=f.readline()
f.close()


