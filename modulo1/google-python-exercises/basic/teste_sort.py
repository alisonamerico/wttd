lista = list(range(10))
import random
random.shuffle(lista)
print(lista)
lista.sort()
print(lista)

def épar(x):
    return (x%2==0)
print(épar(2))
print(épar(3))



def maior_numero(n_maior, n_menor):
    if  n_maior > n_menor:
        return n_maior
    else:
        return n_menor
print(maior_numero(5,6))
print(maior_numero(2,1))
print(maior_numero(7,7))