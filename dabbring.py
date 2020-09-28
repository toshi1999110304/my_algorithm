#ダブリング O(NlogK) : N 個の要素の K 回操作後の状態を求める
# 二次元配列作成(0-index)
import math
dv = []
for _ in range(int(math.log2(K)) + 1):
    l = [0] * N
    dv.append(l)

# ダブリングで表を構築
for k in range(1, int(math.log2(K)) + 1):
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]
        
# N 回目を 2 ^ t で表すためにビット演算を用いる
# a : dv の何行目を用いるかを格納
a = []
for i in range(int(math.log2(K)) + 1):
    if K >> i & 1:
        a.append(i)
        
# a を用いて N 回操作後の状態を求める
now = 0
    for i in a:
        now = dv[i][now]
        
        
#若干コード短縮版
import math

dv = []
dv.append(ai)
for k in range(1, int(math.log2(K)) + 1):
    l = [0] * N
    dv.append(l)
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]
    
now = 0
for i in range(int(math.log2(K)) + 1):
    if K >> i & 1:
        now = dv[i][now]
