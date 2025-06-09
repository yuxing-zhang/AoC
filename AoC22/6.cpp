#include <iostream>
#include <fstream>
#include <map>

void find(const std::string& s, int n) {
    std::map<char, int> ct;
    int i;
    for (i = 0; i < s.size(); ++i) {
        ct[s[i]] += 1;
        if (i >= n && !--ct[s[i - n]]) ct.erase(s[i - n]);
        if (ct.size() == n) break;
    }
    std::cout << i + 1 << '\n';
}
 
int main() {
    std::string s;
    std::ifstream fin{"input"};
    fin >> s;
    find(s, 4), find(s, 14);
}
