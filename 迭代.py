'''---------------------迭代器------------------------------

迭代器有兩個基本方法:iter() 和 next()

'''
import sys

list=["C","C++","C#","Java","Python"]
for x in iter(list):        #創建迭代器對象
    print(x,end=",")


#自定義迭代器

class MyNumber:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass=MyNumber()      #實例化MyNumber類
myiter=iter(myclass)

for x in range(4):
    print(next(myiter))


#
it=iter(list)
print("開始迭代")
while True:
    try:
        print(next(it))
    except StopIteration:   #異常處理
        # sys.exit()        #退出程序
        break
print("退出迭代");print()


#生成器
def fibon():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


f=fibon()       #返回一個生成器對象

# while True:
try:
        print(next(f))
        print("!"*20)
        print(next(f))
except StopIteration:
        print("StopIteration異常")
        # break

'''
生成器
    當 f 調用fibon（）方法的時候，返回一個生成器對象
調用next（）方法的時候，進行迭代，執行print 後，進入循環，
執行yield 4 ，然後把4 return 之後停止。
    當再次調用next（）的時候，從上一次的位置繼續執行。
因為 4 在上一次操作的時候已經被return出去，所以res沒有賦到值，輸出res:None
再次執行yield 4的時候，return 4然後停止。等待下一次操作
'''
