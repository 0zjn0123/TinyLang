from detection import *
import os
import re
import sys

try:
    if not sys.argv[1]:
        print("TinyChatMode")

        
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





# 解释部分





kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
funlist = {'print':"printfun"}
def printfun(text):
    print(text)
def runcode(code):
    # 移除代码字符串的前后空格
    code_lstrip = code.strip()
    # 检查代码是否为空或以注释符号开头，如果是，则直接返回None
    if code_lstrip.startswith("#") or code_lstrip == "":
        return None
    # 提取代码字符串中的函数调用
    function_calls = extract_function_calls(code_lstrip)
    if function_calls:
        # 检查函数名是否在预定义的函数列表中
        if funlist.get(function_calls[0][0], False):
            # 执行对应的函数，并传入函数调用的参数
            exec(funlist[function_calls[0][0]]+"("+function_calls[0][1]+")")
    
    kwdetected = detect_keywords(code_lstrip)
    # 处理嵌套代码
    if "if" in code_lstrip or "while" in code_lstrip or "for" in code_lstrip:
        # 使用 eval 来执行嵌套代码
        try:
            exec(code_lstrip)
        except Exception as e:
            print(f"Error executing nested code: {e}")


for code in code_list:
    print(code)
    runcode(code)