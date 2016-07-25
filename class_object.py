# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:

"""


# 类的定义
class Person:  # 使用class关键词来定义类
    pass  # 占位

someone = Person()  # 创建一个类型为Person的对象


class Person:
    def __init__(self, name):  # __init__方法初始化对象，第一个参数为self且为必需
        self.name = name  # 类内部调用name属性使用 self.name

hunter = Person("xujm")  # 传递参数name
print hunter.name  # 获取对象的属性


# 继承
class Car:
    def exclaim(self):
        print "I am a Car"


class Yugo(Car):  # 基于基类Car的子类
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class Person:
    def __init__(self, name):
        self.name = name


class DRPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class TRPerson(Person):
    def __init__(self, name):
        self.name = "Teacher " + name

person = Person("xujm")
doctor = DRPerson("xujm")
teacher = TRPerson("xujm")
print person.name, doctor.name, teacher.name


class Car:
    def exclaim(self):
        print "I am a car"


class Yugo(Car):
    def exclaim(self):
        print "I am a Yugo! Much like a Car, but more Yugo-ish."

    def need_a_push(self):
        print "A little help here?"

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()


# super
class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        Person.__init__(self, name)  # Python3 super().__init__(name)
        self.email = email

xujm = EmailPerson("xujm", "xujm@realbio.cn")
print xujm.name
print xujm.email


# property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print c.radius, c.diameter
c.radius = 7
print c.diameter
c.diameter = 8
print c.diameter


# 私有成员
class Person:
    x = 1  # 静态成员

    def __init__(self, name):
        self.__name = name  # 私有成员

print Person.x  # 输出1
# print Person("xujm2").__name  # 报错


# 方法类型： 实例方法、类方法（@classmethod）、静态方法（@staticmethod）
class A:
    count = 0

    def __init__(self):
        A.count += 1  # 使用类属性

    def exclaim(self):
        print "I am an A!"

    @classmethod
    def kids(cls):  # 类方法，
        print "A has", cls.count, "little.objects"  # cls.count 也可以使用A.count

    @staticmethod
    def commercial():
        print "Copyright: xujm @ 2016"  # 静态方法，可以直接被类调用

easy_a = A()
breezy_a = A()
A.kids()  # 受所有实例化的对象的影响
A.commercial()


