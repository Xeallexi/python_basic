#20251203 Day8
#文件编码 记录了内容和二进制之间的转换 默认UTF-8

#文件 长久保留数据
#文件的读取
# 使用open函数 打开一个已经存在的文件或创界一个新文件
#open(name,mode,encoding)
# neme : 打开目标文件名的字符串
# mode : 设置打开文件的模式 r只读 w写入 a追加
# encoding : UTF-8
f = open("D:/tset.txt","r",encoding="UTF-8")
print(type(f))

#读取文件 -read()
#print(f"读取10个字节的结果是：{f.read(10)}")
#print(f"read方法读取全部结果是{f.read()}")#会接着上一个read继续

#readlines读取全部行，封装到列表中
#print(f"readlines方法读取全部结果是{f.readlines()}")#会接着上一个read继续

#readline 一次只读取一行
#print(f"readline方法读取全部结果是{f.readline()}")
#print(f"readline方法读取全部结果是{f.readline()}")

#close 关闭文件
#f.close()

#withopen 自带close with open() as f

#文件的写出
f1 = open("D:/tset2.txt","w",encoding="UTF-8")
f1.write("hello")
#f1.flush #只有flush后才会写入文件 close内置flush
f1.close
#再用一次write会直接覆盖原先的内容，若不存在该文件则创建一个新文件

#文件的追加 a模式会在文件不存在时创建文件，文件存在时会在和最后追加写入文件
f2 = open("D:/tset3.txt","a",encoding="UTF-8")
f2.write("hi")
f2.close()



#json
import json
data = [{"name":"张","age":11},{"name":"茗","age":12},{"name":"曦","age":13}]
json_str = json.dumps(data,ensure_ascii=False) #若是英文不需要加ensure_ascii
print(json_str)
str1 = '[{"name":"张","age":11},{"name":"茗","age":12},{"name":"曦","age":13}]'
l = json.loads(str1)
print(l)#将别人的字符串转换为新字典

