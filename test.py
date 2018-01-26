
import re
import sys

from UnicodeRegex import unicode_dict as ud

def IsExist(str):
    flag = False
    for k,v in ud.items():
        temp = v.match(str)
        if(temp is not None):
            flag = True
            break
    return flag


f = open(r"D:\sample.txt")
s = f.read().decode('gbk')
f.close()

result = {}

for i in s:
    if(IsExist(i)):
        continue
    else:
        if(result.has_key(i)):
            result[i] = result[i] + 1
        else:
            result[i] = 1
            print i.encode('raw_unicode_escape'),
print "\nResult:"


for k,v in result.items():
    print k, '\t', k.encode('raw_unicode_escape'), '\t', v