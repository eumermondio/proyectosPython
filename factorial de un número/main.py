num = int(input("Dime número a saber factorial: "))
for i in range(num - 1):
    num = (i + 1) * num
print(num)