def solution(record):
    rec = []
    nick = {}
    ans = []
    
    for rc in record:
        info = rc.split()
        action = info[0]
        uid = info[1]
        
        if action =="Enter":
            rec.append((uid, action))
            if uid not in nick:
                nick[uid] = info[2]
            if nick[uid] != info[2]:
                nick[uid] = info[2]
        elif action == "Leave":
            rec.append((uid, action))
        else:
            nick[uid] = info[2]
            
    for uid, action in rec:
        if action == "Enter":
            ans.append(f"{nick[uid]}님이 들어왔습니다.")
        else:
            ans.append(f"{nick[uid]}님이 나갔습니다.")
    return ans