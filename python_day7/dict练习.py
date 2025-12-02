my_dict = {
    "a":{
        "工资":3000,
        "级别":1
    },
    "b":{
        "工资":5000,
        "级别":2
    },
    "c":{
        "工资":7000,
        "级别":3
    },
    "d":{
        "工资":4000,
        "级别":1
    },
    "e":{
        "工资":6000,
        "级别":2
    },
}
print(my_dict)
for key in my_dict:
    if my_dict[key]["级别"] == 1:
         my_dict[key]["级别"] += 1
         my_dict[key]["工资"] += 1000
print(my_dict)