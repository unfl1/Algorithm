#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    int cur_A = 0;
    int cur_B = 0;
    
    sort(A.begin(), A.end(), greater<int>());
    sort(B.begin(), B.end(), greater<int>());
    
    while (true){
        
        // 종료 조건
        if (cur_A == A.size() || cur_B == B.size()){
            break;
        }
        
        // B 값이 더 크다면
        if (A[cur_A]<B[cur_B]){
            answer++;
            cur_B++;
        }
        
        // A 값은 계속 커져야 함
        cur_A++;
    }
    
    return answer;
}