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

