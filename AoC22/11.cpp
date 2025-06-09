#include <iostream>
#include <fstream>
#include <vector>
#include <array>

std::vector<std::array<int, 3>> paras;
std::vector<long> counts;
std::vector<std::array<int, 2>> ops;
int n;

int test(int i, long& j) {
    if (int k = ops[i][1]; ops[i][0])
        if (k) j = j * k / 3;
        else j = j * j  / 3;
    else j = (j + k) / 3;
    return j % paras[i][0] == 0 ? paras[i][1] : paras[i][2];
}

int test(int i, std::vector<int>& j) {
    if (int k = ops[i][1]; ops[i][0])
        if (k) for (int i = 0; i < n; ++i) j[i] = j[i] * k % paras[i][0];
        else for (int i = 0; i < n; ++i) j[i] = j[i] * j[i] % paras[i][0];
    else for (int i = 0; i < n; ++i) j[i] = (j[i] + k) % paras[i][0];
    return j[i] == 0 ? paras[i][1] : paras[i][2];
}

template<class T>
void run(std::vector<std::deque<T>>& items) {
    T j;
    for (int i = 0; i < n; ++i) {
        while (!items[i].empty()) {
            ++counts[i];
            j = items[i].front();
            items[i].pop_front();
            items[test(i, j)].push_back(j);
        }
    }
}

int main() {
    std::ifstream fin{"input"};
    std::vector<std::deque<long>> items;
    std::vector<std::deque<std::vector<int>>> items2;
    int i = 0, j;
    for (std::string s; std::getline(fin, s);) {
        if (!s.size()) { ++i; continue; }
        std::getline(fin, s);
        items.push_back({});
        for (j = 0; (j = s.find(',', j) + 1);)
            items[i].push_back(stoi(s.substr(j - 3, 2)));
        items[i].push_back(stoi(s.substr(s.size() - 2, 2)));
        std::getline(fin, s);
        if ((j = s.find('+')) != -1)
            ops.push_back({0, stoi(s.substr(j + 2))});
        else if (s[s.size() - 1] < 'a')
            ops.push_back({1, stoi(s.substr(s.size() - 2))});
        else ops.push_back({1, 0});
        std::getline(fin, s);
        paras.push_back({});
        j = s.find('y');
        paras[i][0] = stoi(s.substr(j + 2));
        std::getline(fin, s);
        paras[i][1] = stoi(s.substr(s.size() - 1));
        std::getline(fin, s);
        paras[i][2] = stoi(s.substr(s.size() - 1));
    }
    n = i + 1;
    for (i = 0; i < n; ++i) {
        items2.push_back({});
        for (long j : items[i]) {
            std::vector<int> v;
            for (int i = 0; i < n; ++i) v.push_back(j % paras[i][0]);
            items2[i].push_back(v);
        }
    }

    counts.insert(counts.begin(), n, 0);
    for (i = 0; i < 20; ++i) run(items);
    make_heap(counts.begin(), counts.end());
    pop_heap(counts.begin(), counts.end());
    pop_heap(counts.begin(), counts.end() - 1);
    std::cout << counts[n - 2] * counts[n - 1] << '\n';

    for (auto& i : counts) i = 0;
    for (i = 0; i < 10000; ++i) run(items2);
    make_heap(counts.begin(), counts.end());
    pop_heap(counts.begin(), counts.end());
    pop_heap(counts.begin(), counts.end() - 1);
    std::cout << counts[n - 2] * counts[n - 1] << '\n';
}
