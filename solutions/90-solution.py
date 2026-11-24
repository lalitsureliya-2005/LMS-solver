import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1])
    rel = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        op = data[idx + 1]
        v = int(data[idx + 2]) - 1
        rel.append((u, op, v))
        idx += 3

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1

    # unite equalities
    for u, op, v in rel:
        if op == '=':
            union(u, v)

    # map roots to ids
    root_to_id = {}
    comp_id = 0
    for i in range(n):
        r = find(i)
        if r not in root_to_id:
            root_to_id[r] = comp_id
            comp_id += 1

    k = comp_id
    adj = [[] for _ in range(k)]
    indeg = [0] * k

    # process strict relations
    for u, op, v in rel:
        if op == '=':
            continue
        ru = find(u)
        rv = find(v)
        if ru == rv:
            print("IMPOSSIBLE")
            return
        if op == '<':
            a, b = ru, rv
        else:  # '>'
            a, b = rv, ru
        ida = root_to_id[a]
        idb = root_to_id[b]
        adj[ida].append(idb)
        indeg[idb] += 1

    # topological sort
    q = deque([i for i in range(k) if indeg[i] == 0])
    visited = 0
    while q:
        node = q.popleft()
        visited += 1
        for nb in adj[node]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)

    if visited == k:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()