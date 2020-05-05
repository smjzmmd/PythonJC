'''------------------------------輸入輸出----------------'''
for x in range(1,5):
    print(repr(x).rjust(5),str(x*x).rjust(9))

'''
str（） ：函數返回一個用戶易讀的表達形式
repr（）：產生一個解釋器易讀的表達形式
rjust（n）：先在左邊填充n個空格
'''

#zfill(x)  :  zfill()會在數字的左邊填充  x個0,
print("12".zfill(4))
print("gou".zfill(2))

#format() : 括號及其裡面的字符（稱為格式化字段），將會被format（）中的闡述替換
print('{}網址："{}!"'.format('菜鳥教程','www.runoob.com'))
print("{1}{3}{2}{0}{2}".format("我不猜","hha","。","猜猜我是誰"))
print("網站名：{name}，網址：{site}".format(name="百度",site="www.baidu.com"))

'''
!a  :   ascii()的簡寫
!s  :   str()的簡寫
!r  :   repr()簡寫
'''
import math
print('常量PI的值近似為：{}'.format(math.pi))
print('常量PI的值近似為：{!r}'.format(math.pi))

# 可选项 : 和格式标识符可以跟着字段名，对值进行格式化
print("对PI进行格式化：{0:.3f}".format(math.pi))

# 在 : 传入一个整数，可以在左边填充 个的空格
print("填充空格：{0:30}".format(math.pi))

#传入字典
table={'google':1,'runoob':2,'taobao':3}
print('runoob:{0[runoob]:d};google:{0[google]:d};taobao:{0[taobao]:d}'.format(table))
#也可以通过在table变量前使用**来实现相同的功能
print('taoao:{taobao}---google:{google}---runoob:{runoob}'.format(**table))

# 旧版的python使用 % 来格式化字符串。它将左边的阐述作为类似sprintf()式的格式化字符串，而将右边的代入，然后返回格式化后的字符串
print('常量PI的值近似为：%5.3f'%math.pi)


'''----------------------input--------------'''

print("输入了-:{}".format(input("请输入:")))

