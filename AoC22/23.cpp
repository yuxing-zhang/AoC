#include <iostream>
#include <fstream>
#include <array>
#include <map>
#include <set>

typedef std::set<std::array<int, 2>> pos_set;
typedef std::map<std::array<int, 2>, pos_set> pos_map;

std::array<std::array<int, 2>, 4> cycle{{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

bool run(pos_set& pos, int i) {
    pos_map candi;
    std::array<int, 2> di;
    int j, x, y;
    bool moved = false;
    for (auto& p : pos)
        if (pos.count({p[0] - 1, p[1] - 1}) || pos.count({p[0] - 1, p[1]}) ||
                pos.count({p[0] - 1, p[1] + 1}) ||
                pos.count({p[0], p[1] - 1}) ||
                pos.count({p[0], p[1] + 1}) ||
                pos.count({p[0] + 1, p[1] - 1}) ||
                pos.count({p[0] + 1, p[1]}) ||
                pos.count({p[0] + 1, p[1] + 1}))
            for (j = 0; j < 4; ++j) {
                di = cycle[(i + j) % 4];
                x = p[0] + di[0], y = p[1] + di[1];
                if (di[0] && !pos.count({x, y}) && !pos.count({x, y - 1}) &&
                        !pos.count({x, y + 1}) || !pos.count({x, y}) &&
                        !pos.count({x - 1, y}) && !pos.count({x + 1, y})) {
                    candi[{x, y}].insert(p);
                    break;
                }
            }
    for (auto& p : candi)
        if (p.second.size() == 1) {
            pos.insert(p.first);
            pos.erase(*p.second.begin());
            moved = true;
        }
    return moved;
}

int count(pos_set& pos) {
    int xmin = std::numeric_limits<int>::max(), ymin = xmin;
    int xmax = std::numeric_limits<int>::min(), ymax = xmax;
    for (auto& p : pos) {
        if (p[0] < xmin) xmin = p[0];
        if (p[0] > xmax) xmax = p[0];
        if (p[1] < ymin) ymin = p[1];
        if (p[1] > ymax) ymax = p[1];
    }
    return (xmax - xmin + 1) * (ymax - ymin + 1) - pos.size();
}

int main() {
    pos_set pos;
    std::ifstream fin{"input"};
    std::string s;
    int i, j;
    for (i = 0; fin >> s; ++i)
        for (j = 0; j < s.size(); ++j)
            if (s[j] == '#') pos.insert({i, j});
    pos_set pos2{pos};
    for (i = 0; i < 10; ++i) run(pos, i);
    std::cout << count(pos) << '\n';
    for (i = 0; run(pos2, i); ++i) {}
    std::cout << i + 1;
}

