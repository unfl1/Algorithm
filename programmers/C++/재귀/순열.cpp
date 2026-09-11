# include <iostream>
# include <string>
# include <vector>

using namespace std;

int N;
vector<int> nums;
vector<bool> selected;

void dfs(int d, vector<int> res){
  if (d==N){
    for (int num : res){
      cout << num << " ";
    }
    cout <<"\n";
    return;
  }

  for (int i=0; i<N; i++){
    if (!selected[i]){
      selected[i]=true;
      res.push_back(nums[i]);
      dfs(d+1, res);
      res.pop_back();
      selected[i]=false;
    }
  }

}

int main(){
  cin >> N;

  nums.resize(N);
  selected.resize(N, false);

  for (int i=0; i<N; i++){
    cin >> nums[i];
  }

  dfs(0, {});

  return 0;
}