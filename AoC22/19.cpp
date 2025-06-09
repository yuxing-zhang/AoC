#include <iostream>
#include <fstream>
#include <array>
#include <map>
#include <list>
#include <unordered_set>

struct Hash {
    unsigned long operator()(const std::array<int, 9>& arr) const {
      unsigned long hash = 0;
      for (int c : arr)
        hash = ((hash << 7) + hash) + c;
      return hash;
    }
};

std::unordered_set<std::array<int, 9>, Hash> cache;

int geo;
void count(std::array<int, 9> env, const std::array<int, 6>& bp) {
    if (env[0] == 24) { geo = geo < env[8] ? env[8] : geo; return; }
    if (cache.count(env)) return;
    cache.insert(env);
    bool ob = false, cl = false, o = false;
    if (env[5] >= bp[4] && env[7] >= bp[5]) count({env[0] + 1, env[1], env[2],
            env[3], env[4] + 1, env[5] - bp[4] + env[1], env[6] + env[2],
            env[7] - bp[5] + env[3], env[8] + env[4]}, bp);
    if (env[3] < bp[5]) {
        ob = true;
        if(env[5] >= bp[2] && env[6] >= bp[3]) count({env[0] + 1, env[1],
                env[2], env[3] + 1, env[4], env[5] - bp[2] + env[1], env[6] -
                bp[3] + env[2], env[7] + env[3], env[8] + env[4]}, bp);
    }
    if ((bp[5] - env[3]) * bp[3] > env[6] + env[2] * 2) {
        cl = true;
        if( env[5] >= bp[1]) count({env[0] + 1, env[1], env[2] + 1, env[3],
                env[4], env[5] - bp[1] + env[1], env[6] + env[2], env[7] +
                env[3], env[8] + env[4]}, bp);
    }
    if (env[1] < bp[4] || ob && env[1] < bp[2] || cl && env[1] < bp[1]) {
        o = true;
        if (env[5] >= bp[0]) count({env[0] + 1, env[1] + 1, env[2], env[3],
                env[4], env[5] - bp[0] + env[1], env[6] + env[2], env[7] +
                env[3], env[8] + env[4]}, bp);
    }
    if (o && env[5] < bp[0] || cl && env[5] < bp[1] || ob && (env[5] < bp[2] ||
            env[6] < bp[3]) || env[5] < bp[4] || env[7] < bp[5])
        count({env[0] + 1, env[1], env[2], env[3], env[4], env[5] + env[1],
                env[6] + env[2], env[7] + env[3], env[8] + env[4]}, bp);
}

int main() {
    std::array<int, 6> bp;
    std::ifstream fin{"input"};
    std::string s;
    int j = 0, sum = 0;
    for (int i = 0; fin >> s; ++i)
        switch (i) {
            case 6: bp[0] = stoi(s); break;
            case 12: bp[1] = stoi(s); break;
            case 18: bp[2] = stoi(s); break;
            case 21: bp[3] = stoi(s); break;
            case 27: bp[4] = stoi(s); break;
            case 30: bp[5] = stoi(s); break;
            case 31:
                i = -1;
                geo = 0, cache.clear();
                count({0, 1, 0, 0, 0, 0, 0, 0, 0}, bp);
                std::cout << geo << std::endl;
                sum += ++j * geo;
        }
    std::cout << sum;
}
