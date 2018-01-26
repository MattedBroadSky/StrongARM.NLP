#! /usr/bin/python
# -*- coding: UTF-8 -*-


def HexStr2Unicode(Hex_Str):
    '''
    * Function:  HexStr2Unicode
    * Description：  16进制字符串转换为Unicode字符串
    * Input:  Hex_Str 16进制字符串
    * Return:  Unicde_Str Unicode字符串
    '''
    Unicde_Str = ""
    for i in range(0,len(Hex_Str)//4):
        chr(int(Hex_Str[i*4:i*4+4], 16))
        Unicde_Str += chr(int(Hex_Str[i*4:i*4+4], 16))

    return Unicde_Str


def Unicode2HexStr(Unicde_Str):  
    '''
    * Function:  Unicode2HexStr  
    * Description：  Unicode字符串转换为16进制字符串
    * Input:  Unicde_Str要转换的Unicode字符串
    * Return:  Hex_Str返回16进制字符串 
    '''  
    Hex_Str = ""  
    for i in range(0, len(Unicde_Str)):  
        Hex_Str += (hex(ord(Unicde_Str[i])).replace('0x','').zfill(4))  
    return Hex_Str  

a = 28288
b = hex(a)

print b

print unichr(int(b, base = 16))

d = "让我们荡起双桨"

print type(d)

c = d.decode('utf-8')

print type(c)

g = u'\u004b'

print g

print ''.decode('utf-8') == g

