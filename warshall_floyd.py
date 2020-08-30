# d : 隣接行列
# n : n * n
def warshall_floyd(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                #print(d)
    return d
