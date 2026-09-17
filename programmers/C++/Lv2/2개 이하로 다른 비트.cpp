#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string tobinary(long long num) {
    string result = "";

    while (num != 0) {
        result += to_string(num % 2);
        num /= 2;
    }

    result += '0';

    return result;
}

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;

    for (long long num : numbers) {
        string binary = tobinary(num);

        for (int i = 0; i < binary.size(); i++) {
            if (binary[i] == '0') {
                binary[i] = '1';

                if (i > 0) {
                    binary[i - 1] = '0';
                }

                break;
            }
        }

        reverse(binary.begin(), binary.end());
        answer.push_back(stoll(binary, nullptr, 2));
    }

    return answer;
}