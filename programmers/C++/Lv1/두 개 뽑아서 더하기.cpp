#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    set<int> num;
    
    sort(numbers.begin(), numbers.end());
    for (int i=0; i<numbers.size()-1; i++){
        for (int j=i+1; j<numbers.size(); j++){
            num.insert(numbers[i]+numbers[j]);
        }
    }
    
    for (int n : num){
        answer.push_back(n);
    }
    
    return answer;
}