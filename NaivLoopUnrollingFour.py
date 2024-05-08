def naivLoopUnrollingFour(a, b, c, n, p, m):
    for i in range(n):
        for j in range(m):
            aux = 0.0
            if p % 4 == 0:
                for k in range(0, p, 4):
                    aux += (a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j] +
                            a[i][k + 2] * b[k + 2][j] + a[i][k + 3] * b[k + 3][j])
            elif p % 4 == 1:
                PP = p - 1
                for k in range(0, PP, 4):
                    aux += (a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j] +
                            a[i][k + 2] * b[k + 2][j] + a[i][k + 3] * b[k + 3][j])
                aux += a[i][PP] * b[PP][j]
            elif p % 4 == 2:
                PP = p - 2
                PPP = p - 1
                for k in range(0, PP, 4):
                    aux += (a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j] +
                            a[i][k + 2] * b[k + 2][j] + a[i][k + 3] * b[k + 3][j])
                aux += a[i][PP] * b[PP][j] + a[i][PPP] * b[PPP][j]
            else:
                PP = p - 3
                PPP = p - 2
                PPPP = p - 1
                for k in range(0, PP, 4):
                    aux += (a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j] +
                            a[i][k + 2] * b[k + 2][j] + a[i][k + 3] * b[k + 3][j])
                aux += (a[i][PP] * b[PP][j] + a[i][PPP] * b[PPP][j] + a[i][PPPP] * b[PPPP][j])
            c[i][j] = aux
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
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0 for _ in range(m2l)] for _ in range(m1l)]

    resultado = naivLoopUnrollingFour(m1, m2, m3, m1l, m2l, p)
    imprimirMatriz(resultado)
