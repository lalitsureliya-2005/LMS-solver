import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((w, u, v))
    edges.sort()
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    total_weight = 0
    edge_cnt = 0
    for w, u, v in edges:
        if union(u, v):
            total_weight += w
            edge_cnt += 1
            if edge_cnt == n - 1:
                break

    if n == 1:
        print("0 0")
    elif edge_cnt == n - 1:
        print(f"{total_weight} {edge_cnt}")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()