'''
    1、类的封装
        - 私有变量和私有方法，虽然有办法访问，但是仍然不建议使用上面给出的方法直接访问，
          而应该接口统一的接口（函数入口）来对私有变量进行查看、变量，对私有方法进行调用。
'''
class Person:
    def __init__(self, name,age):
        self.name = name
        self.__age = age

    def is_adult(self):
        return self.__age>=18

xh=Person(name='小红',age=27)
print(xh.is_adult())