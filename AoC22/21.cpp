#include <map>
#include <vector>
#include <string>
#include <array>
#include <fstream>
#include <iostream>

std::map<std::string, std::array<std::string, 3>> tree;
std::map<std::string, std::pair<std::string, int>> prt;
std::map<std::string, long> cache;

long trvs(const std::string& s) {
    try { return cache.at(s); }
    catch (std::out_of_range&) {
        switch (tree[s][0][0]) {
            case '+': return cache[s] = trvs(tree[s][1]) + trvs(tree[s][2]);
            case '-': return cache[s] = trvs(tree[s][1]) - trvs(tree[s][2]);
            case '*': return cache[s] = trvs(tree[s][1]) * trvs(tree[s][2]);
            case '/': return cache[s] = trvs(tree[s][1]) / trvs(tree[s][2]);
        }
    }
}

long find(const std::string& s, long v) {
    std::pair<std::string, int>& p = prt[s];
    int i = 3 - p.second;
    long j = cache[tree[p.first][i]];
    switch (tree[p.first][0][0]) {
        case '+': return v - j;
        case '-': return i == 1 ? j - v : j + v;
        case '*': return v / j;
        case '/': return i == 1 ? j / v : j * v;
    }
}
int main() {
    std::ifstream ifs{"input"};
    std::string s;
    while (getline(ifs, s))
        if (s[6] < 'A') cache[s.substr(0, 4)] = std::stoi(s.substr(6));
        else {
            tree[s.substr(0, 4)] = {s.substr(11, 1), s.substr(6, 4),
                    s.substr(13)};
            prt[s.substr(6, 4)] = {s.substr(0, 4), 1};
            prt[s.substr(13)] = {s.substr(0, 4), 2};
        }
    std::cout << trvs("root") << '\n';
    std::vector<std::string> stck;
    for (s = "humn"; s != "root"; s = prt[s].first) { stck.push_back(s); }
    long v = cache[tree["root"][3 - prt[stck.back()].second]];
    stck.pop_back();
    while (!stck.empty()) {
        v = find(stck.back(), v);
        stck.pop_back();
    }
    std::cout << v;
}
