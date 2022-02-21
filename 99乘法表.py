a=0
b=1

while a<9:
    a = a + 1
    while b<10:
        print(b, "*", a, "=", a * b, end="\t")
        b = b + 1
    print(" ")
    if b>9:
        b=1

