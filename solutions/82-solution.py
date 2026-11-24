import sys

sys.setrecursionlimit(10000)

def count_n_queens(n):
    if n == 0:
        return 1
    limit = (1 << n) - 1
    total = 0
    def backtrack(cols, d1, d2):
        nonlocal total
        if cols == limit:
            total += 1
            return
        # positions available in this row
        avail = limit & ~(cols | d1 | d2)
        while avail:
            bit = avail & -avail
            avail -= bit
            backtrack(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)
    backtrack(0, 0, 0)
    return total

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    ns = list(map(int, data[1:1+q]))
    max_n = max(ns) if ns else 0
    max_n = min(max_n, 12)
    pre = [0] * (max_n + 1)
    for n in range(max_n + 1):
        pre[n] = count_n_queens(n)
    out_lines = []
    for n in ns:
        if n <= max_n:
            out_lines.append(str(pre[n]))
        else:
            out_lines.append(str(count_n_queens(n)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()