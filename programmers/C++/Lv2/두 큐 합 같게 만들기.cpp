#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    
    queue<long long> q1;
    queue<long long> q2;
    
    long long sumq1 = 0;
    long long sumq2 = 0;
    
    for (int q : queue1){
        q1.push(q);
        sumq1+=q;
    }
    
    for (int q : queue2){
        q2.push(q);
        sumq2+=q;
    }
    
    if ((sumq1+sumq2)%2!=0){
        return -1;
    }
    
    int answer = 0;
    int limit = static_cast<int>((q1.size() + q2.size()) * 2);
    
    while (sumq1 != sumq2){
        if (answer > limit){
            return -1;
        }
        
        if (sumq1 > sumq2){
            long long value = q1.front();
            q1.pop();
            
            q2.push(value);
            sumq1-=value;
            sumq2+=value;
        }
        else{
            long long value = q2.front();
            q2.pop();
            
            q1.push(value);
            sumq2-=value;
            sumq1+=value;
        }
        
        answer++;
    }
    
    return answer;
}