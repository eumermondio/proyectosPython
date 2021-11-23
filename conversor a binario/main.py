num = (int(input("Dame el número a convertir a binario, hasta el 32767: ")))
i = pow(2,14)
while i >= 1:
    i = int(i)
    resto = num & i
    i /= 2
    if resto != 0:
        print("1", end = '')
    else:
        print("0", end = '')