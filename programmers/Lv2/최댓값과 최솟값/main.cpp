#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
    stringstream ss(s);

    vector<int> num;
    int n;

    while (ss >> n){
        num.push_back(n);
    }

    int minNum = *min_element(num.begin(), num.end());
    int maxNum = *max_element(num.begin(), num.end());

    return to_string(minNum) + " " + to_string(maxNum);
}