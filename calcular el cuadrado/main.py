# Calcula el doble de el numero que le digas, opera con decimales

x = float(input("Escribe un número y te daré su cuadrado: "))
if x == 0:
        print("El cero no vale, cualquier numero por cero siempre va a ser cero")
elif x <= 0:
        print("Tu numero es bajo cero", x**2 )
elif x > 0:
        print("El resultado es", x**2 )


