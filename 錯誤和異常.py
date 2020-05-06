'''----------異常處理-----------'''
# while True:
#     try:
#         x=int(input("请输入数字："))
#         print(x)
#         break
#     except (ValueError,NameError,RuntimeError):
#         print("输入错误，请重新输入")


#当 except 要处理多个异常的时候，需要把要抛出的异常放在一个元组
#也可以分开写
# try:
#     print()
# except OSError:
#     print()
# except ValueError:
#     print()
# except RuntimeError:
#     print()
# except:
#     print()


# try/except...else...finally
#else : 是在 try 没有发生异常的时候执行
#finally : 不管有没有异常，最终都会执行
for x in range(0,5):
    try:
        print("++++++第",x,"次执行+++++++++")
        i=10/x
    except ZeroDivisionError:
        print("异常<<",x,"<<")
    else:
        print("正常<<",x,"<<")
    finally:
        print("++++++结 束+++++++++")


#raise 语句抛出一个指定的异常
# x=10
# if x>5:
#     raise Exception("x大于5，当前值为：{}".format(x))


#如果知道一个异常，不想去处理它，那么可以用raise语句再次把它抛出
try:
    raise NameError('裂开')
except NameError:
    print('An exception flew by!')
    # raise   #再次抛出异常

#自定义异常
#自定义异常类
class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(6)
except MyError as e:
    print("My exception occurred , value:",e.value)
    # raise

##如果一个异常在try子句里（或者except和eles子句里）被抛出，而又没有任何的except把他拦截，那么这个异常会在finally子句执行后被抛出

# with 可以在文件使用完之后，一定会正确的执行它的清理方法。不论处理过程中是否出现问题，文件总会关闭
with open("F:\\zzz\\Desktop\\软件测试视频.txt") as f:
    for x in f:
        print(x)

