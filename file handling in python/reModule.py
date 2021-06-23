import re


fh=open("jptfile.txt")
a="sushan"
for line in fh:
    if re.search(a, line):
        print(line)
    else:
        print("Sorry!!!")
