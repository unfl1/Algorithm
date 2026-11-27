# Gold 3
# 시뮬레이션

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(board[i])