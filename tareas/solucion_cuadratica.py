import math

a = float(input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

determinante = b**2 - 4*a*c

if determinante < 0:
    print("La ecuación tiene raices imaginarias")
    exit(0)
elif determinante == 0:
    print("La ecuación tiene raices iguales")

x1 = (-b + math.sqrt(determinante)) / (2*a)
x2 = (-b - math.sqrt(determinante)) / (2*a)

print("X1 = ", x1)
print("X2 = ", x2)



