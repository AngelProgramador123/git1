def ordenar_datos():
    lista_numeros = []
    print("Ingrese 10 números:")

    # Pedir los 10 números por teclado
    for contador in range(10):
        while True:
            try:
                valor = float(input(f"Ingrese el número {contador+1}: "))
                lista_numeros.append(valor)
                break
            except ValueError:
                print("Dato incorrecto. Ingrese un número válido.")

    # Organizar los números de mayor a menor y de menor a mayor
    orden_mayor = sorted(lista_numeros, reverse=True)
    orden_menor = sorted(lista_numeros)

    # Encontrar el valor máximo y mínimo
    numero_mayor = max(lista_numeros)
    numero_menor = min(lista_numeros)

    # Mostrar los datos obtenidos
    print("\n--- RESULTADOS ---")
    print(f"Números ordenados de mayor a menor: {orden_mayor}")
    print(f"Números ordenados de menor a mayor: {orden_menor}")
    print(f"El número mayor es: {numero_mayor}")
    print(f"El número menor es: {numero_menor}")


ordenar_datos()