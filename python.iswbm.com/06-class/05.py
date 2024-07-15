'''
    1、类的继承
        - 被继承的类称为基类（也叫做父类），继承而得的类叫派生类（也叫子类）
        - 单继承、多继承
        - MRO算法
            - mro 查询
            - merge 推导
'''
class People:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is {self.age} years old")

'''
    单继承
'''
class Student(People):
    def __init__(self, name, age, weight,grade):
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 子可以访问父的所有属性和方法
    # 子可对父方法重写
    def speak(self):
        print(f"{self.name} is {self.age} years old，在读{self.grade}")

xm=Student(name="小明",age=10,weight=50,grade="三年级")
xm.speak() # 小明 is 10 years old，在读三年级

'''
    多继承
        - 多继承的顺序使用的是从左向右再深度优先的原则。
'''
class D:
    def run(self):
        print("D run")
class C(D):pass

class B(C):
    def show(self):
        print("i am B")

class G:pass
class F(G):pass

class E(F):
    def show(self):
        print("i am E")

    def run(self):
        print("E run")

# 先继承了B
class A(B, E):pass
'''
    继承关系为：   ->B-->C-->D
                /
               A
                \
                 ->E-->F-->G
    B、E 都有show方法
    D、E 都有run方法
    
    继承顺序为 A - B - C - D - E - F - G
'''
a=A()
a.show() # i am B
a.run() # D run

'''
    MRO查询
    - 若继承关系为     ->B1-
                    /      \
                  D1         ->A1
                    \      /
                     ->C1-
        菱形继承，继承关系复杂
'''
class A1(object):pass
class B1(A1):pass
class C1(A1):pass
class D1(B1, C1):pass

import inspect
print(inspect.getmro(D1))
# (<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.C1'>, <class '__main__.A1'>, <class 'object'>)
# 可见继承关系为：D1 B1 C1 A1 object

'''
    merge推导
        - 略
'''
