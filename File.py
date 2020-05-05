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
while True:
    st=fil.read(1024)
    print(st)
    if st<0:
        print("+=================取文件完毕=================+")
        break

