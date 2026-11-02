# 숫자 집합에서 6개 조합 출력하기

cur = []

def dfs(arr, start, d):
    if d == 6:
        print(*cur)
        return

    for i in range(start, len(arr)):
        cur.append(arr[i])
        dfs(arr, i+1, d+1)
        cur.pop()

while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    nums = sorted(nums[1:])
    dfs(nums, 0, 0)
    print()