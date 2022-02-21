a=0
a=int(a)

for i in range(1,11):
    b=input("请输入您的第{}个数:".format(i))
    b=int(b)
    a=a+b
print("总和为",a)
