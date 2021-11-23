num = (int(input("Dame el número a convertir a binario ( menor de 255 ): ")))
cont = 1
for i in range(num):
    i = 2
    if num >= 1:
        num = int(num)
        resto = num % i
        num /= 2
        if resto != 0:
            print("1", end = '')
        elif cont != 1:
            print("0", end = '')
    else:
        break
    cont = cont + 1