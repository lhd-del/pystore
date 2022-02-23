

##循环遍历出所有的key
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
##遍历key和value
# for i,j in dict.items():
#     print(i,j)
##添加键值
# dict.update({"k4","v4"})
# print(dict)



# # 超市水果
# Friuts = {
#     "苹果":12.3, #水果和单价
#     "草莓":4.5,
#     "香蕉": 6.3,
#     "葡萄": 5.8,
#     "橘子": 6.4,
#     "樱桃": 15.8,
# }
# info = {
#     "小明":{
#         "fruits":{"苹果":4,"草莓":13,"香蕉":10},
#         "money":0
#     },
#     "小钢":{
#         "fruits":{"葡萄":19,"橘子":12,"樱桃":30},
#         "money":0
#     }
# }
#
# for i,j in info.items():#循环获取info,小明、小刚value
#     print(i,"买了")
#     m=j["money"]
#     for i,j in j["fruits"].items():#循环获取小明、小刚fruits中的key
#         print(i,j)
#         moneys=Friuts[i]*j
#         m=m+moneys
#     print("一共",m,"元")
#     #     j["money"]=j["money"]+i
#     # print(j["money"])
#     # for i,j in j.items():
#     #         print(i,j)


#统计数字出现次数，返回字典数据：{21:3,56:9,10:3}
# list_number=[]
# num={}
# for i in range(3):
#     list_number.append(21)
# for i in range(9):
#     list_number.append(56)
# for i in range(3):
#     list_number.append(10)
# print(list_number)
#
#
# for i in list_number:#循环统计每个数字的次数
#     b=list_number.count(i)
#     num.update({i:b})
# print("返回字典数据：",num)



##数据转换为字典方式
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# user={
#     # "刘备":{"年龄":"56","性别":"男","编号":"106","任职公司":"IBM","薪资":500,"部门编号":"50"}
# }
# message={"年龄":"","性别":"","编号":"","任职公司":"","薪资":0,"部门编号":""}
# a=0
#
# for i in range(0,4):
#     a=names[i][0]
#     for j in range(1,7):
#         b=names[i][j]
#         if j==1:
#             message["年龄"]=b
#         elif j==2:
#             message["性别"] = b
#         elif j==3:
#             message["编号"] = b
#         elif j==4:
#             message["任职公司"] = b
#         elif j==5:
#             message["薪资"] = b
#         elif j == 6:
#             message["部门编号"] = b
#     user.update({a:message})
#     message={"年龄":"","性别":"","编号":"","任职公司":"","薪资":0,"部门编号":""}
#
#
# for i in user.items():
#     print(i)


