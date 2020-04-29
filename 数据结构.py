'''----------------------数据结构----------------------'''
list=[1,2,3,4,5]

list.append("哈哈劍")#整個添加
print(list)

list.extend("憨憨批")#分開添加
print(list)

list.insert(1,"rua")#指定位置插入
print(list)

list.remove("哈哈劍")#刪除列表中值為“哈哈劍”的第一個元素，如果沒有會報錯
print(list)

print("pop删除了：",list.pop(0))#刪除列表中的【0】位置的元素,不填写位置默认最后一个
print(list)

print("憨的位置：",list.index("憨"))#返回第一个值的索引，如果没有会报错

print("出现憨的次数：",list.count("憨"))#计数，憨在列表出现的次数

list2=[3,5,1,2,88,22,1,0.1]
list2.sort()#队列表进行排序
print(list2)

list.reverse()#倒排列表
print(list)

print(list.copy())#返回列表的复制

list.clear()#移除列表中的所有项,等同于del list[:]
print(list)

del list[:]
print(list)


#列表推导式
vec=[3,6,9,12,15]
temp=[3*x for x in vec]
print(temp)

print([[x,x**2] for x in vec])

print([x*2 for x in vec if x>6])

vec2=[2,4,6,8,10]
print([x*y for x in vec for y in vec2])


#嵌套列表解析
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
matrix3=[]
for i in range(4):
    matrix3.append([y[i] for y in matrix])
print(matrix3)


#del
'''
del可以從一個列表中依索引刪除一個元素，也可以用del語句從列表中刪除一個切割，或者清空整個列表
'''
d=[1,2,3,4,5,6]
del d[0]
print(d)

s={"a":1,"b":3,"c":3,"d":4}
for x,y in s:
    print(x,y)


