#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> nums;
    nums.resize(n);
    for (int i=0; i<n; i++){
        nums[i]=s/n;
    }
    
    int rem = s%n;
    
    for (int i=0; i<rem; i++){
        nums[n-1-i]++;
    }
    
    if (nums[0]==0){
        return nums={-1};
    }
    
    return nums;
}