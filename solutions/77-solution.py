import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    target_value, k = data[0], data[1]
    n, root = data[2], data[3]
    value = [0] * n
    left = [ -1 ] * n
    right = [ -1 ] * n
    p = 4
    for i in range(n):
        value[i] = data[p]
        left[i] = data[p + 1]
        right[i] = data[p + 2]
        p += 3
    parent = [-1] * n
    for i in range(n):
        if left[i] != -1:
            parent[left[i]] = i
        if right[i] != -1:
            parent[right[i]] = i
    # find target index
    target_idx = -1
    for i, v in enumerate(value):
        if v == target_value:
            target_idx = i
            break
    if target_idx == -1:
        print("NONE")
        return
    visited = [False] * n
    q = deque()
    q.append(target_idx)
    visited[target_idx] = True
    for _ in range(k):
        level_size = len(q)
        if level_size == 0:
            break
        for _ in range(level_size):
            node = q.popleft()
            for nb in (left[node], right[node], parent[node]):
                if nb != -1 and not visited[nb]:
                    visited[nb] = True
                    q.append(nb)
    if not q:
        print("NONE")
    else:
        result = sorted(value[node] for node in q)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()