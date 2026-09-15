#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer = 0;

    // cur = 현재 기준으로 아직 커버되지 않은 첫 번째 아파트 위치
    int cur = 1;
    int range = w * 2 + 1;

    for (int st : stations) {
        int start = st - w;
        int end = st + w;

        if (start > cur) {
            int gap = start - cur;
            answer += (gap + range - 1) / range;
        }

        cur = max(cur, end + 1);
    }

    // 마지막 station 범위 ~ 끝 사이도 설치
    if (cur <= n) {
        int gap = n - cur + 1;
        answer += (gap + range - 1) / range;
    }

    return answer;
}