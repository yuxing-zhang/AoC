#include <iostream>
#include <fstream>

bool check(int a0, int b0, int a1, int b1) {
    return a0 <= a1 && b1 <= b0 || a1 <= a0 && b0 <= b1;
}

bool check2(int a0, int b0, int a1, int b1) {
    return a1 <= b0 && b0 <= b1 || b1 < b0 && a0 <= b1;
}

int main() {
    std::ifstream fin{"input"};
    int i, j, a0, b0, a1, b1, c = 0, c2 = 0;
    for (std::string s; std::getline(fin, s);) {
        i = s.find('-'), j = s.find(',');
        a0 = stoi(s.substr(0, i)), b0 = stoi(s.substr(i + 1, j - i - 1));
        i = s.find('-', j);
        a1 = stoi(s.substr(j + 1, i - j - 1)), b1 = stoi(s.substr(i + 1));
        if (check(a0, b0, a1, b1)) ++c;
        if (check2(a0, b0, a1, b1)) ++c2;
    }
    std::cout << c << ' ' << c2 << '\n';
}
