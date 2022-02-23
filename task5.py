# import random
#
# #随机生成1000个整数;
# # 数字范围[20,100];
# # 输出所有不同的数字及其每个数字重复的次数,
# # 有能力的话升序排序打印所有数字{“数字”:”次数”}
#
# list_num=[]
# num={}
#
# for i in range(1000):#重复1000次随机20~120
#     list_num.append(random.randint(20,120))
#     for i in set(list_num):
#         num.update({i:list_num.count(i)})#统计同个数字出现次数并保存在num字典里
# print(num)



# #输出商品列表，用户输入序号，显示用户选中的商品
# goods = [{"name": "电脑", "price": 1999},
#
#          {"name": "鼠标", "price": 10},
#
#          {"name": "显示器", "price": 120},
#
#          {"name": "内存", "price": 230}, ]
#
# print("有下列商品供选择：")
# for i in range(len(goods)):
#     print(i+1,goods[i]["name"],goods[i]["price"])
# print(" ")
# while True:
#     a = input("请输入购买物品的序号：")
#     if a == "Q" or a == "q":#输入Q或q退出
#         break
#     elif a.isalnum():#判断是否为数字
#         a=int(a)
#         a = a - 1
#         if a < len(goods):
#             print(goods[a]["name"], goods[a]["price"])#输出商品名和价格
#         else:
#             print("输入有误")
#     else:
#         print("输入有误")