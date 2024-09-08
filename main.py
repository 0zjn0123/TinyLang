from detection import *
import os
import re
import sys

# 读取命令行参数
try:
    if not sys.argv[1]:
        print("TinyChatMode")
        sys.exit()

    try:
        target_file = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("FileNotFound!")
        sys.exit()
except IndexError:
    print("TinyChatMode")
    sys.exit()

# 读取文件内容并分割成代码列表
code_list = re.split("\n|;", target_file.read())

# 关键字列表
kwlist = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

# 函数列表
funlist = {'print': "printfun"}

def printfun(*text):
    if len(text) == 1:
        text = str(text[0])
    elif len(text) > 1:
        text = " ".join(text)
    else:
        text = ""
    print(text)



def runcode(code,num):
    
    
    # 检查代码是否为空或以注释符号开头，如果是，则直接返回None
    if code.startswith("#") or code == "" or code.startswith(" "*4):
        return None
    
    # 提取代码字符串中的函数调用
    function_calls = extract_function_calls(code)
    if function_calls:
        # 检查函数名是否在预定义的函数列表中
        main_func_name, main_args = function_calls[0]
        if funlist.get(main_func_name, False):
            # 执行对应的函数，并传入函数调用的参数
            
            exec(f"{funlist[main_func_name]}"+"("+f"{main_args}"+")")

    elif not detect_keywords(code) and not extract_function_calls(code):
        print(f"Error executing code: {code}")
            
            
    
    # 处理嵌套代码
    long_code = code + "\n"
    if "if" in code or "while" in code or "for" in code:
        for line in range(num+1,len(code_list)):
            if code_list[line][:4] == " "*4:
                long_code += code_list[line]+"\n"
            else:
                break
        
        
        try:
            #print(long_code)
            exec(long_code)
        except Exception as e:
            print(f"Error executing nested code: {e}")

# 逐行执行代码
for code in code_list:
    print(code)
    runcode(code,code_list.index(code))