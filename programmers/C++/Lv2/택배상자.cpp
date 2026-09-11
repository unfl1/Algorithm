#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    
    stack<int> belt;
    
    int idx = 0;
    
    for (int i=1; i<=order.size(); i++){
        belt.push(i);

        while (idx<order.size() && !belt.empty() && belt.top()==order[idx]){
            belt.pop();
            idx++;
        }
    }
    
    return idx;
}