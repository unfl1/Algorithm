cnt = 0
ans = 0

def solution(word):
    global cnt, ans
    cnt, ans = 0, 0

    arr = ['A', 'E', 'I', 'O', 'U']
    dfs(arr, word, "", 0)

    return ans

def dfs(arr, target, cur, d):
    global cnt, ans

    if cur == target:
        ans = cnt
        return

    cnt += 1

    if d == 5:
        return

    for i in range(len(arr)):
        dfs(arr, target, cur+arr[i], d+1)
        
        if ans:
            return