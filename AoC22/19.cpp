#include <iostream>
#include <fstream>
#include <array>
#include <unordered_map>

template<>
struct std::hash<std::array<int, 8>> {
    unsigned long operator()(const std::array<int, 8>& arr) const {
        unsigned long hash = arr[5] * 100000 + arr[6] * 100 + arr[7];
        hash *= 1000000000;
        hash += arr[0] * 10000000 + arr[1] * 1000000 + arr[2] * 10000 + arr[3] * 100 + arr[4];
        return hash;
    }
};

std::unordered_map<std::array<int, 8>, int> cache;

int count(std::array<int, 8> env, const std::array<int, 6>& bp) {
    if (env[0] == 1) { return env[4]; } 
    if (cache.count(env)) return cache[env];
    bool ob = false, cl = false, o = false, built[4]{false, false, false, false};
    int c = 0, t;
    if (env[5] >= bp[4] && env[7] >= bp[5] && (
            built[3] = true,
            t = count({env[0] - 1, env[1], env[2], env[3], env[4] + 1,
                env[5] - bp[4] + env[1], env[6] + env[2],
                env[7] - bp[5] + env[3]}, bp) + env[4]
            ) > c)
        c = t;
    if (env[3] < bp[5]) {
        ob = true;
        if(env[5] >= bp[2] && env[6] >= bp[3] && (
                built[2] = true,
                t = count({env[0] - 1, env[1], env[2], env[3] + 1, env[4],
                    env[5] - bp[2] + env[1], env[6] - bp[3] + env[2],
                    env[7] + env[3]}, bp) + env[4]
                ) > c)
            c = t;
    }
    if ((bp[5] - env[3]) * bp[3] > env[6] + env[2] * 2 && env[2] < bp[3]) {
        cl = true;
        if( env[5] >= bp[1] && (
                built[1] = true,
                t = count({env[0] - 1, env[1], env[2] + 1, env[3], env[4],
                    env[5] - bp[1] + env[1], env[6] + env[2], env[7] + env[3]},
                    bp) + env[4]
                ) > c)
            c = t;
    }
    if (env[1] < bp[4] || ob && env[1] < bp[2] || cl && env[1] < bp[1]) {
        o = true;
        if (env[5] >= bp[0] && (
                built[0] = true,
                t = count({env[0] - 1, env[1] + 1, env[2], env[3], env[4],
                    env[5] - bp[0] + env[1], env[6] + env[2], env[7] + env[3]},
                    bp) + env[4]
                ) > c)
            c = t;
    }
    if ((o && env[5] < bp[0] || cl && env[5] < bp[1]
                || ob && (env[5] < bp[2] || env[6] < bp[3] && !(
                    built[0] && env[5] - bp[0] + env[1] >= bp[2]
                    || built[1] && env[5] - bp[1] + env[1] >= bp[2]
                    || built[3] && env[5] - bp[4] + env[1] >= bp[2]))
                || env[5] < bp[4] || env[7] < bp[5] && !(
                    built[0] && env[5] - bp[0] + env[1] >= bp[4]
                        && env[5] - bp[0] - bp[4] + 2 * env[1] >= bp[2]
                    || built[1] && env[5] - bp[1] + env[1] >= bp[4]
                        && env[5] - bp[1] - bp[4] + 2 * env[1] >= bp[2]
                    || built[2] && env[5] - bp[2] + env[1] >= bp[4])) && (
            t = count({env[0] - 1, env[1], env[2], env[3], env[4],
                env[5] + env[1], env[6] + env[2], env[7] + env[3]}, bp)
                + env[4]
            ) > c)
        c = t;
    return cache[env] = c;
}

int main() {
    std::array<int, 6> bp;
    std::ifstream fin{"input"};
    std::string s;
    int j = 0, sum = 0, prod = 1;
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
                cache.clear();
                sum += count({24, 1, 0, 0, 0, 0, 0, 0}, bp) * ++j;
                if (j == 1 || j == 2 || j == 3)
                    prod *= count({32, 1, 0, 0, 0, 0, 0, 0}, bp);
        }
    std::cout << sum << ' ' << prod << '\n';
}
