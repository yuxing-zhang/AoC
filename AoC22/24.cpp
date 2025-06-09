#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <array>
#include <list>

typedef std::map<std::array<int, 2>, std::set<std::array<int, 2>>> Map;

int M, N;
Map map;

Map move_bliz(const Map& map) {
    Map nxt;
    for (auto& p : map)
        for (auto& a : p.second)
            nxt[{(p.first[0] + a[0] + M) % M,
                    (p.first[1] + a[1] + N) % N}].insert(a);
    return nxt;
}

int move(int x0, int y0, int x1, int y1) {
    std::list<std::array<int, 3>> q{{0, x0, y0}};
    std::set<std::array<int, 3>> vstd;
    std::array<int, 3> node, nxt;
    int i, j, x, y, step = -1;
    while (true) {
        node = q.front();
        q.pop_front();
        if (node[0] > step) {
            ++step;
            map = move_bliz(map);
            vstd.clear();
        }
        if (node[1] == x1 && node[2] == y1) break;
        for (i = -1; i < 2; ++i)
            for (j = -1 + abs(i); j < 2 - abs(i); ++j) {
                x = node[1] + i, y = node[2] + j;
                if (0 <= x && x < M && 0 <= y && y < N && !map.count({x, y}) ||
                        x == x0 && y == y0) {
                    nxt = {step + 1, x, y};
                    if (!vstd.count(nxt)) {
                        q.push_back(nxt);
                        vstd.insert(nxt);
                    }
                }
            }
    }
    return step;
}

int main() {
    std::ifstream fin{"input"};
    std::string s;
    int i, j;
    for (i = 0; fin >> s; ++i)
        for (j = 0; j < s.size(); ++j)
            switch (s[j]) {
                case '>':
                    map[{i - 1, j - 1}].insert({0, 1});
                    break;
                case '^':
                    map[{i - 1, j - 1}].insert({-1, 0});
                    break;
                case '<':
                    map[{i - 1, j - 1}].insert({0, -1});
                    break;
                case 'v':
                    map[{i - 1, j - 1}].insert({1, 0});
                    break;
            }
    Map map0 = map;
    M = i - 2, N = j - 2;
    std::cout << move(-1, 0, M - 1, N - 1) + 1;
    map = map0;
    std::cout << move(-1, 0, M - 1, N - 1) + move(M, N - 1, 0, 0) +
            move(-1, 0, M - 1, N - 1) + 3;
}
