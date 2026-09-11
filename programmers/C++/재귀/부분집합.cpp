# include <iostream>
# include <vector>

using namespace std;

int N;
vector<int> nums;
vector<int> res;

void dfs(int d){

  if (d==N){
    for (int num : res){
    cout << num << " ";
    }
    cout << "\n";
    return;
  }

  // 선택
  res.push_back(nums[d]);
  dfs (d+1);

  res.pop_back();

  // 선택 x
  dfs (d+1);
}

int main(){
  cin >> N;

  nums.resize(N);

  for (int i=0; i<N; i++){
    cin >> nums[i];
  }

  dfs(0);

  return 0;
}