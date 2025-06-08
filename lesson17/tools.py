from dataclasses import dataclass #註冊一個dataclass的

PI:float = 3.1415926 #

def func1(a:int, b:int) -> int:
    return a + b

@dataclass  #註冊一個dataclass的實體方法decorator, 註冊了才有name到english的功能
class Student:
    name:str
    chinese:int
    math:int
    english:int