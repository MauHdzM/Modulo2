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
#corremos un for que vaya en el rango la lista para analiza cada numero dentro de esta
    for x in b:
        if x==2:
            lista1.append(x)
        if x>2:
            primo=True
        #Dividimos la iteración entre todos los números que van antes 
            for p in range(2, x-1):
                if x%p== 0: #en caso de que uno de dichos residuos sea igual a cero el número es compuesto
                    primo=False
                    
            if primo: #en caso de que el número sea primo se agregará a otra lista
            
                lista1.append(x)
    print (lista1)
    return lista1
lista1=unu(lista)
