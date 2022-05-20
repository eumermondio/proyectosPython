import math

x1 = float(input("Punto1 x: "))
y1 = float(input("Punto1 y: "))

x2 = float(input("Punto2 x: "))
y2 = float(input("Punto2 y: "))
print("Distancia entre los puntos: " + str(math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))))