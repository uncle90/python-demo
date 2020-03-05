'''
[菜鸟  ] https://m.runoob.com/python3/python3-class.html
[廖雪峰] https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408
'''

################  01 ################
# class Student1:
#     pass
#
# stu = Student1()
# stu.name = 'Mr Li'


################ 02 ################
class Student(object):
    #和普通的函数相比，在类中定义的函数（类的方法）只有一点不同，就是第一个参数永远是实例变量self（惯例，可以起别名），并且调用时，不用传递该参数。
    #self指向类的实例  <__main__.Student instance  at 0x269aec96288>
    #self.class指向类  __main__.Student
    def __init__(self, n, s):
        self.name = n
        self.score = s
stu = Student('aaa',22)


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = Complex(3.0, -4.5)
# print(x.r, x.i)   # 输出结果：3.0 -4.5