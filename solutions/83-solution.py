import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    R, C = map(int, data[:2])
    grid = data[2:2 + R]
    word = data[2 + R]
    L = len(word)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*C for _ in range(R)]

    sys.setrecursionlimit(10000)

    def dfs(r, c, idx):
        if idx == L:
            return True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == word[idx]:
                visited[nr][nc] = True
                if dfs(nr, nc, idx + 1):
                    return True
                visited[nr][nc] = False
        return False

    for i in range(R):
        for j in range(C):
            if grid[i][j] == word[0]:
                visited[i][j] = True
                if dfs(i, j, 1):
                    print("YES")
                    return
                visited[i][j] = False
    print("NO")

if __name__ == "__main__":
    solve()