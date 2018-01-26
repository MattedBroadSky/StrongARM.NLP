
import re
import sys

import UnicodeRegex as ur


f = open(r"D:\sample5.txt")
s = f.read().decode('gbk')
f.close()

result = {}

for i in s:
    if(ur.Exist(i)):
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