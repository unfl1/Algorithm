def solution(arr):
    answer = [0, 0]
    
    search(arr, len(arr), 0, 0, answer)
    
    return answer

def search(arr, size, sy, sx, ans):
    cur = arr[sy][sx]
    
    same = True
    
    for y in range(sy, sy+size):
        for x in range(sx, sx+size):
            if arr[y][x] != cur:
                same = False
                break
                
        if not same:
            break
            
    if same:
        ans[cur]+=1
    else:
        for i in range(2):
            for j in range(2):
                half = size//2
                search(arr, half, sy + half*i, sx + half*j, ans)