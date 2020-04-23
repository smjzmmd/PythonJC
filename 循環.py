'''-----------------while循環------------------------'''

#
num=3
# num=input("請輸入：")
while num>0:
    print(num)
    num=num-1

#無限循環
while True:
    num = num + 1
    print(num,end=",")
    if num>=200:
        break


#while ... else ...
num2=6
while num2>0:
    print("當前數字：",num2)
    num2-=1
else:
    print("數字等於0，跳出")

#如果while 循環體只有一句的話，可以和while寫同一行
num3=1
# while num>=0:print("單行")
print()
'''----------------------for循環--------------------------'''
list=["C","C++","C#","Java","Python"]
for x in list:
    print(x,end=",")


#range()函數
print();print('''連續''')
for x in range(4):
    print(x,end=",")

print();print('''區間''')

for x in range(4,8):
    print(x,end=",")

print();print('''步長''')

for x in range(0,20,5):
    print(x,end=",")
print()

#range結合len
print()
for x in range(len(list)):
    print(list[x],end=".")
print()

#continue關鍵字
n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print("含有continue的循環結束")

'''
continue與break不同
break 會跳出整個循環
continue則不會跳出整個循環，只跳過當前循環塊，執行下一次
'''

#pass  佔位語句
if 1==1:
    pass
    print("pass")




