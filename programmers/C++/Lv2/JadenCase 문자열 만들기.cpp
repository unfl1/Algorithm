#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    bool first = true;
    
    for (char& c : s){
        if (c==' '){
            first=true;
        }
        else {
            if (first){
                c=toupper(c);
                first=false;
            } else {
                c=tolower(c);
            }
        }
    }
    
    return s;
}