#1
def a():
    return 5
print(a())
#entrega el valor 5

#2
def a():
    return 5
print(a()+a())
#entrega el valor 10

#3
def a():
    return 5
    return 10
print(a())
#entrega  valor 5 

#4

#entrega valor 5
#5
def a():
    print(5)
x = a()
print(x)

#entrega valor 5, y luego nada, por que la variable x no tiene valor

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#imprime 8

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#imprime el valor 2 y 5, pero como string, es decir se ve 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#imprime el valor de la funcion 100, luego verifica las condiciones, e imprime 10

#9
defcopy a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#Devuelve los valores 7, 14 y 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#Devuelve valor 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#imprime el valor de b, 500, luego la funcion a le asigna a bun valor de 300, pero no se llama la funcion a. luego se pide imprimir b nuevamente, que vale 500, ahora se llama la funcion a(), e imprime 300, y finalmente, se llama a imprimir nuevamnete la variable b o sea 500


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#igual a la 11

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#imprime 500 500 300 300

#14copy
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#idefine funcion a() y imprime 1 . define funcion b() e imprime 3. luego llama a la funcion a() e imprime 2


#15
defcopy a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#imprime el valor 1, luego se salta a la def de funcion b, por lo que imprime 3 y 5, luego la variable y toma el valor de la funcion a(), y ya puede imprimir x, que ha tomado el valor de la funcion b()