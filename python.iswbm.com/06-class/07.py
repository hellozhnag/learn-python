'''
    1、类的property属性
'''
class Student(object):pass
s=Student()
# 直接赋值会存在一个问题，就是无法对属性值进行合法性较验
# 为了实现属性的合法性校验，引入 property 属性。
s.name="tom"

class Student1:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if 0<= value <=150:
            self._age = value
        else:
            raise ValueError('Age must be between 0 and 150.')

s=Student1()
# s.age=-1 # ValueError: Age must be between 0 and 150.
'''
    property ，其实是 Python 中一个内置的装饰器，
    它可以在新式类中把一个函数 改造 成属性。
        - 当读取属性值时，会进入被 property 装饰的函数。
        - 当对属性进行赋值时，会进入被 @xx.setter 装饰的函数。
        - 两个装饰器， @property在前， @xx.setter在后
'''