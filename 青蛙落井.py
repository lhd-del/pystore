jing=-20
up=3
down=2
day=1

while True:
    print("day",day)
    day=day+1
    print("剩",jing)
    jing=jing+up
    if jing>=0:
        break
    jing=jing-down
    if jing>=0:
        break
print(day,"天能出来")
