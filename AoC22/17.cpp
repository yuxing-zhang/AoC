#include <iostream>
#include <fstream>
#include <array>
#include <set>
#include <vector>

typedef std::array<int, 2> Point;

std::vector<Point> get_rock(int i, int h) {
    switch(i) {
        case 0: return {{h + 4, 2}, {h + 4, 3}, {h + 4, 4}, {h + 4, 5}};
        case 1: return {{h + 6, 3}, {h + 5, 2}, {h + 5, 3}, {h + 5, 4},
                        {h + 4, 3}};
        case 2: return {{h + 6, 4}, {h + 5, 4}, {h + 4, 2}, {h + 4, 3},
                        {h + 4, 4}};
        case 3: return {{h + 7, 2}, {h + 6, 2}, {h + 5, 2}, {h + 4, 2}};
        case 4: return {{h + 5, 2}, {h + 5, 3}, {h + 4, 2}, {h + 4, 3}};
    }
}

int fall(const std::string& s, int N) {
    int h = 0, i, j, k, l, n;
    std::set<Point> S;
    std::vector<Point> rock;
    for (n = 0, i = 0; n < N; ++n) {
        rock = get_rock(n % 5, h);
        while (true) {
            j = s[i] == '>' ? 1 : -1, k = 0;
            if (++i == s.size()) i = 0;
            for (const Point& p : rock)
                if (p[1] + j == -1 || p[1] + j == 7 ||
                        S.count({p[0], p[1] + j})) { k = 1; break; }
            if (!k) for (Point& p : rock) p[1] += j;
            k = 0;
            for (const Point& p : rock)
                if (p[0] == 1 || S.count({p[0] - 1, p[1]})) k = 1;
            if (k) {
                for (const Point& p : rock) S.insert(p);
                if ((l = rock[0][0]) > h) h = l;
                break;
            }
            for (Point& p : rock) --p[0];
        }
    }
    return h;
}

int main() {
    std::ifstream fin{"input"};
    std::string s;
    fin >> s;
    std::cout << fall(s, 2022) << '\n';
    long i = (1000000000000 - 23) / 35, j = (1000000000000 - 23) % 35;
    std::cout << 53 * i + fall(s, 23 + j);
}
