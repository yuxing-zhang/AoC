#include <iostream>
#include <fstream>
#include <vector>
#include <array>

std::vector<std::array<int, 2>> S, B;
std::vector<int> dist;
int n, N = 2000000;

int count(int y) {
    std::vector<std::array<int, 2>> itvs;
    for (int a, b, c, i = 0; i < n; ++i) {
        std::array<int, 2>& s = S[i];
        if ((c = abs(s[1] - y)) > dist[i]) continue;
        a = s[0] + c - dist[i], b = s[0] - c + dist[i] + 1;
        if (B[i][1] == y) {
            if (a == B[i][0]) a = a == s[0] ? a : a + 1;
            b = b - 1 == B[i][0] ? b - 1 : b;
        }
        itvs.push_back({a, 0});
        itvs.push_back({b, 1});
    }
    std::sort(itvs.begin(), itvs.end());
    int s = 0, c = 0, a;
    for (auto& i : itvs)
        if (!i[1]) { if (!c++) a = i[0]; }
        else if (!--c) s += i[0] - a;
    return s;
}

int find(int y, int xmin, int xmax) {
    std::vector<std::array<int, 2>> itvs;
    for (int a, b, c, i = 0; i < n; ++i) {
        std::array<int, 2>& s = S[i];
        if ((c = abs(s[1] - y)) > dist[i]) continue;
        a = s[0] + c - dist[i], b = s[0] - c + dist[i] + 1;
        itvs.push_back({std::max(a, xmin), 0});
        itvs.push_back({std::min(b, xmax), 1});
    }
    std::sort(itvs.begin(), itvs.end());
    int c = 0, a, b;
    for (auto& i : itvs)
        if (!i[1]) { if (!c++ && (a = i[0]) - b == 1) return b; }
        else if (!--c) b = i[0];
    return -1;
}

int main() {
    std::ifstream fin{"input"};
    int i, j;
    for (std::string s; std::getline(fin, s);) {
        S.push_back({});
        B.push_back({});
        i = s.find('='), j = s.find(',', i);
        S.back()[0] = stoi(s.substr(i + 1, j - i - 1));
        i = s.find('=', j), j = s.find(':', i);
        S.back()[1] = stoi(s.substr(i + 1, j - i - 1));
        i = s.find('=', j), j = s.find(',', i);
        B.back()[0] = stoi(s.substr(i + 1, j - i - 1));
        i = s.find('=', j), j = s.size();
        B.back()[1] = stoi(s.substr(i + 1, j - i - 1));
        dist.push_back(abs(S.back()[0] - B.back()[0]) +
                abs(S.back()[1] - B.back()[1]));
    } 
    n = S.size();
    std::cout << count(N) << '\n';
    for (int i = 0; i < 2 * N + 1; ++i)
        if (int x; (x = find(i, 0, 2 * N + 1)) != -1) {
            std::cout << (long) x * 2 * N + i << '\n';
            return 0;
        }
}
