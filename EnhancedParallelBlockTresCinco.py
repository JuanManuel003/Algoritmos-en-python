from concurrent.futures import ThreadPoolExecutor, as_completed

def parallel_block_matrix_multiply(A, B, C, size, bsize):
    # Crear un ThreadPoolExecutor para administrar los hilos
    executor = ThreadPoolExecutor(max_workers=2)
    
    # Primer hilo para la primera mitad de la multiplicación
    future1 = executor.submit(multiply_block, A, B, C, size, bsize, 0, size // 2)
    
    # Segundo hilo para la segunda mitad de la multiplicación
    future2 = executor.submit(multiply_block, A, B, C, size, bsize, size // 2, size)
    
    # Esperar a que ambos hilos completen su tarea
    for _ in as_completed([future1, future2]):
        pass
    
    # Apagar el ThreadPoolExecutor
    executor.shutdown()
    
    return A

def multiply_block(A, B, C, size, bsize, start, end):
    for i1 in range(start, end, bsize):
        for j1 in range(0, size, bsize):
            for k1 in range(0, size, bsize):
                for i in range(i1, min(i1 + bsize, size)):
                    for j in range(j1, min(j1 + bsize, size)):
                        for k in range(k1, min(k1 + bsize, size)):
                            A[i][j] += B[i][k] * C[k][j]

def imprimir_matriz(matriz):
    imprimir = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            imprimir += " " + str(matriz[i][j])
        imprimir += "\n"
    print(imprimir)

if __name__ == "__main__":
    m1 = [[2, 4, 9], [1, 3, 9], [5, 6, 7]]
    m2 = [[6, 8, 9], [5, 7, 9], [5, 6, 7]]

    resultado = parallel_block_matrix_multiply(m1, m1, m2, len(m1), 1)
    imprimir_matriz(resultado)
