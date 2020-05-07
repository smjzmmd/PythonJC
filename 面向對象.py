'''---------------面向對象-------------'''

'''类对象'''
class MyClass:
    #成员变量
    i=123456
    j=0
    #构造方法
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print("self::{}".format(self))
    def f(self):
        print("MyClass，参数：",self.i)
        print("再调用类，参数：",MyClass.i)

x=MyClass(1,2)#实例化，要加括号
x.f()
print(x.i,"----",x.j)

'''self 表示类的实例，而非类'''
#类的方法与普通函数只有一个特别的区别。    他们必须有一个额外的第一个参数名称，按照惯例它的名称是self

'''类的方法'''
#在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数slef，且为第一个参数，self代表的是类的实例
class people:
    name=""
    age=0
    __weight=0#定义一个私有属性，只有在类的内部才能访问

    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.__weight=weight
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name,self.age))
        print("{}说：我{}岁。".format(self.name,self.age))

pep=people("狗子",10,20)
pep.speak()

'''继承'''
#
class student(people):
    grade=""
    def __init__(self,name,age,weight,grade):
        people.__init__(self,name,age,weight)#调用父类构造方法
        self.grade=grade
    #重写父类方法
    def speak(self):
        print("{0}说: 我{1}岁了，我在读{2}年级".format(self.name,self.age,self.grade))
    def __addd(self):
        print()
stus=student("大红",10,90,2)
stus.speak()

'''多继承'''
#需要注意括号内的父类顺序，当父类有同名方法的时候，子类未指定，将从左到右搜索，即方法在子类中未找到时，将从左到右查找父类中的方法

'''方法重写'''

'''类属性 与 方法'''
#私有属性 ： 两个下划线开头，声明私有属性，不能被外界访问，内部访问则调用self.私有方法名
#类的方法 ： 类的内部，使用 def 来定义一个方法，与一般函数不同，类方法必须包含self，且为第一个参数，self代表的是类的实例。   self 的名字也不是定死的，也可以使用this，但是 最好还是按照约定使用self
#类的私有方法 ： 两个下划线开头，声明私有方法，只能在类的内部调用，不能在类的外部调用




