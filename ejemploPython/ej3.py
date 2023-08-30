lista_ejemplo=[3,5,4,5,67,8]

print(lista_ejemplo[0])
print(lista_ejemplo[2])
print(lista_ejemplo[4])

lista_ejemplo[1]=43

print(lista_ejemplo[1])

print(len(lista_ejemplo))

i=0

while i<len(lista_ejemplo):
    print(f"El elemento {i +1 } es {lista_ejemplo[i]}")
    i=i+1

print("se utlizara el bucle for")


for elemento  in lista_ejemplo:
    print(f"el valor es {elemento}")


print ("programa finalizado")
