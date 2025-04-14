# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

for i in range(1,21):
    if(i==15):
        break # exit the loop turant
    print(i)


for i in range(1,8):
    if(i==4):
        continue # skip this iteration turant
    print(i)
