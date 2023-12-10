import os

data=os.popen("df -h").readlines()
for line in data:
    line=line.split()
    if line[-1]=="/":
        print(line[-4])
        print(type(line[-4]))
