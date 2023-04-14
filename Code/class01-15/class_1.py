# 在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
# 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。


class Student(object):
    # __init_ 是一个特殊方法用于创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name 和 age 两个属性
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s。" % (self.name, course_name))

    def watchMovie(self):
        if self.age < 18:
            print("%s只能观看《熊出没》." % self.name)
        else:
            print("%s正在观看岛国爱情大电影." % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student("罗浩", 38)
    # 给对象发study消息
    stu1.study(" python程序设计")
    stu1.watchMovie()
    stu2 = Student("王大锤", 15)
    stu2.study("思想品德")
    stu2.watchMovie()


if __name__ == "__main__":
    main()
