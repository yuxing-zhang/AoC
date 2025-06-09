#include <iostream>
#include <fstream>
#include <array>
#include <vector>
#include <unordered_map>

template<int N>
struct std::hash<std::array<int, N>> {
    unsigned long operator()(const std::array<int, N>& arr) const noexcept {
        unsigned long s = 0;
        for (auto i = arr.rbegin(); i != arr.rend(); ++i) s = s * 100 + *i;
        return s;
    }
};

std::unordered_map<std::string, int> rate;
std::vector<int> rate_;
std::unordered_map<std::string, std::vector<std::string>> graph;
std::vector<std::vector<int>> sketch;
std::vector<bool> vstd;
std::unordered_map<std::array<int, 6>, int> cache;
int n;

int count(int t, int pos) {
    int ss = 0, s = 0, r;
    for (int i = 0; i < n; ++i) if (vstd[i]) ss += rate_[i];
    s = ss * t;
    for (int i = 0; i < n; ++i)
        if (!vstd[i] && (r = sketch[pos][i] + 1) < t) {
            vstd[i] = true;
            s = std::max(s, count(t - r, i) + ss * r);
            vstd[i] = false;
        }
    return s;
}

int count(int t, int x, int tx, int y, int ty) {
    int v = 0;
    for (int i : vstd) v = (v << 1) + i;
    try { return cache.at({t, x, tx, y, ty, v}); }
    catch (std::out_of_range&) {
        try { return cache.at({t, y, ty, x, tx, v}); }
        catch (std::out_of_range&) {}
    }
    bool xdone = true, ydone = true;
    int r, s = 0;
    if (!tx)
        for (int i = 0; i < n; ++i)
            if (!vstd[i] && (r = sketch[x][i] + 1) < t) {
                vstd[i] = true;
                xdone = false;
                s = std::max(count(t, i, r, y, ty), s);
                vstd[i] = false;
            }
    if (xdone && !ty)
        for (int i = 0; i < n; ++i)
            if (!vstd[i] && (r = sketch[y][i] + 1) < t) {
                vstd[i] = true;
                ydone = false;
                s = std::max(count(t, x, tx, i, r), s);
                vstd[i] = false;
            }
    if (xdone && ydone) {
        int ss = 0;
        for (int i = 0; i < n; ++i)
            if (vstd[i]) {
                ss += rate_[i];
                if (i == x && tx || i == y && ty) ss -= rate_[i];
            }
        if (!tx)
            if (!ty) s = ss * t;
            else s = count(t - ty, x, 0, y, 0) + ss * ty;
        else
            if (!ty) s = count(t - tx, x, 0, y, 0) + ss * tx;
            else {
                r = std::min(tx, ty);
                s = count(t - r, x, tx - r, y, ty - r) + ss * r;
            }
    }
    return cache[{t, x, tx, y, ty, v}] = s;
}

int main() {
    std::ifstream fin{"input"};
    std::unordered_map<std::string, int> a2i;
    std::string s, u;
    for (int i = 0, j, k; std::getline(fin, s); ++i) {
        u = s.substr(6, 2);
        j = s.find('='), k = s.find(';');
        rate[u] = stoi(s.substr(j + 1, k - j - 1));
        while ((k = s.find(',', k) + 1)) graph[u].push_back(s.substr(k - 3, 2));
        graph[u].push_back(s.substr(s.size() - 2, 2));
    }
    n = graph.size();
    std::vector<std::unordered_map<std::string,
            std::unordered_map<std::string, int>>> dist(n + 1);
    for (const auto& i : graph) {
        for (const auto& j : graph)
            dist[0][i.first][j.first] = 100;
        dist[0][i.first][i.first] = 0;
        for (const auto& j : i.second) dist[0][i.first][j] = 1;
    }
    int l = 0;
    for (const auto& i : graph) {
        const std::string& si = i.first;
        for (const auto& j : graph) {
            const std::string& sj = j.first;
            for (const auto& k : graph) {
                const std::string& sk = k.first;
                dist[l + 1][sj][sk] = std::min(dist[l][sj][sk],
                        dist[l][sj][si] + dist[l][si][sk]);
            }
        }
        ++l;
    }
    n = 0;
    for (const auto& i : graph)
        if (rate[i.first]) {
            rate_.push_back(rate[i.first]);
            sketch.push_back({});
            for (const auto& j : graph)
                if (rate[j.first])
                    sketch[n].push_back(dist[l][i.first][j.first]);
            ++n;
        }
    sketch.push_back({});
    for (const auto& i : graph)
        if (rate[i.first])
                sketch[n].push_back(dist[l]["AA"][i.first]);
    
    vstd.reserve(n);
    vstd.insert(vstd.begin(), n, false);
    std::cout << count(30, n) << ' ' << count(26, n, 0, n, 0) << '\n';
}
