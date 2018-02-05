#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

def FileRowsCounter(filepath):
    ''''' count the number of lines when file is big '''  

    count=0  
    fp=open(filepath,"r")
    while True:
        buffer=fp.read(8*1024*1024)  
        if not buffer:  
            break  
        count+=buffer.count('\n')

    fp.close()
    return count

def QuickSort(sortList, start = -1, end = -1):
    '''quick sort to a list'''
    if start == -1:
        if end == -1:
            start = 0
            end = len(sortList) - 1

    if start < end:
        i,j = start,end

        base = sortList[i]

        while i < j:
            while (i < j) and (sortList[j] >= base):
                j = j - 1

            sortList[i] = sortList[j]

            while (i < j) and (sortList[i] <= base):
                i = i + 1
            sortList[j] = sortList[i]

        sortList[i] = base

        QuickSort(sortList, start, i - 1)
        QuickSort(sortList, j + 1, end)
    return sortList

def FileReadLine(fp, blockLength):
    result = []
    for i in range(0, blockLength):
        temp = fp.readline()
        if temp == 'EOF'
            break;
        result.append(temp)
    return result

def Process(inputFile, outputFile = '', tempPath = '', blockLength = 500000):
    '''Process Big File Sort'''

    if os.path.isfile(inputFile) == False:
        return
    
    inputFile = os.path.abspath(inputFile)

    if outputFile == '':
        outputFile == inputFile + '.output'
    if tempPath == '':
        tempPath = os.path.join(os.path.dirname(inputFile), "SortTemp")

    wfCount = 0

    os.mkdir(tempPath)

    fp = open(inputFile, 'r')

    docList = FileReadLine(fp, blockLength)

    while docList != []:
        docList = QuickSort(docList)
        wf = open(os.path.join(tempPath, 'tempFile' + str(wfCount)), 'w')
        for line in docList:
            wf.write(line + '\n')
        wf.close()
        wfCount = wfCount + 1

        docList = FileReadLine(fp, blockLength)

    fp.close()

    filePoints = []

    for filename in os.listdir(tempPath):
        c = []
        c.append(open(os.path.join(tempPath, filename)), 'r')
        c.append(c[0].readline())
        filePoints.append(c)

    wf = open(outputFile,'w')

    while(filePoints != [])

        temp = filePoints[0]

        for filePoint in filePoints:
            if filePoints[1] < temp[1]:
                temp = filePoint
        
        wf.write(temp[1] + '\n')

        temp[1] = temp[0].readline()
        if temp[1] == 'EOF':
            temp[0].close()
            filePoints.remove(temp)

    wf.close()

    print 'Done'

    return True


print QuickSort(['cde','abc','bcd'])