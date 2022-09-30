import sys
import random
a = int(sys.argv[1])
numbers_1_to_10 = list(range(1,a+1))
print(numbers_1_to_10)
lista=[]

for x in numbers_1_to_10:
    if x==2:
        lista.append(x)
    if x>2:
        primo=True
        for p in range(2, x-1):
            if x%p== 0:
                primo=False
                
        if primo:
            lista.append(x)
print(lista)
