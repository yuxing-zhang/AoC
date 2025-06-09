#include <iostream>
#include <fstream>
#include <map>

int N = 100000, M = 40000000, size = 0, min_size = INT_MAX, excess;

struct File {
    bool type;
    int size;
    std::string name;
    File* prt;
    std::map<std::string, File> chdr;
    File(bool type, int size, std::string name, File* prt) : type(type),
            size(size), name(name), prt(prt), chdr{} {}
    File() = default;
};

void ls(File& f, int n) {
    for (int i = 0; i < n; ++i) putchar(' ');
    std::cout << f.name << ' ' << f.size << '\n';
    for (auto& p : f.chdr) ls(p.second, n + 1);
}

void set_size(File& f) {
    if (!f.type) return;
    for (auto& p : f.chdr) { set_size(p.second); f.size += p.second.size; }
    if (f.size <= N) size += f.size;
}

void find(File& f) {
    if (!f.type || f.size < excess) return;
    if (f.size < min_size) min_size = f.size;
    for (auto& p : f.chdr) find(p.second);
}

int main() {
    std::ifstream fin{"input"};
    std::string s, t;
    bool flg = false;
    File root{1, 0, "/", nullptr}, *fp = &root;
    std::getline(fin, s);
    while (true) {
        if (!flg && !std::getline(fin, s)) break;
        flg = false;
        switch (s[2]) {
            case 'l':
                while (std::getline(fin, s)) {
                    switch (s[0]) {
                        case '$': flg = true; break;
                        case 'd':
                            t = s.substr(4);
                            fp->chdr[t] = {1, 0, t, fp};
                            break;
                        default:
                            int i = s.find(' ');
                            t = s.substr(i + 1);
                            fp->chdr[t] = {0, stoi(s.substr(0, i)), t, fp};
                    }
                    if (flg) break;
                }
                break;
            case 'c':
                switch (s[5]) {
                    case '.': fp = fp->prt; break;
                    default: fp = &fp->chdr[s.substr(5)];
                }
        }
    }
    set_size(root);
    std::cout << size << '\n';

    excess = root.size - M;
    find(root);
    std::cout << min_size;
}
