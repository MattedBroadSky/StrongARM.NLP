#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re

regex ={
    # 汉字字符集（UNICODE第一平面）
    "han" : re.compile(ur"[\u4E00-\u9FD5]"),

    # ASCII英文字母（UNICODE）
    "letter" : re.compile(ur"[\u0041-\u005A\u0061-\u007A]"),

    # 数字（UNICODE）
    "number" : re.compile(ur"[\u0030-\u0039]"),

    # 希腊与希伯来语
    "greek_and_coptic" : re.compile(ur"[\u0370-\u03FF]"),

    """标点符号"""

    # 水平制表符
    "horizontal_tab" : re.compile(ur"[\u0009]"),
    # 垂直制表符
    "vertical_tab" : re.compile(ur"[\u000B]"),
    # 回车符
    "carriage_return" : re.compile(ur"[\u000D]"),
    # 换行符
    "new_line" : re.compile(ur"[\u000A]"),
    # 空格符
    "space" : re.compile(ur"[\u0020\uFEFF\u3000]"),

    # 句号
    "period" : re.compile(ur"[\u3002]"),
    # 逗号
    "comma" : re.compile(ur"[\uFF0C\u002C]"),
    # 冒号
    "colon" : re.compile(ur"[\uFF1A\u003A]"),
    # 分号
    "semi_colon" : re.compile(ur"[\uFF1B\u003B]"),
    # 省略号
    "ellipsis" : re.compile(ur"[\u2026]"),
    # 括号对
    "bracket" : re.compile(ur"[\uFF08\uFF09\u3010\u3011\u300A\u300B\)\{\}\[\]]"),
    # 感叹号
    "exclamation_mark" : re.compile(ur"[\u0021\uFF01]"),
    # 引号
    "quotation_mark" : re.compile(ur"[\u2018\u2019\u201C\u201D\u0022\u0027]"),
    # 问号
    "question_mark" : re.compile(ur"[\uFF1F\u003F]"),
    # 顿号
    "pause_mark" : re.compile(ur"[\u3001]"),
    # 横线
    "dash" : re.compile(ur"[\u2012\u2013\u2014]"),
    # 下划线
    "underline" : re.compile(ur"[\u005F]"),
    # 波浪号
    "tilde" : re.compile(ur"[\u007E\uFF5E]"),

    """数学符号"""
    # 数学字符集
    "mathmatical_operator" : re.compile(ur"[\u2200-\u22FF]"),
    # 加号
    "plus" : re.compile(ur"[\uff0B\u002B]"),
    # 减号
    "minus" : re.compile(ur"[\u002D\uFF0D]"),
    # 乘号
    "multiple" : re.compile(ur"[\u002A\uFF0A\u00D7]"),
    # 除号
    "division" : re.compile(ur"[\u002F\u00F7]"),
    # 等号
    "equal" : re.compile(ur"[\u003D]"),
    # 点
    "dot" : re.compile(ur"[\u002E\uFF0E]"),
    # 百分号
    "percent" : re.compile(ur"[\u0025\uFF05]"),
    # 大于号
    "bigger" : re.compile(ur"[\u003E]"),
    # 小于号
    "smaller" : re.compile(ur"[\u003C]"),

    # 脱字符
    "caret" : re.compile("[\^]"),

    """其他符号"""
    # 单位符号
    "unit" : re.compile(ur"[\u2103\uFF04]"),
    # 井号
    "sharp" : re.compile(ur"[\u0023\uFF03]"),
    # 垂线
    "split" : re.compile(ur"[\u007C]"),
    # 和号
    "and" : re.compile(ur"[\u0026]"),
    # 加减号
    "plus_minus" : re.compile(ur"[\u00B1]"),

}

def Exist(str):
    # 判定字符是否合法
    flag = False
    for k,v in regex.items():
        temp = v.match(str)
        if(temp is not None):
            flag = True
            break
    return flag

def Type(str):
    # 返回字符的类型
    for k,v in regex.items():
        temp = v.match(str)
        if(temp is not None):
            return k
    return None