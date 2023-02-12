false = False
true = True

result = 10 <= 10 or 50 == '50' or 100_000 != 100_000 or 'aleatorio' == 'aleatorio' or 0 > 10 or 0 or 1 and True or False
print(result)
# Escribir 10 ejemplos con operadores de comparación y operadores logicos and y or, subirlos a github

a = 21
b = 10
c = 0

if ( a == b ):
   print("Línea 1",a,"es igual a",b)
else:
   print("Línea 1",a,"no es igual a",b)

if ( a != b ):
   print("Línea 2",a,"no es igual a",b)
else:
   print("Línea 2",a,"es igual a",b)

if ( a < b ):
   print("Línea 4",a,"es menor que",b) 
else:
   print("Línea 4",a,"no es menor que",b)

if ( a > b ):
   print("Línea 5",a,"es mayor que",b)
else:
   print("Línea 5",a,"no es mayor que",b)

a = 5
b = 20
if ( a <= b ):
   print("Línea 6",a,"es menor o igual que",b)
else:
   print("Línea 6",a,"no es menor o igual que",b)

if ( b >= a ):
   print("Línea 7",b,"es mayor o igual que",b)
else:
   print("Línea 7",b,"no es mayor o igual que",b)