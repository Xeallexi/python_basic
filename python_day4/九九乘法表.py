#print("hello",end='')
#print("world",end='')

#print("hello\tworld")
#print("xea\tllex")
a = 1
while a<=9:
    b=1
    while b<=a:
        print(f"{b}*{a}={b*a}\t",end='')
        b += 1
    print()
    a+=1