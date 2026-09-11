#include <string>
#include <cmath>

using namespace std;

int divisor(int n){
  int cnt = 0;

  int m = (int) sqrt(n);

  for (int i=1; i<m; i++){
    if (n%i==0) cnt+=2;
  }

  if (m*m==n){
    cnt--;
  }

  return (cnt%2==0)? n : -n;
}

int solution(int left, int right) {
    int answer = 0;

    for (int i = left; i<=right; i++){
      answer+=divisor(i);
    }

    return answer;
}