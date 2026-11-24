import sys, heapq

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    heap = [i for i in range(1, n + 1) if indeg[i] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    out = sys.stdout
    if len(order) == n:
        out.write(' '.join(map(str, order)))
    else:
        out.write('CYCLE')

if __name__ == "__main__":
    main()