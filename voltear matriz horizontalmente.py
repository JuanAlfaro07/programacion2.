def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el elemento para la posición [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def voltear_horizontal(matriz):
    for fila in matriz:
        fila.reverse()
filas = 6
columnas = 6
print(f"Ingrese los elementos para una matriz {filas}x{columnas}:")
matriz_personalizada = crear_matriz(filas, columnas)
print("\nMatriz original:")
for fila in matriz_personalizada:
    print(fila)
voltear_horizontal(matriz_personalizada)
print("\nMatriz volteada horizontalmente:")
for fila in matriz_personalizada:
    print(fila)
