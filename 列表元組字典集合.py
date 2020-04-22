list=[ ]    #列表
tup=( )     #元組
dict={ }    #字典
parame=set  #集合
'''-------------------列表---------------------------'''
list1=["google","裂開","hello","python","@@","/*****/","-----++++++"]#列表

#訪問列表中的元素
print("list1[1]:",list1[1])
print("list1[1:3]:",list1[1:3])
print("list1[1][1:2]:",list1[1][1:2]);print()

#修改list列表指定位置的數據
print("list[4]的值：",list1[4])
list1[4]="我改"
print("修改完後list[4]：",list1[4]);print()

#刪除list1中的某個元素
list2=["a","b","c","d"]
print("原始數據：",list2)
del list2[len(list2)-1]
print("刪除後：",list2);print()


#列表操作     (與字符串操作類似)
print("以下是列表方法測試：")
print([1,1]+[2,2])#拼接
print(len(list1))#長度
print(["hello"]*4,end=" ");print()#重複
for x2 in list1:#迭代
    print(x2,end=",")
print()
print(list1[2:])#輸出第三個和之後的元素
list3=[]
list3.append(3)
list3.append(2)
print(list3)


'''-------------------元組----------------------------'''
tuple1=()#空元組
#當元組只有一個元素時，需要加上逗號
tuple2=(10)
tuple3=(10,)
print(type(tuple2),type(tuple3))

#元組的訪問和列表的一樣

#修改： 元組的元素是不允許修改的，但是可以進行拼接
tuple4=(22,112)
tuple5=("aa",55)
tup=tuple4+tuple5
print(tup)

#刪除：元組元素無法修改，使用也無法刪除，不過可以刪除整個元組
del tup
# print(tup)

print("元組tup已刪除:");print('''
Traceback (most recent call last):
  File "F:/Python Project/基礎/列表元組字典集合.py", line 56, in <module>
    print(tup)
NameError: name 'tup' is not defined''')

'''-----------------------字典---------------------------'''
dict1={"a":"我是A","b":"我是B"}#類似java的map ， 它以 鍵值對的方式儲存

#訪問 使用 dict的 key 來獲得 value
print(dict1["a"]);print()

#修改
#增加、修改
dict1["c"]="我是新加C"
dict1["b"]="我是改過的B"
print(dict1);print()

#刪除
del dict1["a"]  #刪除 a 元素
print("刪除字典dict1中的a：",dict1)
dict1.clear()   #清空 字典 dict1
print("清空字典dict1：",dict1)
# del dict1       #刪除字典
print("刪除字典dict1：",
      '''
Traceback (most recent call last):
  File "F:/Python Project/基礎/列表元組字典集合.py", line 82, in <module>
    print("刪除字典dict1：",dict1)
NameError: name 'dict1' is not defined
      ''')

'''
@字典特性
python中，
1、字典的key是唯一的，如果相同的key出現第二個則會將之前的代替
2、鍵 必須是是不可變的，使用可以是數字、字符串、元組，但是列表不行
3、值 可以是任何對象
'''
tuple6=(1,3)
dict2={tuple6:"居然可以這樣",2:2}
print(dict2[tuple6]);print()

'''*-----------------------------------------集合---------------------------'''
#創建：創建空集合必須用set（）來創建 ， 而不是用 { } ，因為{}是用來創建 空字典 的
parame1={2,3,4,5,6,7}
parame2=set()
print(parame1,parame2)

#添加
parame2.add("憨批")#當成整體添加
parame2.update("憨批")#拆開添加
print(parame2)

#移除元素
parame2.remove("憨")#如果不存在會報錯
print(parame2)
parame2.discard("憨")#也是刪除元素，元素不存在不會報錯
print(parame2)

parame2.update("一二三四")
parame2.pop()#隨機刪除
print(parame2)




