a=1
num=0
n=input("请输入您要计算1~多少的阶乘和：")
n=int(n)
for j in range(1,n+1):
    for k in range(1,j+1):
        a=a*k
    num=num+a
    a=1
print(num)
