import sys, collections

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    LOG = (n).bit_length()
    up = [[0] * n for _ in range(LOG)]
    depth = [0] * n
    parent = [-1] * n

    dq = collections.deque([0])
    parent[0] = 0
    while dq:
        node = dq.popleft()
        for nb in adj[node]:
            if nb == parent[node]:
                continue
            parent[nb] = node
            depth[nb] = depth[node] + 1
            dq.append(nb)

    for v in range(n):
        up[0][v] = parent[v]

    for k in range(1, LOG):
        prev = up[k - 1]
        cur = up[k]
        for v in range(n):
            cur[v] = prev[prev[v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        bit = 0
        while diff:
            if diff & 1:
                u = up[bit][u]
            diff >>= 1
            bit += 1
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    out = []
    for _ in range(q):
        u = int(next(it))
        v = int(next(it))
        out.append(str(lca(u, v)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()