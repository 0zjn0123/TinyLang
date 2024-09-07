

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


def extract_function_calls(code):
    # 正则表达式模式，用于匹配函数调用
    function_call_pattern = r"(\w+)\s*\(([^)]*)\)"

    # 查找所有匹配的函数调用
    matches = re.findall(function_call_pattern, code)

    # 解析并提取函数名称和参数
    function_calls = []
    for match in matches:
        function_name = match[0]
        params = match[1].strip()

        # 如果参数为空，则设置为空字符串
        if not params:
            params = ''

        function_calls.append((function_name, params))

    return function_calls


kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
funlist = {'print':"printfun"}
def printfun(text):
    print(text)
def runcode(code):
    code_lstrip = code.strip()
    if code_lstrip.startswith("#") or code_lstrip == "":
        return None
    # 提取函数调用
    function_calls = extract_function_calls(code_lstrip)
    if function_calls:
        if funlist.get(function_calls[0][0], False):

            exec(funlist[function_calls[0][0]]+"("+function_calls[0][1]+")")


for code in code_list:
    print(code)
    runcode(code)