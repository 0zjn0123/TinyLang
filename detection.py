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
    """
    从给定的代码字符串中提取所有的函数调用。
    
    参数:
    - code (str): 包含源代码的字符串。
    
    返回:
    - list of lists: 每个列表包含两个元素，第一个元素是函数名称，第二个元素是传入该函数的参数字符串。
    """
    # 正则表达式模式，用于匹配形如 'function_name(param1, param2)' 的字符串
    # 使用递归模式来处理嵌套的函数调用
    pattern = r'(\w+)\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*'
    # 查找所有符合模式的函数调用，并将它们作为列表返回
    matches = re.findall(pattern, code)
    
    # 将元组转换为列表
    results = [[function_name, parameters] for function_name, parameters in matches]
    
    return results