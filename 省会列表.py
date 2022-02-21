list_city=["北京","上海","广东"]
list_morecity=["石家庄","沈阳","哈尔滨","杭州","福州","济南","武汉","成都","昆明","兰州","台北","南宁","银川","太原","长春","南京","合肥","南昌","郑州","长沙","海口",'贵阳',"西安","西宁","呼和浩特","拉萨","乌鲁木齐"]
list_gdp=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
num=0
#添加城市
for i in list_morecity:
    list_city.append(i)

#移动广州
a1=list_city.index('上海')
b=list_city.pop(a1)
a2=a1+1
list_city.insert(a2,b)

print(list_city)

#计算GDP平均值
for i in list_gdp:
    num = num + i
print("gdp:",num)
print("平均值:",num/len(list_gdp))