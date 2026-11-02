# 암호 만들기

L, C = map(int, input().split())
alpha = sorted(list(input().split()))

vowel = set()
for i in "aeiou":
    vowel.add(i)

def dfs(d, start, tmp, v, not_v):
    if d == L:
        if v>=1 and not_v>=2:
            print(tmp)

    for i in range(start, C):
        if alpha[i] in vowel:
            dfs(d+1, i+1, tmp+alpha[i], v+1, not_v)
        else:
            dfs(d+1, i+1, tmp+alpha[i], v, not_v+1)

dfs(0,0,"", 0, 0)