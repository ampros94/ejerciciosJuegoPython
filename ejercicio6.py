entrada = input("por favor ingresa una oracion o un parrafo ")
palabras = entrada.split()
inicial = input("por favor ingresa la inicial que quieres buscar ")
print("las palabras que comienzan con la letra ", inicial)
for palabra in palabras:
    if palabra.startswith(inicial):
        print(palabra)