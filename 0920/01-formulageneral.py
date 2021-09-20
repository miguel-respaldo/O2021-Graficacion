import math

a = eval(input("Ingresa el valor de a: "))
b = eval(input("Ingresa el valor de b: "))
c = eval(input("Ingresa el valor de c: "))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("Las raices son imaginarias")
    x1 = -b / (2 * a) + (math.sqrt(-discriminante) / (2 * a))*1j
    x2 = -b / (2 * a) - (math.sqrt(-discriminante) / (2 * a))*1j
elif discriminante == 0:
    print("Las raices son iguales")
    x1 = x2 = -b / (2 * a)
else:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)

print("x1 = ", x1)
print("x2 = ", x2)
