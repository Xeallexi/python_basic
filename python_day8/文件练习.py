f = open("D:/bill.txt","r",encoding="UTF=8")
f1 = open("D:/bill2.txt","w",encoding="UTF-8")
for line in f1:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    f1.write(line)
    f1.write("\n")
f.close()
f1.close()