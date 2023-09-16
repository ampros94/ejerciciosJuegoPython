lista = input("ingrese una lista de 5 numeros separados por espacio")
entrada = lista.split()
numeros = [int(numero) for numero in entrada]
suma = 0
for numero in numeros:
    suma += numero
print("la suma de los numeros", suma)