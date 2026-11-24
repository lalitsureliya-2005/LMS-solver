import sys

MAX_LEN = 19  # 10^18 has at most 19 digits
MAX_K = 100

# precompute dp[k][len][rem] = number of ways to fill 'len' free positions
dp = [None] * (MAX_K + 1)
for k in range(1, MAX_K + 1):
    dp_k = [[0] * k for _ in range(MAX_LEN + 1)]
    dp_k[0][0] = 1
    for l in range(1, MAX_LEN + 1):
        cur = dp_k[l]
        prev = dp_k[l - 1]
        for rem in range(k):
            cnt = prev[rem]
            if cnt:
                for d in range(10):
                    cur[(rem + d) % k] += cnt
    dp[k] = dp_k

def count_upto(N: int, k: int) -> int:
    if N <= 0:
        return 0
    digits = list(map(int, str(N)))
    L = len(digits)
    ans = 0
    rem = 0
    dp_k = dp[k]
    for i, d in enumerate(digits):
        remaining = L - i - 1
        for nd in range(d):
            new_rem = (rem + nd) % k
            need = (-new_rem) % k
            ans += dp_k[remaining][need]
        rem = (rem + d) % k
    if rem == 0:
        ans += 1
    # exclude the number 0
    return ans - 1

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    out = []
    idx = 1
    for _ in range(q):
        N = int(data[idx]); k = int(data[idx + 1]); idx += 2
        out.append(str(count_upto(N, k)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()