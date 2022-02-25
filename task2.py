import random

ran=random.randint(1,30)
money=100
money=int(money)

while True:
    aa=input("请输入一个数字：")
    if aa.isdigit():
        aa=int(aa)
        if money>0:
            if aa == ran:
                print("OK")
                print("还有",money,"元")
                break
            elif aa > ran:
                print("猜大了")
                money = money - 20
                print("还有",money,"元")
            elif aa < ran:
                print("猜小了")
                money = money - 20
                print("还有",money,"元")
        else:
            print("没钱玩什么玩！")
            break
    elif aa=="Q":
        break



# i=0
# i=int(i)
#
# while i<=9:
#      if i%2!=0:
#           print(i)
#           i = i + 1
#      else:
#           i=i+1



# i=input("请输入您要输入的内容:")
# print(i)
# if i.isdigit():
#     print("输入的内容为数字")
# else:
#     print("输入的内容为字符串")



# i=0
# i=int(i)
#
# while i<=50:
#     if i%7==0 or i%10==7 or i//10==7:
#         i=i+1
#     else:
#         print(i)
#         i = i + 1