#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::vector<int> elf{0};
    int n = 0;
    std::ifstream fin{"input"};
    for (std::string s; std::getline(fin, s);) {
        if (!s.size()) { n = std::max(n, elf.back()); elf.push_back(0); }
        else elf.back() += stoi(s);
    }
    n = std::max(n, elf.back());
    std::cout << n << '\n';

    make_heap(elf.begin(), elf.end());
    for (int i = 0; i < 3; ++i)
        pop_heap(elf.begin(), elf.end() - i);
    n = 0;
    for (int i = 0; i < 3; ++i) n += elf.rbegin()[i];
    std::cout << n << '\n';
}
