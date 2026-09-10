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

    // 둘을 앞뒤로 붙여보고, 더 큰 쪽이 앞에 오게 정렬한다
    sort(numb.begin(), numb.end(), [] (string a, string b){
      return a+b > b+a;
    });

    for (string s : numb){
      answer+=s;
    }

    if (answer[0]=='0'){
      return "0";
    }

    return answer;
}