# Silver 3
# 재귀

n = int(input())

def rec(n):
    if n == 0:
        return "-"
    return rec(n-1) + " " *(3**(n-1)) + rec(n-1)

print(rec(n))
