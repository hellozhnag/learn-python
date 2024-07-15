'''
    1 、类的多态
        - python鸭子类型：一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
'''

class American():
    def speak(self):
        print("hello~")

class Chinese():
    def speak(self):
        print("你好~")

p1 =American()
p2=Chinese()

def do_speak(people):
    people.speak()

do_speak(p1) # hello~
do_speak(p2) # 你好~

'''
    传入do_speak方法的参数，只要是一个对象并且有speak方法，
    那么他就是一个 do_speak 方法所需要的 people 对象。
    
    与java的区别：
        对于JAVA，必须指定函数参数的数据类型，
        只能传递对应参数类型或其子类型的参数，不能传递其它类型的参数
'''