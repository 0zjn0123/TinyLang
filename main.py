

import os
import re
import sys
print(sys.argv)
try:
    if not sys.argv[1]:
        print("TinyChatMode")
    elif os.path.isfile(sys.argv[1]):
        print(sys.argv[1][-3:])
        
    try:
        target_file = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("FileNotFound!")
        # 退出
        sys.exit()
except:
    print("TinyChatMode")
    sys.exit()


code_list = re.split("\n|;",target_file.read())
print(code_list)




# 解释部分
kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
funlist = {'print':"printfun"}
def printfun(text):
    print(text)
for code in code_list:
    if not code[0:] == '#':
        if code in funlist or code in kwlist:
            exec(funlist[code])