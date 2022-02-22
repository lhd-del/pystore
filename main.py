import random
#coding=utf-8
'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
            #优惠券：（冰墩墩3张8折  西瓜2张7折）随机抽取一张
            #满200 -10

'''
money=1000
shop=[
    #  0      1
    ["冰墩墩",199],#0
    ["雪蓉荣",199],#1
    ["韩国泡菜，小西巴",10],#2
    ["小日子,小八嘎",20],#3
    ["西瓜",40],#4
    ["骨癌零",999],#5
    ["葫芦小金刚",24]#6
]
preferential=[
    ["冰墩墩",0.8*shop[0][1]],
    ["冰墩墩",0.8*shop[0][1]],
    ["西瓜",0.7*shop[4][1]],
    ["西瓜",0.7*shop[4][1]],
    ["西瓜",0.7*shop[4][1]]
]
a=random.randint(1,5)
b=preferential[a]
print("获得",b[0],"优惠卷")
shop.append(b)
num=0

# 列表的长度-1就是角标的最大值
car=[]
while True:
    for i in enumerate(shop):#打印角标和值
        print(i)
    a=input("请输入商品编号")#用户选择编号
    if a.isdigit():#判断是不是数字
        a=int(a)#转换类型
        if  0<=a and a<len(shop):#判断超出范围
            car.append(shop[a])#加入购物车
            print("购物车:")
            if b == shop[a]:
                shop.remove(shop[a])
            for i in enumerate(car):  # 打印角标和值
                print(i[1])
            print("")
        else:#超出范围
            print("输入的数字,没有此商品")
    elif a=="q" or a=="Q":#结账
        print("购物车有:")
        for i in enumerate(car):  # 打印角标和值
            print(i[1])
            num=num+i[1][1]
        if money >= num:  # 钱够不够
            if num>=200:
                num=num-10
                print("满200-10，现需要支付",num)
            else:
                print("需要支付：", num, "元")
            money=money-num
            print("金额剩余:", money)
        else:  # 钱不够
            print("gun")
        break#结算完，，打印小条之后退出循环
    else:#瞎写
        print("没有此商品")














6





#
# ll=[1,2,3,4,5,1,2,3,1]
# #ll={1,2,3,4,5}
# #set={}
# # print(ll)
# # print()
#
# for i in set(ll):
#     print(i,"出现了",ll.count(i),"次")



# for i in range(10):#0,1,2,9
#     print(" "*(10-i),"* "*i)

# j=20#Σ(っ °Д °;)っ长度
# day=3#爬3米
# night=2#回落2米
# day_d=0#算天数
# while True:#
#     day_d = day_d + 1#开始跳
#     j=j-day#跳3米
#     if j<=0:#跳完算距离
#         print("跳出来",day_d)#出来
#         break
#     j=j+night#晚上回落2米
#



