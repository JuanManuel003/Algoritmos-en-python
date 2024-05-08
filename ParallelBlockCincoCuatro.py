from multiprocessing import Pool

def multiply(a, b, block_size):
    size = len(a)
    c = [[0] * size for _ in range(size)]

    def compute_partial_result(ib):
        for jb in range(0, size, block_size):
            for kb in range(0, size, block_size):
                for i in range(ib, min(ib + block_size, size)):
                    for j in range(jb, min(jb + block_size, size)):
                        for k in range(kb, min(kb + block_size, size)):
                            c[k][i] += a[k][j] * b[j][i]

    # Use Pool for parallel computation
    with Pool(processes=2) as pool:
        pool.map(compute_partial_result, range(0, size, block_size))

    return c

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    m1 = [[2, 4], [1, 3]]
    m2 = [[6, 8], [5, 7]]

    resultado = multiply(m1, m2, int(len(m1) ** 0.5))
    imprimir_matriz(resultado)
