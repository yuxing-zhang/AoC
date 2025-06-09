#include <iostream>
#include <fstream>
#include <set>
#include <array>

std::set<std::array<int, 2>> vstd;
int xh, yh, xt, yt;
int X[10], Y[10];

void move(int x, int y, int n) {
    for (int i = 0; i < n; ++i) {
        if (xh == xt && yh != yt || xh != xt && yh == yt) {
            if (x == xh - xt && y == yh - yt)
                xt = xh, yt = yh;
        }
        else if (xh != xt && yh != yt)
            if (x == xh - xt || y == yh - yt)
                xt = xh, yt = yh;
        xh += x, yh += y;
        vstd.insert({xt, yt});
    }
}

void move10(int x, int y, int n) {
    for (int i = 0; i < n; ++i) {
        X[0] += x, Y[0] += y;
        for (int j = 0, i, k; j < 9; ++j) {
            if (i = X[j] - X[j + 1], k = Y[j] - Y[j + 1], abs(i) == 2 || abs(k) == 2) {
                    X[j + 1] += i / std::max(abs(i), 1);
                    Y[j + 1] += k / std::max(abs(k), 1);
            }
            else break;
       }
        vstd.insert({X[9], Y[9]});
    }
}

int main() {
    {
        std::ifstream fin{"input"};
        vstd.insert({0, 0});
        for (std::string s; std::getline(fin, s);) {
            int n = stoi(s.substr(2));
            switch (s[0]) {
                case 'U': move(-1, 0, n); break;
                case 'R': move(0, 1, n); break;
                case 'D': move(1, 0, n); break;
                case 'L': move(0, -1, n); break;
            }
        }
        std::cout << vstd.size() << '\n';
    }
    std::ifstream fin{"input"};
    vstd.clear();
    vstd.insert({0, 0});
    for (std::string s; std::getline(fin, s);) {
        int n = stoi(s.substr(2));
        switch (s[0]) {
            case 'U': move10(-1, 0, n); break;
            case 'R': move10(0, 1, n); break;
            case 'D': move10(1, 0, n); break;
            case 'L': move10(0, -1, n); break;
        }
    }
    std::cout << vstd.size() << '\n';
}
