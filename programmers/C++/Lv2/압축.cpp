#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    unordered_map<string, int> word;
    
    for (int i=0; i<26; i++){
        string s(1, 'A'+i);
        word[s]=i+1;
    }
    
    int next_idx = 27;
    int cur = 0;
    
    while (cur<msg.size()){
        string add_word="";
        int next = cur;
        
        while(next<msg.size()){
            string tmp = add_word + msg[next];
            
            if (word.find(tmp) == word.end()){
                break;
            }
            
            add_word = tmp;
            next++;
        }
        
        answer.push_back(word[add_word]);
        
        if (next < msg.size()){
            word[add_word+msg[next]] = next_idx++;
        }
        
        cur=next;
    }
    return answer;
}