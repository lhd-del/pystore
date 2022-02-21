s = input("请输入变量名：")

if s[0].isalpha() or s[0]=="_":
    for i in s[1:]:
        if not(i.isalnum() or i=="_"):
            print("变量名不合法")
            break
    else:
        print("变量名合法")
else:
    print("变量名不合法")