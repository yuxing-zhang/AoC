#include <vector>
#include <string>
#include <map>
#include <array>
#include <fstream>
#include <iostream>

std::vector<const std::string> map;
typedef std::map<std::array<int, 4>, std::array<int, 4>> nxt_t;
nxt_t nxt1, nxt2;
std::map<std::pair<int, int>, int> d_score{{{0, 1}, 0}, {{1, 0}, 1},
        {{0, -1}, 2}, {{-1, 0}, 3}};

const int N = 50;
int right[4 * N], bot[3 * N];
int left[4 * N], top[3 * N];

void run(nxt_t& nxt, const std::string& path) {
    int x{0}, y{N}, dx{0}, dy{1}, nx, ny, pdx, pdy, t;
    int i, j, k, mv;
    for (i = 0; i < path.size(); ++i) {
        if (path[i] < 'A') {
            j = i;
            while (i < path.size() && path[i] < 'A') ++i;
            mv = stoi(path.substr(j, i-- - j));
            for (k = 0; k < mv; ++k) {
                nx = x + dx, ny = y + dy;
                pdx = dx, pdy = dy;
                if (0 > nx || nx >= bot[y] || 0 > ny || ny >= right[x] ||
                        map[nx][ny] == ' ')
                    std::tie(nx, ny, dx, dy) = nxt[{x, y, dx, dy}];
                if (map[nx][ny] == '#') {
                    dx = pdx, dy = pdy;
                    break;
                }
                x = nx, y = ny;
            }
        }
        else if (path[i] == 'L') t = dx, dx = -dy, dy = t;
        else if (path[i] == 'R') t = dx, dx = dy, dy = -t;
    }
    std::cout << 1000 * (x + 1) + 4 * (y + 1) + d_score[{dx, dy}] << '\n';
}
int main() {
    std::ifstream ifs{"input"};
    std::string s;
    map.reserve(200);
    while (std::getline(ifs, s) && s.size()) map.push_back(s);
    std::getline(ifs, s);
    const std::string path = s;
    for (int i = 0; i < N; ++i) {
        nxt1[{i, N, 0, -1}] = {i, 3 * N - 1, 0, -1};
        nxt1[{i, 3 * N - 1, 0, 1}] = {i, N, 0, 1};
        nxt1[{i + N, N, 0, -1}] = {i + N, 2 * N - 1, 0, -1};
        nxt1[{i + N, 2 * N - 1, 0, 1}] = {i + N, N, 0, 1};
        nxt1[{i + 2 * N, 0, 0, -1}] = {i + 2 * N, 2 * N - 1, 0, -1};
        nxt1[{i + 2 * N, 2 * N - 1, 0, 1}] = {i + 2 * N, 0, 0, 1};
        nxt1[{i + 3 * N, 0, 0, -1}] = {i + 3 * N, N - 1, 0, -1};
        nxt1[{i + 3 * N, N - 1, 0, 1}] = {i + 3 * N, 0, 0, 1};
        nxt1[{2 * N, i, -1, 0}] = {4 * N - 1, i, -1, 0};
        nxt1[{4 * N - 1, i, 1, 0}] = {2 * N, i, 1, 0};
        nxt1[{0, i + N, -1, 0}] = {3 * N - 1, i + N, -1, 0};
        nxt1[{3 * N - 1, i + N, 1, 0}] = {0, i + N, 1, 0};
        nxt1[{0, i + 2 * N, -1, 0}] = {N - 1, i + 2 * N, -1, 0};
        nxt1[{N - 1, i + 2 * N, 1, 0}] = {0, i + 2 * N, 1, 0};

        nxt2[{i, N, 0, -1}] = {3 * N - 1 - i, 0, 0, 1};
        nxt2[{3 * N - 1 - i, 0, 0, -1}] = {i, N, 0, 1};
        nxt2[{i + N, N, 0, -1}] = {2 * N, i, 1, 0};
        nxt2[{2 * N, i, -1, 0}] = {i + N, N, 0, 1};
        nxt2[{i + 3 * N, 0, 0, -1}] = {0, i + N, 1, 0};
        nxt2[{0, i + N, -1, 0}] = {i + 3 * N, 0, 0, 1};
        nxt2[{i + 3 * N, N - 1, 0, 1}] = {3 * N - 1, i + N, -1, 0};
        nxt2[{3 * N - 1, i + N, 1, 0}] = {i + 3 * N, N - 1, 0, -1};
        nxt2[{i + 2 * N, 2 * N - 1, 0, 1}] = {N - 1 - i, 3 * N - 1, 0, -1};
        nxt2[{N - 1 - i, 3 * N - 1, 0, 1}] = {i + 2 * N, 2 * N - 1, 0, -1};
        nxt2[{i + N, 2 * N - 1, 0, 1}] = {N - 1, 2 * N + i, -1, 0};
        nxt2[{N - 1, 2 * N + i, 1, 0}] = {i + N, 2 * N - 1, 0, -1};
        nxt2[{0, i + 2 * N, -1, 0}] = {4 * N - 1, i, -1, 0};
        nxt2[{4 * N - 1, i, 1, 0}] = {0, i + 2 * N, 1, 0};

        right[i] = 3 * N;
        right[i + N] = 2 * N;
        right[i + 2 * N] = 2 * N;
        right[i + 3 * N] = N;
        bot[i] = 4 * N;
        bot[i + N] = 3 * N;
        bot[i + 2 * N] = N;
    }
    run(nxt1, path);
    run(nxt2, path);
}
