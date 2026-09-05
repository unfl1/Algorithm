def solution(participant, completion):
    
    participant_dict={}

    for i in participant:
        participant_dict[i]=participant_dict.get(i,0)+1

    for i in completion:
        if i in participant_dict:
            participant_dict[i]-=1
            if participant_dict[i]==0:
                del participant_dict[i]

    return ''.join(participant_dict.keys())