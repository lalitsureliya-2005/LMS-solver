import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, src, dst, k = data[:5]
    edges = []
    idx = 5
    for _ in range(m):
        u, v, w = data[idx], data[idx+1], data[idx+2]
        edges.append((u, v, w))
        idx += 3

    L = k + 1  # maximum number of legs allowed
    INF = 10**18
    prev = [INF] * n
    prev[src] = 0

    best_cost = INF
    best_legs = -1

    for legs in range(1, L + 1):
        cur = [INF] * n
        for u, v, w in edges:
            pu = prev[u]
            if pu != INF:
                nd = pu + w
                if nd < cur[v]:
                    cur[v] = nd
        # check destination
        cost = cur[dst]
        if cost < best_cost:
            best_cost = cost
            best_legs = legs
        # if equal cost, keep earlier (smaller legs) which is already stored
        prev = cur

    if best_cost == INF:
        print("-1 -1")
    else:
        print(f"{best_cost} {best_legs}")

if __name__ == "__main__":
    solve()