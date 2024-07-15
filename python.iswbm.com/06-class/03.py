'''
    1、私有变量与私有方法
        - 以单个下划线开头的变量或方法仅供内部使用，但这并不是强制性的
        - 双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。
            - 也叫做名称修饰，解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
            - 使用双下划线开头的属性变量，就是一个私有变量。
'''
class Demo:
    def __init__(self):
        self.foo=11
        self._bar=22
        self.__baz=33

demo=Demo()
print(demo.foo) # 11
# print(demo.bar)# 报错，'Demo' object has no attribute 'bar'
print(demo._bar) # 22
# print(demo.__baz) # 报错 'Demo' object has no attribute '__baz'
print(dir(demo)) # ['_Demo__baz', ...... , '_bar', 'foo']
'''
    可以看到有一个名为_Demo__baz的属性。
    这就是Python解释器所做的名称修饰。
    它这样做是为了防止变量在子类中被重写。
'''
# 若要访问，在 __baz 前面加上 _类名
print(demo._Demo__baz) # 33

'''
    这个规则对方法同样适用，
    如果一个实例方法，以双下划线开头，那么这个方法就是一个私有的方法，
    不能由实例对象或者类直接调用。必须得通过 实例._类名__方法名 来调用。
'''
