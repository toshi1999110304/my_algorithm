# O(AloglogA + NlogA)
# 素因数分解を何度も行うときは、高速verが使える
def preprocess_fun(A_max):
    # Dテーブルを作る D[12] = 2, D[3] = 3, D[6] = 2
    # D[i] : i の素因数のうち一番小さいもの
    p_flag = [True] * (A_max + 1)
    D = [0] * (A_max + 1)
    p_flag[0] = False
    p_flag[1] = False
    for i in range(2, A_max + 1):
        if p_flag[i]:
            for j in range(i, A_max + 1, i):
                if p_flag[j]:
                    p_flag[j] = False
                    D[j] = i
    return D

# 例[6, 12, 5, 20]に対して, [[2, 3], [2, 2, 3], [5], [2, 2, 5]]を返す
def high_speed_prifac(A_list, D, A_max):
    prist = []
    for A in A_list:
        num = []
        temp = A
        while temp != 1:
            num.append(D[temp])
            temp = temp // D[temp]
        prist.append(num)
    return prist
