# 칸토어 문자열 재귀 출력하기

n = int(input())

def rec(n):
    if n == 0:
        return "-"
    return rec(n-1) + " " *(3**(n-1)) + rec(n-1)

print(rec(n))
