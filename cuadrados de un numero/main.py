num = int(input("Dime número a saber cuadrados: "))
limite = int(input("Dime la cantidad de cuadrados a mostrar: "))
print()
for i in range(limite):
    print(num, "\n")
    num = num * num
    