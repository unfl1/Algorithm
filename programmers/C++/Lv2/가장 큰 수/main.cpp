#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> numb;

    for (int num : numbers){
      numb.push_back(to_string(num));
    }

    sort(numb.begin(), numb.end(), [] (string a, string b){
      return a+a+a+a > b+b+b+b;
    });

    for (string s : numb){
      answer+=s;
    }

    if (answer[0]=='0'){
      return "0";
    }

    return answer;
}