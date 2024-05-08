def multiply(a, b, block_size):
    size = len(a)
    c = [[0] * size for _ in range(size)]

    for ib in range(0, size, block_size):
        for jb in range(0, size, block_size):
            for kb in range(0, size, block_size):
                for i in range(ib, min(ib + block_size, size)):
                    for j in range(jb, min(jb + block_size, size)):
                        for k in range(kb, min(kb + block_size, size)):
                            c[i][k] += a[i][j] * b[j][k]

    return c

def imprimir_matriz(matriz):
    imprimir = ""
    for fila in matriz:
        for elemento in fila:
            imprimir += " " + str(elemento)
        imprimir += "\n"
    print(imprimir)

if __name__ == "__main__":
    m1 = [[2, 4], [1, 3]]
    m2 = [[6, 8], [5, 7]]

    resultado = multiply(m1, m2, int(len(m1) ** 0.5))
    imprimir_matriz(resultado)
