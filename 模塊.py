'''------------------模塊--------------------------------------java叫導包'''

import sys

print("命令行參數如下：")
for x in sys.argv:
    print(x)

print("\nPython路徑為：",sys.path,"\n")
'''import 模塊名'''
import support
#
support.print_func("誒嘿")    #調用模塊的方法

'''from 模塊名 import 函數名'''
# from support import print_func
#
# print_func("嘿嘿哈")

'''from 模塊名 import *'''
# from support import *
#
# print_func("裂開")

#dir(模塊名)   可以找到模塊內定義的所有名稱，以字符串的形式返回
print(dir(support))

print(dir(sys))

#如果沒有給參數的話，則會羅列出當前定義的所有名稱
print(dir())



