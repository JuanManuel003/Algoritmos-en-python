from concurrent.futures import ThreadPoolExecutor

def multiply(a, b, block_size):
    size = len(a)
    c = [[0] * size for _ in range(size)]

    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(lambda _: compute_partial_result(a, b, c, size, block_size), [None])

    return c

def compute_partial_result(a, b, c, size, block_size):
    for ib in range(0, size, block_size):
        for jb in range(0, size, block_size):
            for kb in range(0, size, block_size):
                for i in range(ib, min(ib + block_size, size)):
                    for j in range(jb, min(jb + block_size, size)):
                        for k in range(kb, min(kb + block_size, size)):
                            c[i][j] += a[i][k] * b[k][j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    m1 = [[12, 44], [19, 23]]
    m2 = [[66, 80], [75, 78]]


    resultado = multiply(m1, m2, int(len(m1) ** 0.5))
    imprimir_matriz(resultado)

