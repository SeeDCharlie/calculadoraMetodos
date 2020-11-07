print("Suma y resta de matrices")

def restaMatriz(col, row):
        # Se declara la primer matriz con el num de filas y columnas dados por el usuario
        matriz1 = [[0 for x in range(row)] for y in range(col)]
        print("\nPRIMER MATRIZ")
        # Se utiliza un ciclo para solicitar los valores de la primer matriz
        for i in range(col):
            for j in range(row):
                matriz1[i][j] = float(input("Elemento[" + str(i) + "][" + str(j) + "]: "))

        # Se declara la segunda matriz con el num de filas y columnas dados por el usuario
        matriz2 = [[0 for x in range(row)] for y in range(col)]
        print("\nSEGUNDA MATRIZ")
        # Se utiliza un ciclo para solicitar los valores de la segunda matriz
        for i in range(col):
            for j in range(row):
                matriz2[i][j] = float(input("Elemento[" + str(i) + "][" + str(j) + "]: "))
        # Se declara una tercer matriz para almacenar el resultado de la resta
        matriz3 = [[0 for x in range(row)] for y in range(col)]

        # Se utiliza un ciclo para realizar la sresta
        for i in range(col):
            for j in range(row):
                matriz3[i][j] = matriz1[i][j] - matriz2[i][j]
        return matriz3

def sumaMatriz():
    # se solicita al usuario el numero de columnas de las matrices
        col = int(input("Número de filas:"))
    # se solicita al usuario el numero de filas de las matrices
        row = int(input("Número de columnas:"))
    # Se declara la primer matriz con el num de filas y columnas dados por el usuario
        matriz1 =[[0 for x in range(row)] for y in range(col)]
        print("\nPRIMER MATRIZ")
    #Se utiliza un ciclo para solicitar los valores de la primer matriz
        for i in range(col):
            for j in range(row):
                matriz1[i][j] = float(input("Elemento[" + str(i) + "][" + str(j) + "]: "))

    # Se declara la segunda matriz con el num de filas y columnas dados por el usuario
        matriz2 =[[ 0 for x in range(row)] for y in range(col)]
        print("\nSEGUNDA MATRIZ")
    #Se utiliza un ciclo para solicitar los valores de la segunda matriz
        for i in range(col):
            for j in range(row):
                matriz2[i][j] = float(input("Elemento[" + str(i) + "][" + str(j) + "]: "))
    # Se declara una tercer matriz para almacenar el resultado de la suma
        matriz3 =[[0 for x in range(row)] for y in range(col)]

    #Se utiliza un ciclo para realizar la suma
        for i in range(col):
            for j in range(row):
                matriz3[i][j] = matriz1[i][j]+ matriz2[i][j]
        return matriz3

def menu():
        print("\nSelecciona una opción")
        print("1 - Suma de matrices")
        print("2 - Resta de matrices")
        print("3 - Salir")

while True:
        menu()
        # solicitamos una opción al usuario
        opcionMenu = input("Digita una opción: ")

        if opcionMenu == "1":
            Matriz = sumaMatriz()
            print("\nRESULTADO")
            for i in Matriz:
                print(i)
        elif opcionMenu == "2":
            Matriz = restaMatriz()
            print("\nRESULTADO")
            for i in Matriz:
                print(i)
        elif opcionMenu =="3":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
