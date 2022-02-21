list_numbers=[]
c=0
c=int(c)

for i in range(1,11):
    a=input("请输入您的第{}数字:".format(i))
    a=int(a)
    list_numbers.append(a)
    b = len(list_numbers)
for i in range(len(list_numbers)):
    c=c+list_numbers[i]
print("和为",c)
print("平均值为",c/b)
print(max(list_numbers))