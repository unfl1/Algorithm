#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int solution(vector<int> nums)
{
    unordered_set<int> ponketmon;
    for (int num : nums){
        ponketmon.insert(num);
    }

    return min(ponketmon.size(), nums.size()/2);
}