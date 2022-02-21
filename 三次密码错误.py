import time

i=0
i=int(i)
username="root"
password="admin"

while i<3:
    a = input("请输入用户名：")
    b = input("请输入用户密码：")
    if a != username and b != password:
        print("用户名或密码错误")
        i=i+1
print("三次密码输入错误，请60秒后重新输入")
time.sleep(60)