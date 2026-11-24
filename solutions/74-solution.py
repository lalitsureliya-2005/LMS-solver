import sys

class Node:
    __slots__ = ('val',)
    def __init__(self, val):
        self.val = val

def solve():
    data = sys.stdin.read().strip()
    if not data:
        print("true")
        return
    data = data.strip()
    if data[0] == '[' and data[-1] == ']':
        data = data[1:-1]
    data = data.strip()
    if not data:
        print("true")
        return
    tokens = [tok.strip() for tok in data.split(',')]
    nodes = []
    for tok in tokens:
        if tok.lower() in ('null', 'none', ''):
            nodes.append(None)
        else:
            try:
                val = int(tok)
            except:
                # fallback for possible stray characters
                val = int(tok)
            nodes.append(Node(val))
    n = len(nodes)
    if n == 0:
        print("true")
        return
    stack = [(0, float('-inf'), float('inf'))]
    while stack:
        idx, low, high = stack.pop()
        if idx >= n:
            continue
        cur = nodes[idx]
        if cur is None:
            continue
        v = cur.val
        if not (low < v < high):
            print("false")
            return
        # right child
        r = 2 * idx + 2
        if r < n:
            stack.append((r, v, high))
        # left child
        l = 2 * idx + 1
        if l < n:
            stack.append((l, low, v))
    print("true")

if __name__ == "__main__":
    solve()