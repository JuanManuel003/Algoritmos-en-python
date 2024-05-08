def multiply(a, b, blockSize):
    size = len(a)
    c = [[0.0] * size for _ in range(size)]

    for ib in range(0, size, blockSize):
        for jb in range(0, size, blockSize):
            for kb in range(0, size, blockSize):
                for i in range(ib, min(ib + blockSize, size)):
                    for j in range(jb, min(jb + blockSize, size)):
                        for k in range(kb, min(kb + blockSize, size)):
                            c[i][j] += a[i][k] * b[k][j]

    return c

def imprimirMatriz(matriz):
    imprimir = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            imprimir += " " + str(matriz[i][j])
        imprimir += "\n"
    print(imprimir)

if __name__ == "__main__":
    m1 = [[2, 4], [1, 3]]
    m2 = [[6, 8], [5, 7]]

    resultado = multiply(m1, m2, int(len(m1) ** 0.5))
    imprimirMatriz(resultado)
