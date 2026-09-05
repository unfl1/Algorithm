def solution(clothes):
    answer = 1
    clothes_dict={}
    for _, category in clothes:
        clothes_dict[category]=clothes_dict.get(category,0)+1

    for v in clothes_dict.values():
        answer*=(v+1)

    return answer-1