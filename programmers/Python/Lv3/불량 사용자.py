res = set()

def dfs(d, user_id, banned_id, visited, selected):
    if d == len(banned_id):
        for idx, value in enumerate(selected):
            if not is_same(user_id[value], banned_id[idx]):
                return

        res.add(frozenset(selected))
        return
        
    for i in range(len(user_id)):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            dfs(d+1, user_id, banned_id, visited, selected)
            selected.pop()
            visited[i] = False
            

def is_same(a, b):
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if b[i]=='*':
            continue
            
        if a[i] != b[i]:
            return False
        
    return True

def solution(user_id, banned_id):
    res.clear()
    visited = [False] * len(user_id)
    
    dfs (0, user_id, banned_id, visited, [])
    return len(res)

