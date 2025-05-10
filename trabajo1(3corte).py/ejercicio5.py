n = int(input("Ingrese el numero de numeros triangulares solicitado: "))
print("Secuencia de números triangulares: ")
for i in range(1, n + 1):
    triangular = i * (i + 1) // 2  # Fórmula matemática
    print(triangular, end=" ")