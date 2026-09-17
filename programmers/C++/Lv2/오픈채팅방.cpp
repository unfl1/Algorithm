#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>

using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    
    vector<pair<string, string>> ORDER;
    unordered_map<string, string> ID;
    
    for (string re : record){
        stringstream ss(re);
        
        string action;
        string uid;
        string nickname;
        
        ss >> action >> uid >> nickname;
        
        if(action == "Leave") {
            ORDER.push_back({uid, action});
            continue;
        }
        ID[uid] = nickname;
        
        if (action == "Change") continue;
        ORDER.push_back({uid, action});
    }
    
    for (const pair<string, string>& p : ORDER){
        string message = "";
        
        message+=ID[p.first]+"님이 ";
        
        if (p.second=="Enter"){
            message+="들어왔습니다.";
        }
        else if (p.second=="Leave"){
            message+="나갔습니다.";
        }
            
        answer.push_back(message);
    }
    
    return answer;
}