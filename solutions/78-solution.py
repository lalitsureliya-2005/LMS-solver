import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[1:1 + n]
    cur = best = arr[0]
    for v in arr[1:]:
        cur = v if cur + v < v else cur + v
        if cur > best:
            best = cur
    sys.stdout.write(str(best))

if __name__ == "__main__":
    main()