#Ejercicio de Arreglos de 1 a n
import sys
#función para crear lista de 1 a sys.argv[1]
def uwu(a):
 lista = list(range(1,a+1))
 print(lista)
 return lista
lista=uwu(int(sys.argv[1]))
#función para evaluar que números son primos de dicha lista
def unu(b):
    lista1=[]
#corremos un for que vaya en el rango de la lista para analizar cada número dentro de esta
    for x in b:
        if x==2: #en caso de ser 2 lo adunta automáticamente a la lista de números primos
            lista1.append(x)
        if x>2:
            primo=True
        #Dividimos la iteración entre todos los números que van antes de este y después del dos
            for p in range(2, x-1):
                if x%p== 0: #en caso de que uno de dichos residuos sea igual a cero el número es compuesto. Recordemos que un número sólo tiene residuo 0 cuando se divide entre 1 o sí mismo
                    primo=False
                    
            if primo: #en caso de que el número sea primo se agregará a otra lista
            
                lista1.append(x)
    print (lista1)
    return lista1
lista1=unu(lista)
