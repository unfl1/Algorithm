def solution(files):
    answer = []

    for file in files:
        HEAD = ""
        NUMBER = ""
        TAIL = ""

        idx = 0  # 0: HEAD, 1: NUMBER, 2: TAIL

        for i in file:
            if idx == 0 and i.isdigit():
                idx = 1
            
            if idx == 1 and not i.isdigit():
                idx = 2
                
            if idx == 0:
                HEAD += i
            elif idx == 1:
                NUMBER += i
            else:
                TAIL +=i
                
        answer.append((HEAD, NUMBER, TAIL))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    res = []
    for ans in answer:
        res.append(''.join(ans))

    return res