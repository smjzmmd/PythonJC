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
tup1=()#空元組



