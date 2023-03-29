import os
import shutil

ipStart = "ip"
ipArray = []
allfiles = []
for j in range(78, 81):
    for i in range(2, 255):
        ipArray.append(ipStart + str(j) + "." + str(i))
for ip in ipArray:
    source = '\\\\{}\\path'.format(ip)
    destination = '\\\\ip\\path'
    if not os.path.exists(source):
        continue
    allfiles = os.listdir(source)

for file in allfiles:
    if not os.path.exists(destination + file):
        if file.endswith(".oks"):
            shutil.move(source + file, destination + file)