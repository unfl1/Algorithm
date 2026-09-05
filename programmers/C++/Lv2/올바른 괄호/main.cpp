#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> st;

    for (char i : s){
        if (i=='('){
            st.push(i);
        } else {
            if (st.size() == 0){
                return false;
            }
            st.pop();
        }
    }

    return st.size()==0;
}