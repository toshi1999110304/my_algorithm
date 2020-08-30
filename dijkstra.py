# e : 連結リスト
# s : スタート地点　0 ~ n - 1
import heapq
def dijkstra(s, e):
    n = len(e)
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost
