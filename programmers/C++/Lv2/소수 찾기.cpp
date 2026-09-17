#include <string>
#include <vector>
#include <cmath>
#include <unordered_set>

using namespace std;

string num;
vector<bool> visited;
int cnt;
unordered_set<int> num_set;

bool isprime(string num){
    int n = stoi(num);
    
    if (n<2){
        return false;
    }
    
    for (int i=2; i<=sqrt(n); i++){
        if (n%i==0){
            return false;
        }
    }
    
    return true;
}

void dfs (int d, string cur, int length){
    if (d==length) {
        if (isprime(cur)){
            int icur = stoi(cur);
            if (num_set.find(icur) == num_set.end()){
                num_set.insert(icur);
                cnt++;
            }
        }
        return;
    }
    
    for (int i=0; i<num.size(); i++){
        if (!visited[i]){
            visited[i]=true;
            dfs(d+1, cur+num[i], length);
            visited[i]=false;
        }
    }
}

int solution(string numbers) {

    num = numbers;
    visited.assign(numbers.size(), false);
    cnt = 0;
    
    for (int len=1; len<=numbers.length(); len++){
        dfs(0,"",len);
    }
    
    return cnt;
}