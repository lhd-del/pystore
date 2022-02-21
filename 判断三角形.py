i = 1
i=int(i)
list_bian=[]

for i in range(1,4):
    d=input("请输入您的第{}条边的值：".format(i))
    d=int(d)
    list_bian.append(d)

a=list_bian[0]
b=list_bian[1]
c=list_bian[2]

if a+b>c and a+c>b and b+c>a:
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("直角三角形")
    elif a==b or a==c or b==c:
        print("等腰三角形")
    elif a==b==c:
        print("等边三角形")
    else:
        print("普通三角形")
else:
    print("不能形成三角形")