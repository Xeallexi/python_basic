#20251202 Day7
#元组
#元组不可修改 
#(, , ,)
#tuple()

#定义元组
t1 = (1,"hello",True)
t2 = tuple()
t3 = ()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

#只有一个元素的元组，最后要加 ,
t4 = ("hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")
t4 = ("hello")
print(f"t4的类型是：{type(t4)},内容是：{t4}") #未打，不是元组

#元组的嵌套
t5 = ((1,2,3),(4,5,6))
t4 = ("hello",)
print(f"t5的类型是：{type(t5)},内容是：{t5}")

#下表引索取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是{num}")

#index
t6 = ("hi","hello",True)
index = t6.index("hi")
print(f"在元组t6中查找hi的下表是{index}")

#count
t7 = ("hi","hi","hi","hello",True)
num = t7.count("hi")
print(f"在元组t7中查找hi的数量是{num}")

#len
t8 = ("hi","hi","hi","hello",True)
num = len(t8)
print(f"在元组t8中查找的数量是{num}")

#遍历
index = 0
while index<len(t8):
     print(f"元组的元素有：{t8[index]}")
     index += 1

for element in t8:
     print(f"元组的元素有{element}")

#修改元组
#t8[1] = "hii" 元组不可修改



#字符串str
#字符串不能修改 #'str' object does not support item assignment
my_str = "xeallex"
#通过下表引索取值
print(my_str[2]) #从字符串取下标为2
print(my_str[-5])
#index方法
print(my_str.index("al"))
#replace方法 得到一个新字符串
print(my_str.replace("x","ee")) #eeealleee
#split方法 字符串的分割，将字符串化为多个字符串，并存入列表
print(my_str.split("e")) #x all x
print(type(my_str.split("e"))) #list
#strip 字符串的规整
#不传参数会消除前后空格
my_str = " xeallex "
print(my_str.strip())
my_str = "12xeallex21" #去除字符串1 和 2
print(my_str.strip("123"))
#count
my_str = "xeallex"
print(my_str.count("x"))
#统计字符串长度 len()
num = len(my_str)
print(num)



#数据容器的切片
#序列[起始下标:结束下标:步长]
#起始留空从头开始 结束留空默认取到结尾 
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(f"结果1{result1}")
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[::1]
print(f"结果2{result2}")
new_str = "Xeallex"
result3 = new_str[::2]
print(f"结果3{result3}")


#set 集合 不支持元素的重复 内容无序
my_set = {"x","e","a","x"}
my_set_emphty = set()
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
#因为无序，无法支持下标索引
#允许修改
#添加新元素 add
my_set.add("ss")
my_set.add("x")
print(f"my_set添加元素后的结果是：{my_set}")
#移除元素 remove
my_set = {"x","e","a","x"}
my_set.remove("x")
print(f"移除的元素后：{my_set}")
#随机取出 pop
my_set = {"x","e","a","x"}
pop = my_set.pop()
print(f"集合被取出元素是{pop}，取出之后{my_set}")
#清空集合 clear
my_set = {"x","e","a","x"}
new_set = my_set.clear()
print(f"集合被清空{new_set}")
#取差集 集合1有集合2没有的 
#difference不会改变集合12 的内容
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出的差集是{set3}")
#difference_update
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference_update(set2)
print(f"取出的差集是{set3}")#原地修改” 方法，不会返回新集合 显示none
print(set1)
print(set2)
#union 合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"合并的结果是{set3}")
#统计数量 len
set4 = {1,2,3,4,5,1,2,1,3}
num = len(set4)
print(f"集合内的元素数量是{num}")
#集合的遍历
for i in set4:
     print(i)



#字典 dict
#通过key找到value
#定义字典
my_dict = {"z":20,"m":30,"x":40}
#定义空字典
my_dict_empty = dict()
print(f"字典的元素{my_dict},类型是{type(my_dict)}")
print(f"字典的元素{my_dict_empty}")
#定义重复key 只会保留后一个key
my_dict = {"z":20,"z":30,"x":40}
print(f"字典的元素{my_dict},类型是{type(my_dict)}")

#唯一可用的索引是key 通过key找value
my_dict = {"z":20,"m":30,"x":40}
score = my_dict["m"]
print(score)
#字典的嵌套 
stu_dict = {"z":{
     "语文":77,
     "数学":66,
     "英语":33,},
     "m":{
     "语文":88,
     "数学":86,
     "英语":55,}
     ,"x":{
     "语文":99,
     "数学":96,
     "英语":66,}}
score = stu_dict["z"]["语文"]
print(f"z的语文成绩是{score}")
#字典的常用操作
#新增元素
new_dict = {"x":10,"e":20,"a":30}
new_dict.update({"l":"40","f":"50"})
print(f"字典通过新增后的结果{new_dict}")
#更新元素
new_dict["x"] = 22
print(f"字典通过更新后的结果{new_dict}")
#dict.pop(key)
re = new_dict.pop("x")
print(f"字典移除元素后字典结果是{new_dict}，移除的是{re}")
#dict.clear()
#获得全部key dict.keys()
keys = new_dict.keys()
print(f"字典的全部key{keys}")
#遍历
for key in keys: #第二种直接把keys改成new_dict
     print(f"字典的key是：{key}")
     print(f"字典的value值是：{new_dict[key]}")
#len元素数量

#sorted可以把容器进行排序
str = "sbuiow"
print(f"字符串排序后的结果是：{sorted(str)}")
#reverse进行反转
str = "sbuiow"
print(f"字符串排序后的结果是：{sorted(str,reverse=True)}")
#遍历
item_dict = {"a":10,"b":20,"c":30}
for user,score in item_dict.items():
     print(f"{user}考了{score}分")

