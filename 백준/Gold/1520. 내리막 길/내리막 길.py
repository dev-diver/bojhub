import sys, io, os
import heapq
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
M, N = map(int, input().split())
G = [[*map(int, input().split())] for _ in range(M)]
D = [[0]*N for _ in range(M)]
D[0][0] = 1
Q = [(-G[0][0], 0, 0)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while Q:
    H, x, y = heapq.heappop(Q)
    H = -H
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if 0 <= nx < M and 0 <= ny < N:
            h = G[nx][ny]
            if h < H:
                if D[nx][ny] == 0:
                    heapq.heappush(Q, (-h, nx, ny))
                D[nx][ny] += D[x][y]

sys.stdout.write(str(D[M-1][N-1]))