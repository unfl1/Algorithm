def solution(genres, plays):
    answer = []

    musics = {}
    total = {}

    # 장르별 노래 + 장르별 총 재생 횟수 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in musics:
            musics[genre].append((i, play))
            total[genre] += play
        else:
            musics[genre] = [(i, play)]
            total[genre] = play

    # 장르 총 재생 횟수 기준 내림차순
    genre_order = sorted(total.keys(), key=lambda x: total[x], reverse=True)

    for genre in genre_order:

        # 재생 횟수 내림차순, 고유번호 오름차순
        musics[genre].sort(key=lambda x: (-x[1], x[0]))

        # 최대 2곡
        for i in range(min(2, len(musics[genre]))):
            answer.append(musics[genre][i][0])

    return answer