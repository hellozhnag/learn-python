'''
    1、类的魔术方法
        - 通常是两个下划线包围来命名的（比如 __init__ ， __lt__ ）
'''

'''
    1.1 构造方法
        - 当初始化一个对象的时候，__init__ 并不是第一个调用的方法，第一个调用的
            方法是__new__，这个方法真正创建了实例；当对象的生命周期结束的时候，
            __del__会被调用
        - __new__(cls,[…)
            - 它只取下 cls 参数，并把其他参数传给 __init__
        - __del__(self)
            - __del__ 是对象的销毁器，但并非实现了语句 del x ，
                而是定义了当对象被垃圾回收时的行为。当对象需要在销毁时做一些处理的时候这个方法很有用，
                比如 socket 对象、文件对象。
'''
from os.path import join
class FileObject:
    def __init__(self, filepath='C:\\Users\\zhang\\Desktop',filename='sample.txt'):
        self.file=open(join(filepath,filename),'r+')

    def __del__(self):
        self.file.close()
        del self.file

FileObject()

'''
    1.2 操作符
        - 比较操作符
            - __cmp__ __eq__ __ne__ ......
        - 数值操作符
            - 一元操作符
            - 常见算数操作符
            - 反射算数操作符
            - 增强赋值操作符
            - 类型转换操作符。
'''
class Word(str):
    '''单词类，按照单词长度来定义比较行为'''

    def __new__(cls, word):
        # 注意，我们只能使用 `__new__` ，因为str是不可变类型
        # 所以我们必须提前初始化它（在实例创建时）
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]
            # Word现在包含第一个空格前的所有字母
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

w1 = Word("hello")
w2 = Word("world hh") # Value contains spaces. Truncating to first space.
print(w1>w2) #False
print(w1<w2) #False
print(w1>=w2) # True
print(w1<=w2) # True

'''
    一元操作符
'''
class Number:
    def __pos__(self):
        print("取正操作")
    def __neg__(self):
        print("取负操作")
    def __abs__(self):
        print("取绝对值")
    def __invert__(self):
        print('取反操作')
    def __round__(self,n):
        print("实现内建函数 round() ，n 是近似小数点的位数。")
    def __floor__(self):
        print("实现 math.floor() 函数，即向下取整。")
    def __ceil__(self):
        print("实现 math.ceil() 函数，即向上取整。")
    def __trunc__(self):
        print("实现 math.trunc() 函数，即截断整数")

n=Number()
+n # 取正操作
~n # 取反操作
import math
math.ceil(n) # 实现 math.ceil() 函数，即向上取整。

'''
    算数操作符
        - __sub__ __mul__ __floordiv__ __div__ __truediv__ __mod__ 
            __divmod__ __pow__ __lshift__ __rshift__ __and__ __or__ __xor__
'''
class Number1:
    def __add__(self, other):
        print("加法操作")

n1=Number1()
n1+1 # 加法操作

'''
    反射算数运算符
        - 所有反射运算符魔法方法和它们的常见版本做的工作相同，
            只不过是处理交换连个操作数之后的情况。绝大多数情况下，
            反射运算和正常顺序产生的结果是相同的，
        - __rsub__ __rmul__ __rdiv__  ......
'''
class Number2:
    def __radd__(self, other):
        print("反射加法操作")

n2=Number2()
1+n2 # 反射加法操作
# 操作符左侧的对象定义了add（radd操作符的非反射板本），radd就不会调用
n1+n2 # 加法操作

'''
    增强赋值运算符
        - 算数运算符前边加 i
        - __isub__ __imul__ __idiv__  ......
'''
class Number3:
    def __iadd__(self, other):
        print("实现加法赋值操作。")

n3=Number3()
n3+=1 # 实现加法赋值操作。

'''
    类型转换操作符
        - __long__ __float__ __complex__ __oct__ __hex__ _index__ ......
'''
class Number4:
    def __int__(self):
        print("实现到int的类型转换。")
        return 1

n4=Number4()
int(n4) # 实现到int的类型转换。

'''
    1.3 类的表示
        - 使用字符串表示
        - Python中有一些内建方法可以返回类的表示，相对应的，
            也有一系列魔法方法可以用来自定义在使用这些内建函数时类的行为。
        - __repr__ __unicode__ __format__ __hash__ __nonzero__ __dir__ ......
'''
class Number5:
    def __str__(self):
        print("定义对类的实例调用 str() 时的行为。")
        return " "

n5=Number5()
str(n5) # 定义对类的实例调用 str() 时的行为。

'''
    1.4 访问控制
'''
