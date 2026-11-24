import sys

MOD = 1000000007

def mod_pow(x, n):
    if n == 0:
        return 1
    x %= MOD
    result = 1
    while n:
        if n & 1:
            result = (result * x) % MOD
        x = (x * x) % MOD
        n >>= 1
    return result

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    out = []
    idx = 1
    for _ in range(q):
        x = int(data[idx]); n = int(data[idx + 1]); idx += 2
        out.append(str(mod_pow(x, n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()