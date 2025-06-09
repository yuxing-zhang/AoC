#include <iostream>
#include <fstream>
#include <set>
#include <array>

int main() {
    int reg = 1;
    std::ifstream fin{"input"};
    int i = 0, sum = 0;
    for (std::string s; std::getline(fin, s);)
        if (s[0] == 'n') {
            if (++i % 40 == 20) {
                sum += reg * i;
                if (i == 220) break;
            }
        }
        else {
            bool _220 = false;
            for (int j = 0; j < 2; ++j)
                if (++i % 40 == 20) {
                    sum += reg * i;
                    if (i == 220) _220 = true;
                }
            if (_220) break;
            reg += stoi(s.substr(s.find(' ') + 1));
        }
    std::cout << sum << '\n';

    i = 0, reg = 1;
    fin.seekg(0);
    std::set<std::array<int, 2>> lit;
    for (std::string s; std::getline(fin, s);) {
        if (i == 240) break;
        if (s[0] == 'n') {
            if (int j = (i++ % 40); j < reg + 2 && reg - 2 < j)
                lit.insert({(i - 1) / 40, j});
        }
        else {
            for (int j = 0; j < 2; ++j)
                if (int j = (i++ % 40); j < reg + 2 && reg - 2 < j)
                    lit.insert({(i - 1) / 40, j});
            reg += stoi(s.substr(s.find(' ') + 1));
        }
    }
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 40; ++j)
            putchar(lit.count({i, j}) ? '#' : '.');
            putchar('\n');
        }
}
