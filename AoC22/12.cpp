#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <map>
#include <queue>

int main() {
    std::vector<std::string> graph;
    std::map<std::array<int, 2>, int> dist;
    std::ifstream fin{"input"};
    int i = 0, j, m, n;
    std::array<int, 2> S, E;
    for (std::string s; std::getline(fin, s); ++i) {
        graph.push_back(s);
        for (j = 0; j < s.size(); ++j)
            if (s[j] == 'S') S = {i, j}, graph[i][j] = 'a';
            else if (s[j] == 'E') E = {i, j}, graph[i][j] = 'z';
    }
    m = i, n = j;
    std::queue<std::array<int, 2>> q;
    q.push(S);
    dist[S] = 0;
    for (std::array<int, 2> u; (u = q.front()) != E;) {
        q.pop();
        for (i = -1; i < 2; ++i)
            for (j = -1 + abs(i); j < 2 - abs(i); ++j) {
                int x = u[0] + i, y = u[1] + j;
                if (0 <= x && x < m && 0 <= y && y < n && !dist.count({x, y})
                        && graph[x][y] - graph[u[0]][u[1]] <= 1) {
                    q.push({x, y});
                    dist[{x, y}] = dist[u] + 1;
                }
            }
    }
    std::cout << dist[E] << '\n';

    while (!q.empty()) q.pop();
    dist.clear();
    q.push(E);
    dist[E] = 0;
    for (std::array<int, 2> u;;) {
        u = q.front();
        if (graph[u[0]][u[1]] == 'a') {
            std::cout << dist[u] << '\n';
            break;
        }
        q.pop();
        for (i = -1; i < 2; ++i)
            for (j = -1 + abs(i); j < 2 - abs(i); ++j) {
                int x = u[0] + i, y = u[1] + j;
                if (0 <= x && x < m && 0 <= y && y < n && !dist.count({x, y})
                        && graph[x][y] - graph[u[0]][u[1]] >= -1) {
                    q.push({x, y});
                    dist[{x, y}] = dist[u] + 1;
                }
            }
    }
}
