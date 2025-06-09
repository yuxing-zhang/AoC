#include <iostream>
#include <fstream>
#include <set>

int main() {
    std::string s;
    {
        std::ifstream fin{"input"};
        int sum = 0;
        while (fin >> s) {
            std::set<char> t(s.begin() + s.size() / 2, s.end());
            char c;
            for (int i = 0; i < s.size() / 2; ++i)
                if (t.count(s[i])) c = s[i];
            if (c > 'Z') sum += c - 'a' + 1;
            else sum += c - 'A' + 27;
        }
        std::cout << sum << '\n';
    }

    int sum = 0;
    std::ifstream fin{"input"};
    while (fin >> s) {
        std::set<char> t(s.begin(), s.end());
        fin >> s;
        std::set<char> t1(s.begin(), s.end());
        fin >> s;
        for (char c : s)
            if (t.count(c) && t1.count(c)) {
                if (c > 'Z') sum += c - 'a' + 1;
                else sum += c - 'A' + 27;
                break;
            }
    }
    std::cout << sum << '\n';
}
