#include <iostream>
#include <fstream>
#include <list>

void add(std::list<int>& x, const std::list<int>& y) {
    std::list<int>::const_iterator j = y.begin();
    int c = 0, t;
    for (int& i : x) {
        if (j != y.end()) i += *j++;
        else if (c == 0) break;
        if ((i += c) < -2) i += 5, c = -1;
        else if (i > 2) i -= 5, c = 1;
        else c = 0;
    }
    for (; j != y.end(); ++j) {
        if ((t = *j + c) < -2) t += 5, c = -1;
        else if (t > 2) t -= 5, c = 1;
        else c = 0;
        x.push_back(t);
    }
    if (c) x.push_back(c);
}

void print(const std::list<int>& x) {
    for (auto i = x.rbegin(); i != x.rend(); ++i)
        switch (*i) {
            case -2: putchar('='); break;
            case -1: putchar('-'); break;
            default: std::cout << *i;
        }
}

int main() {
    std::list<int> x{0}, y;
    std::ifstream fin{"input"};
    std::string s;
    while (fin >> s) {
        y.clear();
        for (auto i = s.rbegin(); i != s.rend(); ++i)
            switch (*i) {
                case '=': y.push_back(-2); break;
                case '-': y.push_back(-1); break;
                default: y.push_back(*i - 48);
            }
        add(x, y);
    }
    print(x);
}
