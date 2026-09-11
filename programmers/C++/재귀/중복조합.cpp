# include <iostream>
# include <vector>

using namespace std;

int N;
vector<int> nums;
vector<int> res;

void dfs(int d, int start){
  if (d==N){
    for (int num : res){
      cout << num << " ";
    }
    cout<<"\n";
    return;
  }
  
  for (int i=start; i<N; i++){
    res.push_back(nums[i]);
    dfs (d+1, i);
    res.pop_back();
  }
}

int main(){
  cin >> N;

  nums.resize(N);

  for (int i=0; i<N; i++){
    cin >> nums[i];
  }

  dfs(0,0);

  return 0;
}