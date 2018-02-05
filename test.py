#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re
import sys
import os
import chardet
import time

import UnicodeRegex as ur

def RunTest(filepath):

    for filename in os.listdir(filepath):
        f = open(filepath +'\\' + filename)
        s = f.read()
        f.close()
        codes = [
            'ascii',
            'big5',
            'big5hkscs',
            'gb2312',
            'gbk',
            'gb18030',
            'utf_32',
            'utf_32_be',
            'utf_32_le',
            'utf_16',
            'utf_16_be',
            'utf_16_le',
            'utf_7',
            'utf_8',
            'utf_8_sig',
        ]
        doc = ''
        for code in codes:
            try:
                doc = s.decode(code)
            except UnicodeDecodeError:
                continue
            else:
                break
        if doc == '':
            continue

        result = {}

        for i in doc:
            if(ur.Exist(i)):
                continue
            else:
                if(result.has_key(i)):
                    result[i] = result[i] + 1
                else:
                    result[i] = 1
        
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

        for k,v in result.items():
            print "%s\t%s\t%s\t%s\t%s"%(currentTime, filename, k, k.encode('unicode_escape'), v)

def LetterRela(filepath):
    for filename in os.listdir(filepath):
        f = open(filepath +'\\' + filename)
        s = f.read()
        f.close()
        codes = [
            'ascii',
            'big5',
            'big5hkscs',
            'gb2312',
            'gbk',
            'gb18030',
            'utf_32',
            'utf_32_be',
            'utf_32_le',
            'utf_16',
            'utf_16_be',
            'utf_16_le',
            'utf_7',
            'utf_8',
            'utf_8_sig',
        ]
        doc = ''
        for code in codes:
            try:
                doc = s.decode(code)
            except UnicodeDecodeError:
                continue
            else:
                break
        if doc == '':
            continue

        result = {}

        for index,key in enumerate(doc):
            if(index == 0):
                continue
            else:
                temp = doc[index-1] + "\t" + key
                if(result.has_key(temp)):
                    result[temp] = result[temp] + 1
                else:
                    result[temp] = 1
        
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

        for k,v in result.items():
            print "%s\t%s\t%s\t%s\t%s %s"%(currentTime, filename, k, v, k[0].encode('unicode_escape'), k[2].encode('unicode_escape'))

LetterRela(u'D:\\s')