import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0]); head = int(data[1]); tail = int(data[2])
    value = [0] * n
    prv = [0] * n
    nxt = [0] * n
    p = 3
    for i in range(n):
        value[i] = int(data[p]); prv[i] = int(data[p + 1]); nxt[i] = int(data[p + 2]); p += 3

    cur = tail
    max_val = value[tail]
    kept = 1
    cur = prv[tail]
    while cur != -1:
        prev_cur = prv[cur]
        if value[cur] < max_val:
            a = prev_cur
            b = nxt[cur]
            if a != -1:
                nxt[a] = b
            else:
                head = b
            if b != -1:
                prv[b] = a
        else:
            max_val = value[cur]
            kept += 1
        cur = prev_cur

    forward_slots = []
    forward_vals = []
    node = head
    while node != -1:
        forward_slots.append(str(node))
        forward_vals.append(str(value[node]))
        node = nxt[node]

    reverse_slots = []
    node = tail
    while node != -1:
        reverse_slots.append(str(node))
        node = prv[node]

    out = []
    out.append(str(kept))
    out.append(' '.join(forward_slots))
    out.append(' '.join(reverse_slots))
    out.append(' '.join(forward_vals))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()