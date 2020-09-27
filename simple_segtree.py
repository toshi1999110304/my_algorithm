class segtree():   
    def __init__(self, a):
        self.n = len(a)
        self.N = 1
        
        while (self.N < self.n):
            self.N *= 2  #葉の数を計算（n以上の最小の2冪数）
        self.num = [float('Inf')] * (2 * self.N - 1)   
        for j in range(self.n):
            self.update(j, a[j])
            
    def test(self):
        #print(self.num)
        print(self.query(2, 3, 0, 0, self.N))
        
    def update(self, i, x):
        # i 番目の葉の値を x 変える
        i += self.N - 1
        self.num[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.num[i] = min(self.num[i * 2 + 1],
                             self.num[i * 2 + 2])
            
    def query(self, a, b, k, l, r):
        # [a, b)の区間に対するクエリについて
        # ノード k (区間 [l, r) 担当)が答える
        if r <= a or b <= l: #区間が被らない場合は INF を返す
            return float('Inf')
        elif a <= l and r <= b:
            return self.num[k] #ノード k の担当範囲がクエリ区間 [a, b)
                                #に完全に包まれる
        else:
            c1 = self.query(a, b, 2 * k + 1, l, (l + r) / 2) # 左の子に値を聞く
            c2 = self.query(a, b, 2 * k + 2, (l + r) / 2, r) # 右の子に値を聞く
            return min(c1, c2) # 左右の子の値の min を取る
