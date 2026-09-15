#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

struct Car {
    bool is_in = false;
    int in_time = 0;
    int total_time = 0;
};

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    map<string, Car> park;
    
    for (string record : records) {
        stringstream ss(record);
        
        string time;
        string num;
        string inout;
        
        ss >> time >> num >> inout;
        
        // 들어오거나 나간 시각 -> "분"으로 표시
        int h = stoi(time.substr(0, 2));
        int m = stoi(time.substr(3, 2));

        int total_minute = h * 60 + m;
        
        // in, out 상태 처리
        if (inout == "IN") {
            park[num].is_in = true;
            park[num].in_time = total_minute;
        }
        else {
            park[num].total_time += total_minute - park[num].in_time;
            park[num].is_in = false;
        }
    }
    
    for (auto& [num, car] : park) {
        
        // 아직 주차장에 남아있는 차량은 23:59에 나간 것으로 처리
        if (car.is_in) {
            car.total_time += (23 * 60 + 59) - car.in_time;
        }
        
        int total = car.total_time;
        int fee = fees[1];
        
        // 기본 시간을 초과한 경우 추가 요금 계산
        if (total > fees[0]) {
            int extra_time = total - fees[0];
            int extra_count = (extra_time + fees[2] - 1) / fees[2];
            
            fee += extra_count * fees[3];
        }
        
        answer.push_back(fee);
    }
    
    return answer;
}