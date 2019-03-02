Rushi [3:24 PM]
import re
import os, os.path

PATH = '/Users/rushirajparmar/Desktop/'
conclusions = []
for file in os.listdir(PATH):
   #with open(os.path.join(PATH, file),encoding="utf8", errors='ignore','rb') as f:
   with open(os.path.join(PATH,file),encoding="utf8", errors='ignore') as f:
       data = f.read()

conclusion = re.search('Abstract: (.*?)([A-Z]{2,})',data,re.I | re.U)

if conclusions:
   print(conclusions.group())
   print(conclusions.group(1))
   print(conclusions.group(2))

conclusions.append(conclusion)
print(conclusions)