#include <iostream>
#include <fstream>
#include <deque>
#include <vector>

void move(std::vector<std::deque<char>>& crates, int n, int from, int to) {
    for (int i = 0; i < n; ++i) {
        crates[to].push_back(crates[from].back());
        crates[from].pop_back();
    }
}

void move2(std::vector<std::deque<char>>& crates, int n, int from, int to) {
    std::deque<char> t;
    for (int i = 0; i < n; ++i) {
        t.push_back(crates[from].back());
        crates[from].pop_back();
    }
    for (int i = 0; i < n; ++i) {
        crates[to].push_back(t.back());
        t.pop_back();
    }
}

int main() {
    std::ifstream fin{"input"};
    std::vector<std::deque<char>> crates, crates2;
    std::string s;
    std::getline(fin, s);
    for (int i = 1; i < s.size(); i += 4) {
        crates.push_back({});
        if (s[i] != ' ') crates[i / 4].push_front(s[i]);
    }
    while (std::getline(fin, s)) {
        if (s[0] == ' ') break;
        for (int i = 1; i < s.size(); i += 4)
            if (s[i] != ' ') crates[i / 4].push_front(s[i]);
    }
    crates2 = crates;
    std::getline(fin, s);
    for (int i, j, from, to, n; std::getline(fin, s);) {
        i = s.find(' '), j = s.find(' ', i + 1);
        n = stoi(s.substr(i + 1, j - i - 1));
        i = s.find(' ', j + 1), j = s.find(' ', i + 1);
        from = stoi(s.substr(i + 1, j - i - 1)) - 1;
        i = s.find(' ', j + 1);
        to = stoi(s.substr(i + 1)) - 1;
        move(crates, n, from, to);
        move2(crates2, n, from, to);
    }
    for (auto& c : crates) putchar(c.back());
    putchar('\n');
    for (auto& c : crates2) putchar(c.back());
    putchar('\n');
}
