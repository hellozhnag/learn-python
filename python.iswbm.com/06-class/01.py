'''
    1、定义类
        - 是具有相同特性（属性）和行为（方法）的对象（实例）的抽象模板
'''
# 这三种定义类名写法都可以
# class Animal(object):
# class Animal():
class Animal:
    age=0
    # 构造函数
    def __init__(self,name):
        self.name=name

    def run(self):
        print(f"{self.name} is running.")

'''
    2、实例化
'''
dog = Animal(name='dog')

'''
    3、方法的调用
'''
print(dog.name) # dog
# 对象.方法名
dog.run() # dog is running.
# 类.方法名(实例对象)
Animal.run(dog) # dog is running.