import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    pre = list(map(int, data[1:1 + n]))
    ino = list(map(int, data[1 + n:1 + 2 * n]))
    pos = {val: i for i, val in enumerate(ino)}
    sys.setrecursionlimit(30000)
    res = []

    def dfs(pre_start, in_start, size):
        if size <= 0:
            return
        root = pre[pre_start]
        idx = pos[root]
        left_size = idx - in_start
        right_size = size - left_size - 1
        dfs(pre_start + 1, in_start, left_size)
        dfs(pre_start + 1 + left_size, idx + 1, right_size)
        res.append(root)

    dfs(0, 0, n)
    sys.stdout.write(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()