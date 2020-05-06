'''---------------------File-------------'''
'''
file : 必须！！！，文件路径（相对绝对）
mode ： 可选，文件打开模式
buffering ： 设置缓冲
encoding ： 一般使用utf8
errors ： 报错级别
newline ： 区分换行符
closefd ： 传入的file的阐述类型
opener ： 
'''
fil=open(file="F:\\zzz\\Desktop\\软件测试视频.txt")
print("+=================开始读取文件=================+")
st=fil.readlines()
# for x in st:
#     print(x)
print(st)
fil.close()
print("+=================取文件完毕,關閉IO=================+")

fil2=open("F:\\zzz\\Desktop\\软件测试视频.txt","a")   # a 用於追加
print("+=================开始寫入=================+")
fil2.writelines(["\n","\n","\n","裂開","\n","\n","\n"])
fil2.close()
print("+=================寫入完成,關閉IO=================+")

