
import re

re_han_detail = re.compile(ur"[\u4E00-\u9FD5]")
re_skip_detail = re.compile("([\.0-9]+|[a-zA-Z0-9]+)")
re_han_internal = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._]+)")
re_skip_internal = re.compile("(\r\n|\s)")

re_eng = re.compile("[a-zA-Z0-9]+")
re_num = re.compile("[\.0-9]+")

re_eng1 = re.compile('^[a-zA-Z0-9]$', re.U)

a = '一二三四'.decode("utf-8")

han = re.compile(ur"[\u4E00-\u5E00]")

print han.match(a)

print re_han_detail.match(a)


tst = re.compile("[0-9]")

print tst.match('1')