#! usr/bin/python
# # -*- coding: UTF-8 -*-



def IsIn(source, range):

    if(type(source) != 'unicode'):
        raise Exception 'source is not a unicode!'

    if(len(range) != 2):
        raise Exception 'range error!'

    if(type(range[0]) != 'int' && type(range[1]) != 'int'):
        raise Exception 'range error!'

    if(range[0] > range[1]):
        raise Exception 'range error!'

    