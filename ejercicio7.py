entrada1 = input("Por favor, ingresa la primera lista de números separados por espacios: ")

entrada2 = input("Por favor, ingresa la segunda lista de números separados por espacios: ")

lista1 = [int(numero) for numero in entrada1.split()]
lista2 = [int(numero) for numero in entrada2.split()]

if len(lista1) != len(lista2):
    print("Las listas no tienen la misma longitud. Deben tener la misma cantidad de elementos.")
else:
    lista_resultado = []

    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        lista_resultado.append(suma)

    print("Lista resultante de la suma de las dos listas:", lista_resultado)
