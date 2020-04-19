import sys

class MyNuber:
    def __iter__(self):#返回一個迭代器對象
        self.a=1
        return self

    def __next__(self):#返回下一個迭代器對象
        x=self.a
        self.a+=1
        return self

myclass=MyNuber()
myiter=iter(myclass)

for j in range(5):
    print(next(myiter),end=",")

list=['a','b','c','d','e']
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()






