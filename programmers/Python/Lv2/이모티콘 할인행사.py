max_people = 0
max_cost = 0

def solution(users, emoticons):
    global max_people, max_cost

    max_people = 0
    max_cost = 0

    discount = [40, 30, 20, 10]
    dfs(users, emoticons, discount, 0, [])

    return [max_people, max_cost]


def dfs(users, emoticons, discount, d, cur):
    global max_people, max_cost

    if d == len(emoticons):
        people = 0
        cost = 0

        for per, price in users:
            total = 0

            for i in range(len(cur)):
                if cur[i] >= per:
                    total += emoticons[i] * (100 - cur[i]) // 100

            if total >= price:
                people += 1
            else:
                cost += total

        if people > max_people:
            max_people = people
            max_cost = cost
        elif people == max_people:
            max_cost = max(max_cost, cost)

        return

    for i in range(4):
        cur.append(discount[i])
        dfs(users, emoticons, discount, d+1, cur)
        cur.pop()