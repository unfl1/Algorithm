#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    
    stack<int> belt;
    
    int cnt = 0;
    int idx = 0;
    
    for (int i=1; i<=order.size(); i++){
        if (i != order[idx]){
            belt.push(i);
        } else {
            cnt++;
            idx++;
            while (!belt.empty() && belt.top()==order[idx]){
                belt.pop();
                idx++;
                cnt++;
            }
        }
    }
    
    return cnt;
}