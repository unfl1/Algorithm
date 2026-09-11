# include <vector>
# include <iostream>

using namespace std;

int N;
vector<int> nums;
vector<int> res;
int target;

void dfs (int d, int start){
  if (d==target){
    for (int num : res){
      cout << num << " ";
    }
    cout << "\n";
    return;
  }

  for (int i=start; i<N; i++){
    res.push_back(nums[i]);
    dfs (d+1, i+1);
    res.pop_back();
  }

}

int main(){
  cin >> N;

  nums.resize(N);

  for (int i=0; i<N; i++){
    cin >> nums[i];
  }

  cin >> target;

  dfs(0, 0);

  return 0;
}