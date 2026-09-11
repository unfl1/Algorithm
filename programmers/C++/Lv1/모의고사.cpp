#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    vector<int> person1 = {1,2,3,4,5};
    vector<int> person2 = {2,1,2,3,2,4,2,5};
    vector<int> person3 = {3,3,1,1,2,2,4,4,5,5};

    int p1=0, p2=0, p3=0;
    
    for (int i=0; i<answers.size(); i++){
      if (answers[i]==person1[i%5]){
        p1++;
      }
      if (answers[i]==person2[i%8]){
        p2++;
      }
      if (answers[i]==person3[i%10]){
        p3++;
      }
    }

    int max_value = max({p1,p2,p3});

    if (p1 == max_value) answer.push_back(1);
    if (p2 == max_value) answer.push_back(2);
    if (p3 == max_value) answer.push_back(3);

    return answer;
}