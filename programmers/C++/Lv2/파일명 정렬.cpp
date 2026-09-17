#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

using namespace std;

struct File {
    string head;
    int number;
    string original;
};

vector<string> solution(vector<string> files) {
    vector<string> answer;
    
    vector<File> filesss;
    
    for (string st : files){
        int idx = 0;
        
        string h = "";
        while (idx<st.size() && !isdigit(st[idx])){
            h+=toupper(st[idx]);
            idx++;
        }
        
        string num = "";
        while (idx<st.size() && isdigit(st[idx])){
            num+=st[idx];
            idx++;
        }
        
        filesss.push_back({h, stoi(num), st});
    }
    
    stable_sort(filesss.begin(), filesss.end(),
                [](const File& a, const File& b){
                  if (a.head!=b.head){
                    return a.head < b.head;
                  }

                  return a.number<b.number;
                });
    
    for (const File& f : filesss){
        answer.push_back(f.original);
    }
    
    return answer;
}