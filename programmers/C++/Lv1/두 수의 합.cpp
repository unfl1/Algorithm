# include <string>
# include <algorithm>

using namespace std;

string solution(string a, string b){
  string answer = "";

  reverse(a.begin(), a.end());
  reverse(b.begin(), b.end());

  int carry = 0;
  int n = max(a.size(), b.size());

  for (int i=0; i<n; i++){
    int l = (i<a.size())? a[i]-'0':0;
    int r = (i<b.size())? b[i]-'0':0;

    int sum = l + r + carry;
    
    answer += (sum%10) + '0';
    carry = sum/10;
  }

  if (carry>0){
    answer = carry + '0';
  }

  reverse(answer.begin(), answer.end());

  return answer;
}