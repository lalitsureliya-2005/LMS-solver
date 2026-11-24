import json, sys
from collections import deque

def can_finish_courses(payload):
    n = payload.get("n", 0)
    prereqs = payload.get("prerequisites", [])
    indeg = [0] * n
    adj = [[] for _ in range(n)]
    for a, b in prereqs:
        # edge b -> a
        if 0 <= a < n and 0 <= b < n:
            adj[b].append(a)
            indeg[a] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == n

if __name__ == "__main__":
    payload = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(can_finish_courses(payload), separators=(",", ":")))