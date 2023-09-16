print("Bienvenido al laberinto del minotauro, al entrar seras perseguido por el minotaruto, recuerda que tambien hay trampas, si te alcanza el Minotauro o activas una trampa pierdes. ¿Tienes estas 3 opciones: Derecho, Derecha o Izquierda. A donde iras primero?")

decicion1 = int(input("Escribre que opcion tomaras: 1. izqueirda, 2. derecho, 3.derecha "))

if decicion1 == 2:
    print("Te alejaste un poco de Minotauro.")
elif decicion1 == 3:
    print("LLegas  un callejon sin salida. el Minotauro te a alcanzado. PERDISTE")
    exit()
else:
    print("Activaste una trampa. PERDISTE")
    exit()

print("Bien hecho. A donde iras ahora?")

decicion2 = int(input("Escribre que opcion tomaras: 1. izqueirda, 2.derecha"))

if decicion2 == 1:
    print("Te sigues alejado del Minorauro.")
else:
    print("Activaste una trampa. PERDISTE")
    exit()

print("Vas bien, sigue a si.")

decicion3 = int(input("Escribre que opcion tomaras: 1. izqueirda, 2.derecha"))

if decicion3 == 1:
    print("Vas muy bien, pero el Minotauro sigue detras tuyo.")
else:
    print("Has caido en una fosa. PERDISTE")
    exit()

print("Continua a si vas muy bien.")

decicion4 = int(input("Escribre que opcion tomaras: 1. izqueirda, 2.derecho"))

if decicion4 == 1:
    print("Te tropiezas con una cadena. PERDISTE")
    exit()
else:
    print("Bien hecho.")

print("Ahora te encuentras con un hueco en la pared")

decicion5 = int(input("Escribre que opcion tomaras: 1. derecha, 2. derecho, 3. hueco"))

if decicion5 == 1:
    print("Bien, estas muy cerca de salir.")
elif decicion5 == 2:
    print("Entras a un callejon sin salida. PERDISTE")
    exit()
else:
    print("En le hueco habia una serpiente y te a mordido. PERDISTE")
    exit()

print("Ya casi logras salir.")

decicion6 = int(input("Escribre que opcion tomaras: 1. derecha, 2.derecho"))

if decicion6 == 1:
    print("Activaste una trampa y el minotauro te alcanza. PERDISTE")
    exit()
else:
    print("Vez la salida.")

print("Felicidades, lograste salir con vida del laberinto del Minotauro y ya no te persigue, puedes seguir tu camino." )