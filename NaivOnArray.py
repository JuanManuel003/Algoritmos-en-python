def naive_on_array(a, b, c, n, p, m):
    for i in range(n):
        for j in range(m):
            c[i][j] = 0.0
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c

def imprimir_matriz(matriz):
    imprimir = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            imprimir += " " + str(matriz[i][j])
        imprimir += "\n"
    print(imprimir)

def main():
    m1 = [[2, 4], [1, 3]]
    m2 = [[6, 8], [5, 7]]
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0 for _ in range(m2l)] for _ in range(m1l)]

    resultado = naive_on_array(m1, m2, m3, m1l, m2l, p)
    imprimir_matriz(resultado)

if __name__ == "__main__":
    main()
