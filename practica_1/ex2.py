#Ejercicio de Arreglos de 1 a n
import sys

def uwu(a):
 lista = list(range(1,a+1))
 print(lista)
 return lista
lista=uwu(int(sys.argv[1]))
def unu(b):
 for x in b:
    if x==2:
        lista1.append(x)
    if x>2:
        primo=True
        for p in range(2, x-1):
            if x%p== 0:
                primo=False
                
        if primo:
            lista1.append(x)
 print(lista1)
unu(lista)
