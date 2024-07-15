'''
    1、静态方法和类方法
        - 静态方法：staticmethod修饰的函数
        - 类方法：有classmethod装饰的函数
        - 实例方法：没有装饰器的普通函数
'''
class Animal:
    def __init__(self, name):
        self.name = name

    # 实例方法，第一个参数固定self，如果从实例调用，self参数不需要传入，
    # 如果是通过类调用，那么self要传入已经实例化的对象
    def run(self):
        print(f"{self.name} is running.")

    # 静态方法定义不需要self
    @staticmethod
    def eat():
        print("正在吃饭...")

    # 类方法，第一个参数固定是 cls，为 class 的简写，代表类本身。
    # 不管是通过实例还是类调用类方法，都不需要传入 cls 的参数。
    @classmethod
    def jump(cls,name):
        print(f"{name} is jumping.")

# 静态方法调用
dog = Animal('大黄')
dog.eat() # 正在吃饭...
Animal.eat() # 正在吃饭...

# 类方法调用
dog.jump("大黄") #大黄 is jumping.
Animal.jump("大黄") # 大黄 is jumping.

'''
    2、方法vs函数
'''
def demo_func():
    pass
print(type(demo_func)) # 普通函数：<class 'function'>
print(type(dog.run)) # 实例方法：<class 'method'>
print(type(Animal.eat)) # 静态方法：<class 'function'>
print(type(Animal.jump)) # 类方法：<class 'method'>
