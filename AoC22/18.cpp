#include <iostream>
#include <fstream>
#include <set>
#include <array>
#include <list>

typedef std::array<int, 3> Node;
std::set<Node> graph;
std::set<Node> vstd;

std::array<Node, 6> neib(const Node& node) {
    return {{
            {node[0] - 1, node[1], node[2]},
            {node[0] + 1, node[1], node[2]},
            {node[0], node[1] - 1, node[2]},
            {node[0], node[1] + 1, node[2]},
            {node[0], node[1], node[2] - 1},
            {node[0], node[1], node[2] + 1},
    }};
}

void vst(const Node& node, const Node& x, const Node& y, int& count) {
    if (node[0] < x[0] || node[0] > y[0] || node[1] < x[1] || node[1] > y[1] ||
            node[2] < x[2] || node[2] > y[2]) return;
    vstd.insert(node);
    for (const auto& u : neib(node))
        if (graph.count(u)) ++count;
        else if (!vstd.count(u)) vst(u, x, y, count);
}

int main() {
    int n = 0, i, j, e = 0;
    std::ifstream fin{"input"};
    std::string s;
    while (fin >> s) {
        ++n;
        i = s.find(',');
        j = s.find(',', i + 1);
        graph.insert({stoi(s.substr(0, i)), stoi(s.substr(i + 1, j - i - 1)),
                stoi(s.substr(j + 1))});
    }
    for (auto& node : graph)
        for (const auto& u : neib(node)) if (graph.count(u)) ++e;
    std::cout << 6 * n - e << '\n';

    std::list<Node> q{{0, 0, 0}};
    Node u;
    bool flag = false;
    while (true) {
        u = q.front();
        q.pop_front();
        for (const auto& v : neib(u)) {
            if (graph.count(v)) { flag = true; break; }
            if (!vstd.count(v)) { vstd.insert(v); q.push_back(v); }
        }
        if (flag) break;
    }
    vstd.clear();
    int count = 0;
    vst(u, {-1, -1, -1}, {20, 20, 20}, count);
    std::cout << count;
}
