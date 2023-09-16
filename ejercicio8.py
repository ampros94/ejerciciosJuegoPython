numero = int(input("Por favor, ingresa un número para la tabla de multiplicar: "))

rango = range(1, 9)

print(f"Tabla de multiplicar del {numero}:")

for i in rango:
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
