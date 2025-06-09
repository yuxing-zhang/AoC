#include <iostream>
#include <fstream>

int main() {
    std::ifstream fin{"input"};
    int i, j, s1 = 0, s2;
    for (std::string s; std::getline(fin, s);) {
        i = s[0] - 'A', j = s[2] - 'X';
        switch (j - i) {
            case 0: s1 += 3 + j + 1; break;
            case 1: s1 += 6 + j + 1; break;
            case -2: s1 += 6 + j + 1; break;
            case -1: s1 +=  j + 1; break;
            case 2: s1 += j + 1; break;
        }
        switch (i + j - 1) {
            case 0: s2 += j * 3 + 1; break;
            case 1: s2 += j * 3 + 2; break;
            case 2: s2 += j * 3 + 3; break;
            case 3: s2 += j * 3 + 1; break;
            case -1: s2 += j * 3 + 3; break;
        }
    }
    std::cout << s1 << ' ' << s2 << '\n';
}
