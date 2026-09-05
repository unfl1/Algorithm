def solution(str1, str2):
    answer = 0

    str1=str1.lower()
    str2=str2.lower()

    str1_dic={}
    str2_dic={}

    intersection=0
    union=0

    for i in range(len(str1)-1):
        word=str1[i:i+2]
        if word.isalpha():
            str1_dic[word]=str1_dic.get(word,0)+1

    for i in range(len(str2)-1):
        word=str2[i:i+2]
        if word.isalpha():
            str2_dic[word]=str2_dic.get(word,0)+1

    # 교집합
    for word in str1_dic.keys():
        if word in str2_dic:
            intersection+=min(str1_dic[word],str2_dic[word])

    # 합집합
    for word in str1_dic.keys():
        if word in str2_dic:
            union+=max(str1_dic[word],str2_dic[word])
        else:
            union+=str1_dic[word]

    for word in str2_dic.keys():
        if word not in str1_dic:
            union+=str2_dic[word]

    if union==0:
        answer = 1
    else:
        answer=intersection / union

    return int(answer*65536)