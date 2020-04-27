'''----------------------------函數----------------------

#函數 以 def 開頭

#格式為:
def 函數名(參數列表):
    函數體

'''

def area(width,height):
    return "乘積是："+str(width*height)

print(area(4,6))


'''-----------------------------可變與不可變的值-----------'''

#不可變  ： String 、 元組（tuples） 、 number
#可變 ：   list 、 dict（字典）

def ChangeInt(a):
    print("開始",a)
    a=10
    print("結束",a)
b=2
ChangeInt(b)
print("外部b的值：",b)

print();print("可變")
def changeme(list1):
    list1.append([1,2,3,4,5.5])
    print("內部：")
print()

#必須參數
def minp(str):
    print(str)
minp("如果沒參數會報錯")

#關鍵字參數
#可以不制定順序
def prininp(name,age):
    print("名字：",name,";年齡：",age)
prininp("gouzi",3)
prininp(age=1,name="heih")
print()

#默認參數
def printinfo(name,animal="貓猫"):
    print("名字：",name,";動物:",animal)
printinfo("poop")

#不定長參數
'''
加了* 的參數會以元組（tuple）的形式導入，存放所有未命名的變量
當*vartuple沒有指定參數的時候，它就是一個空的元組。
'''
def funname(arg1,*vartuple):
    print("輸出：",arg1,vartuple)

funname(22,33,44,55,66)
funname(11,"aa")
funname(99)
print()

'''
加兩個*的參數會以字典的形式導入
'''
def prinsi(arg1,**vardict):
    print("輸出：")
    print(arg1)
    print(vardict)
prinsi(14,a=1,b="aa")

'''
如果 * 單獨出現的時候，必須用關鍵字傳入
'''
def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=4))

#匿名函數
temp= lambda age1,age2 : age1+age2
print("lambda函數：兩數相加的值：",temp(11,55))






