'''
    1、类的Mixin设计模式
        - Mixin类实现多重继承要遵循的规范：
            - 责任明确：必须表示某一种功能，而不是某个物品；
            - 功能单一：若有多个功能，那就写多个Mixin类；
            - 绝对独立：不能依赖于子类的实现；子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。
'''
# 交通工具类
class Vehicle(object):
    pass

# 飞行只是飞机做为交通工具的一种（增强）属性，
# 可以为这个飞行的功能单独定义一个（增强）类，称之为 Mixin 类
class PlaneMixin(object):
    def fly(self):
        print('I am flying')

class Airplane(Vehicle, PlaneMixin):
    pass

class Car(Vehicle):
    pass