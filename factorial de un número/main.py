num = 1
while num != 0:
    num = int(input("Dime número a saber factorial, 0 para salir: "))
    for i in range(num - 1):
        num = (i + 1) * num
    print(num)
