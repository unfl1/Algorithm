#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    unordered_map<string, int> pp;

    for (string name : participant){
      pp[name]++;
    }

    for (string name : completion){
      pp[name]--;
    }

    for (pair<const string, int> p : pp){
      if (p.second==1){
        answer = p.first;
      }
    }

    return answer;
}