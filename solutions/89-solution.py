import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    V = int(next(it))
    E = int(next(it))
    adj_mask = [0] * V
    self_loop = False
    for _ in range(E):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            self_loop = True
        else:
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u
    M = int(next(it))
    if self_loop:
        print("NO")
        return
    if M >= V:
        print("YES")
        return

    N = 1 << V
    independent = [False] * N
    independent[0] = True
    for mask in range(1, N):
        # get least significant set bit
        lsb = mask & -mask
        v = (lsb.bit_length() - 1)
        rest = mask ^ lsb
        independent[mask] = independent[rest] and ((adj_mask[v] & rest) == 0)

    INF = V + 1
    dp = [INF] * N
    dp[0] = 0
    for mask in range(1, N):
        sub = mask
        while sub:
            if independent[sub]:
                remaining = mask ^ sub
                if dp[remaining] + 1 < dp[mask]:
                    dp[mask] = dp[remaining] + 1
                    if dp[mask] == 1:  # cannot get better
                        break
            sub = (sub - 1) & mask

    print("YES" if dp[N - 1] <= M else "NO")

if __name__ == "__main__":
    solve()