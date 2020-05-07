'''命名空间'''
####命名空间分三种
#   ·内置名称：Python内置的名称，比如abs、char、异常的名称等
#   ·全局名称：模块中定义的名称，记录了模块的变量，包括函数、类、其他导入的模块、模块级的变量常量
#   ·局部名称：函数、类中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量
#命名空间查找顺序：局部、全局、内置
# 生命周期 ： 取决对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束，因此，外部不能访问内部的命名空间对象

####    作用域  有4种：（查询顺序从上往下）
#局部作用域L（Local）：最内层，包含局部变量，比如一个函数/方法内部
#闭包函数外的作用域E（Enclosing）：包含了 非局部 也 非全局 的变量。比如两个函数嵌套，A里面有B，对于B来说，A的作用域就为非局部
#全局作用域G（Global）：当前脚本的最外层，比如当前模块的全局变量
#内建作用域B（Built-in）：包含了内建的变量/关键字，最后被搜索

g_count=0   #全局作用域
def outer():
    o_count=1   #闭包函数外的函数中
    def inner():
        i_count=2   #局部作用域


#dir() : 返回当前范围的变量、方法和定义的类型列表
# import builtins 的标准模块来实现
import builtins
print(dir(builtins))

#Python中，只有模块、类、函数才会引入新的作用域，如 if /elif/else/try/except/for/while等是不会引入新作用域的，使用在语句内部定义的变量，外部是可以使用的
if True:
    msg="I am form Runoob"
    pass
else:
    msg="裂开"
print(msg)

'''global和nonlocal关键字'''
num=1
def fun1():
    global num  #使用global定义
    print("内部：\n修改前：",num)
    num=2333
    print("修改后：",num)
fun1()
print("外部：",num,'\n\n')

#修改嵌套作用域中的变量则需要使用 nonlocal 关键字
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

a=10
def test(a):
    a=a+1
    print(a)
test(a)
