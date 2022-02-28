import random
print("*******************************")
print("|          毒液银行            |")
print("|          V1.0               |")
print("*******************************")
print("|           1、开户            |")
print("|           2、存钱            |")
print("|           3、取钱            |")
print("|           4、转账            |")
print("|           5、查询            |")
print("|           6、再见            |")
print("*******************************")
#bank={}
bank={16667163: {'username': '普京', 'password': '123456', 'country': '俄罗斯', 'province': '乌克兰', 'street': '乌拉', 'door': '001', 'money': 10000, 'bank_name': '屠杀银行'}}
bank_name="屠杀银行"
def user_info():
    #局部变量
    account=random.randint(10000000, 99999999)
    username=input("请输入用户名")
    password=input("请输入密码")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入你的门牌号")

    x=addbank(account,username,password,country,province,street,door)

    if x==1:
        print("添加成功,以下是您的相信信息")
        #模板
        info="""
            -------%s-------
             账号：%s
             用户名：%s
             密码：*******
             国家：%s
             省份：%s
             街道：%s
             门牌号:%s
             余额：%s
        """
        print(info %(bank_name,account,username,country,province,street,door,bank[account]["money"]))
    elif x==2:
        print("重账号")
    elif x==3:
        print("数据库满")

def addbank(account,username,password,country,province,street,door):
    #名【键】=值
    if len(bank)>=100:
        return 3
    elif account in bank:
        return 2
    else:
        bank[account]={
            "username":username,  # frank
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

def money_access():
    #局部变量
    account=int(input("请输入您要转账的账号："))
    x=addmoney(account)

    if x==1:
        print("存款成功，请确认下列信息")
        info = """
                    -------%s-------
                     存款账号：%s
                     存款账户姓名：%s
                     存款金额：%s
                """
        print(info %(bank_name,account,bank[account]["username"],bank[account]["money"]))
    elif x==2:
        print("没有此账号")
        money_access()

def addmoney(account):
    #名【键】=值
    if account in bank.keys():
        money=int(input("请输入您要存的金额："))
        bank[account]["money"] = money
        return 1
    else:
        return 2

def money_take():
    #局部变量
    account=int(input("请输入您要取款的账号："))
    password=int(input("请输入您要取款的账号密码："))
    x=delmoney(account,password)

    if x==1:
        print("取款成功，请确认下列信息")
        info = """
                    -------%s-------
                     取款账号：%s
                     取款账户姓名：%s
                     剩余金额：%s
                """
        print(info %(bank_name,account,bank[account]["username"],bank[account]["money"]))
    elif x==2:
        print("账号或密码错误请重新输入")
        money_take()

def delmoney(account,password):
    #名【键】=值
    if account in bank.keys() and password==int(bank[account]["password"]):
        money=int(input("请输入您要取的金额："))
        bank[account]["money"] = bank[account]["money"] - money
        return 1
    else:
        return 2

def money_transfer():
    #局部变量
    account=int(input("请输入您的账号："))
    password=int(input("请输入您的账号密码："))
    transfer_account=int(input("请输入您要转账的账号"))
    money = int(input("请输入您要转账的金额："))
    x=transfermoney(account,password,transfer_account,money)

    if x==0:
        print("转账成功，请确认下列信息")
        info = """
                    -------%s-------
                     转账账号：%s
                     转账账户姓名：%s
                     转账金额：%s
                """
        print(info %(bank_name,account,transfer_account,money))
    elif x==1:
        print("转账账号有误，请重新输入")
        money_transfer()
    elif x==2:
        print("账号或密码错误，请重新输入")
        money_transfer()
    elif x==3:
        print("金额不够请重新输入")
        money_transfer()

def transfermoney(account,password,transfer_account,money):
    #名【键】=值
    if not (account in bank.keys() and password==int(bank[account]["password"])):
        return 2
    elif transfer_account not in bank.keys():
        return 1
    elif money>bank[account]["money"]:
        return 3
    else:
        bank[account]["money"] = bank[account]["money"] + money
        bank[transfer_account]["money"]=bank[transfer_account]["money"]+money
        return 0

def money_transfer():
    #局部变量
    account=int(input("请输入您的账号："))
    password=int(input("请输入您的账号密码："))
    if account not in bank.keys():
        print("该用户不存在，请重新输入")
        money_transfer()
    elif int(bank[account]["password"])!=password:
        print("密码错误，请重新输入")
        money_transfer()
    else:
        print("下列为您的个人信息")
        info = """
                    -------%s-------
                     账号：%s
                     密码：%s
                     余额：%s
                     用户居住地址：%s
                     当前账户的开户行：%s
                """
        print(info %(bank[account]["bank_name"],account,password,bank[account]["money"],bank[account]["street"],bank[account]["bank_name"]))



while True:
    a = input("请选择业务")
    if a == "1":
        print("1、开户")
        user_info()
    elif a == "2":
        print("2、存钱")
        money_access()
    elif a == "3":
        print("3、取钱")
        money_take()
    elif a == "4":
        print("4、转账")
        money_transfer()
    elif a == "5":
        print("5、查询")
        money_transfer()
    elif a == "6":
        print("6、再见")
        break










