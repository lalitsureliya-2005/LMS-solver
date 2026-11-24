import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))

    def sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = sort_count(arr[:mid])
        right, inv_right = sort_count(arr[mid:])
        merged = []
        i = j = 0
        inv = inv_left + inv_right
        len_left = len(left)
        while i < len_left and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv += len_left - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, ans = sort_count(a)
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()