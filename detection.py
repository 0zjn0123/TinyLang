import re

# Python 内置的关键字列表
kwlist = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

def detect_keywords(code):
    """
    检测给定的代码字符串中是否包含 Python 关键字。
    
    :param code: 要检测的代码字符串
    :return: 包含关键字的列表
    """
    # 分割代码为单词列表
    words = re.findall(r'\b\w+\b', code)
    
    # 检查每个单词是否为关键字
    keywords = [word for word in words if word in kwlist]
    
    return keywords

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