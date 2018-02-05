#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re

regex ={
    # 汉字字符集（UNICODE第一平面）
    "han" : re.compile(ur"[\u4E00-\u9FD5\u3007]"),

    # 汉语拼音（UNICODE）
    "bopomofo" : re.compile(ur"[\u3100-\u312F]"),

    # 英文字母（UNICODE）
    "letter" : re.compile(ur"[\u0041-\u005A\u0061-\u007A\uFF21-\uFF3A\uFF41-\uFF5A\u249C-\u24E9]"),

    # 拉丁字母（UNICODE）
    "latin" : re.compile(ur"[\u00C0-\u024F\u1E00-\u1EFF\u0250-\u0269]"),

    # 斯拉夫字母（UNICODE）
    "cryillic" : re.compile(ur"[\u0400-\u04FF]"),

    # 日语假名字符集（UNICODE）
    "kana" : re.compile(ur"[\u3031-\u3035\u3040-\u30FA\u30FC-\u30FF\uFF66-\uFF9F]"),

    # 韩语字母字符集（UNICODE）
    "hangul" : re.compile(ur"[\u3130-\u3163\uFFA1-\uFFDC\u3165-\u318F]"),

    # 汉字类语言统一字符集扩展（UNICODE）
    "cjk_unifield_extension" : re.compile(ur"[\u3400-\u4DB5]"),

    # 数字（UNICODE）
    "number" : re.compile(ur"[\u0030-\u0039\uFF10-\uFF19\u2150-\u218F\u2460-\u249B\u24Ea-\u24FF\u2776-\u2793\u3021-\u3029\u3038-\u303A]"),

    # 希腊与希伯来语
    "greek_and_coptic" : re.compile(ur"[\u0370-\u03FF]"),

    # 控制字符
    "control" : re.compile(ur"[\u0000-\u001F\u007F-\u009F]"),

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
    "space" : re.compile(ur"[\u0020\uFEFF\u3000\uFFA0\u3164\u2000-\u200F]"),

    # 句号
    "period" : re.compile(ur"[\u3002\uFF61]"),
    # 逗号
    "comma" : re.compile(ur"[\uFF0C\u002C\uFE50]"),
    # 冒号
    "colon" : re.compile(ur"[\uFF1A\u003A\uFE30\uFE55]"),
    # 分号
    "semi_colon" : re.compile(ur"[\uFF1B\u003B\uFE54]"),
    # 省略号
    "ellipsis" : re.compile(ur"[\u2025\u2026]"),
    # 括号对
    "bracket" : re.compile(ur"[\uFF08\uFF09\u3008-\u3011\u3014-\u301B\(\)\{\}\[\]\uFF5B\uFF5D\u2768-\u2775\uFE35-\uFE44\uFE47\uFE48\uFE59-\uFE5E\uFF3B\uFF3D\uFF5F\uFF60\uFF62\uFF63]"),
    # 感叹号
    "exclamation_mark" : re.compile(ur"[\u0021\uFF01\uFE57]"),
    # 引号
    "quotation_mark" : re.compile(ur"[\u2018\u2019\u201C\u201D\u0022\u0027\uFF02\uFF07\u3003\u301D-\u301F]"),
    # 问号
    "question_mark" : re.compile(ur"[\uFF1F\u003F\uFE56]"),
    # 顿号
    "pause_mark" : re.compile(ur"[\u3001\uFE45\uFE46\uFE51\uFF64]"),
    # 横线
    "dash" : re.compile(ur"[\u2010-\u2015\uFE49-\uFE4F]"),
    # 下划线
    "underline" : re.compile(ur"[\u005F\uFE58\uFF3F\u2017]"),
    # 波浪号
    "tilde" : re.compile(ur"[\u007E\uFF5E\u301C\u3030]"),

    """数学符号"""
    # 数学字符集
    "mathmatical_operator" : re.compile(ur"[\u2200-\u22FF]"),
    # 加号
    "plus" : re.compile(ur"[\uff0B\u002B\uFE62]"),
    # 减号
    "minus" : re.compile(ur"[\u002D\uFF0D\uFE63]"),
    # 乘号
    "multiple" : re.compile(ur"[\u002A\uFF0A\u00D7\uFE61]"),
    # 除号
    "division" : re.compile(ur"[\u002F\u00F7\uFF0F]"),
    # 等号
    "equal" : re.compile(ur"[\u003D\uFF1D\uFE66]"),
    # 点
    "dot" : re.compile(ur"[\u002E\uFF0E\uFE52]"),
    # 百分号
    "percent" : re.compile(ur"[\u0025\uFF05\uFE6A\u2030\u2031]"),
    # 大于号
    "greater_than" : re.compile(ur"[\u003E\uFF1E\uFE65]"),
    # 小于号
    "less_than" : re.compile(ur"[\u003C\uFF1C\uFE64]"),

    # 脱字符
    "caret" : re.compile("[\^]"),

    """其他符号"""
    # 单位符号
    "unit" : re.compile(ur"[\u2103\uFF04\u0024\uFE69\uFFE0\uFFE1\uFFE5\uFFE6\u2032-\u2037\u00B0\u00B2\u00B3\u00A5]"),
    # 井号
    "sharp" : re.compile(ur"[\u0023\uFF03\uFE5F]"),
    # 垂线
    "split" : re.compile(ur"[\u007C\uFF5C\uFE31-\uFE34\uFFE4\uFFE8\u2016]"),
    # 和号
    "and" : re.compile(ur"[\u0026\uFF06\FE60]"),
    # 加减号
    "plus_minus" : re.compile(ur"[\u00B1]"),
    # 艾特符号
    "at" : re.compile(ur"[\u0040\uFF20\uFE6B]"),
    # 反斜杠
    "reverse_solidus" : re.compile(ur"[\u005C\u005C\uFF3C\uFE68]"),
    # 中圆点
    "middle_dot" : re.compile(ur"[\u00B7\uFF65\u30FB\u2022]"),

    # 组合图字符
    "block_element" : re.compile(ur"[\u2500-\u259F\u2300-\u23FF]"),

    # 箭头字符
    "arrow_element" : re.compile(ur"[\u2190-\u21FF\uFFE9-\uFFEC]"),

    # 集合图形字符
    "geomertic_shape" : re.compile(ur"[\u25A0-\u25FF]"),

    # 字母式符号
    "letterlike_symbol" : re.compile(ur"[\u2100-\u214F\u02B0-\u02FF]"),

    # 混杂式图标
    "miscellaneous_symbol" : re.compile(ur"[\u2600-\u26FF\u2700-\u2767\u2794-\u27BF]"),

    # 未知字符
    "unknown_symbol" : re.compile(ur"[\u3004-\u3006\u302A-\u302F\u3036\u3037\u303B-\u303F\uFFE2\uFFE3\uFFED\uFFEE\u203B\u00A8]"),

    # 私有区域
    "private_symbol" : re.compile(ur"[\uE000-\uF8FF]"),

}

def Exist(letter):
    # 判定字符是否合法
    if len(letter.encode('unicode_escape')) == 10:
        return True
    flag = False
    for k,v in regex.items():
        temp = v.match(letter)
        if(temp is not None):
            flag = True
            break            
    return flag

def Type(letter):
    # 返回字符的类型
    if len(letter.encode('unicode_escape')) == 10:
        return 'big_unicode'
    for v in regex.items():
        temp = v.match(letter)
        if(temp is not None):
            return v[1]
    return None