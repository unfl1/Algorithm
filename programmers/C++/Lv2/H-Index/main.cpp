#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    
    sort(citations.begin(), citations.end());
    
    int left = 0;
    int right = citations.back();
    
    while (left<=right){
        int mid = (left+right)/2;
        
        int cnt = 0;
        
        for (int i=0; i<citations.size(); i++){
            if (citations[i]>=mid){
                cnt++;
            }
        }
        
        if (cnt>=mid){
            left=mid+1;
        } else {
            right=mid-1;
        }
    }
    return right;
}