#! /usr/bin/python
# -*- coding: UTF-8 -*-


class DocProcessor:
    # 文章处理的类

    doc = ""
    startPoint = 0
    endPoint = 0

    splitKey1 = ('。'.decode('utf-8'), '？'.decode('utf-8'), '！'.decode('utf-8'))
    splitKey2 = ('……'.decode('utf-8'), '$'.decode('utf-8'))
    changeRowKey = ('\n'.decode('utf-8'), '\r'.decode('utf-8'))
    blankKey = (' '.decode('utf-8'), '　'.decode('utf-8'), '\t'.decode('utf-8'), '　'.decode('utf-8'))

    nopKey = blankKey + changeRowKey
    splitKey = splitKey1 + splitKey2 + nopKey + changeRowKey

    def Load(self, path="", document=""):
        """载入文档"""

        if path == "":
            if document == "":
                raise Exception("path and document are EMPTY!")
            else:
                self.doc = document
                self.docLength = len(self.doc)
        else:
            if document == "":
                f = open(path)
                self.doc = f.read()
                self.doc = self.doc.decode('gbk')
                f.close()
                self.docLength = len(self.doc)
            else:
                raise Exception("path and document are all EXIST!")

    def Sentence(self):
        while(self.endPoint < self.docLength):

            while(self.startPoint < self.docLength):
                if(self.doc[self.startPoint] not in self.nopKey):
                    break
                self.startPoint = self.startPoint + 1

            if(self.startPoint == self.docLength):
                return

            self.endPoint = self.startPoint

            while(self.endPoint < self.docLength):
                if(self.doc[self.endPoint] in self.splitKey):
                    self.endPoint = self.endPoint + 1
                    break
                self.endPoint = self.endPoint + 1
            
            yield self.doc[self.startPoint : self.endPoint]

            self.startPoint = self.endPoint

        return


docProcessor = DocProcessor()
docProcessor.Load(path=r"D:\sample.txt")
for temp in docProcessor.Sentence():
    print temp