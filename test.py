#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re
import sys

import UnicodeRegex as ur


f = open(u"D:\\Samples\\001.盘龙.txt")
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