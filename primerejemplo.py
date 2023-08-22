print("Hola")
print("mundo")

a=12
if a<= 15:
    print("a es menor ")
    print("a es = ", a)
elif 15 < a <= 30:
    print("entre 15 y 30")
else:
    print("a es mayor")

while a<=15:
    print("Dentro del bucle a es ", a)
    a += 1 # comentario a = a + 1

lista = [1,3,5,7]
for e in lista:
    print("elemento =", e)

rango = range(0,10,2)
for e in rango:
    print("rango = ",e )

