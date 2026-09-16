#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    
    unordered_set<char> skill_set;
    
    for (char ch : skill){
        skill_set.insert(ch);
    }
    
    for (string sk : skill_trees){
        int idx = 0;
        bool flag = true;
        
        for (char i : sk){
            if (skill_set.find(i) != skill_set.end()){
                if (i==skill[idx]){
                    idx++;
                }
                else {
                    flag=false;
                    break;
                }
            }
        }
        if (flag) answer++;
    }
    
    return answer;
}