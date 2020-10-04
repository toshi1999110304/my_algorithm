# O(AloglogA) 
# A までの素数を求める
def eratosthenes(A):
    p_flag = [True] * (A + 1)
    p_flag[0] = False
    p_flag[1] = False
    for i in range(2, int(A ** 0.5) + 1):
        if p_flag[i]:
            for j in range(i * 2, A + 1, i):
                p_flag[j] = False
                
    return p_flag # 素数のバイナリリスト

    # [2, 3, 5, 7, 11, ~] で表すなら
    #return [i for i in range(n + 1) if p_flag[i]]
