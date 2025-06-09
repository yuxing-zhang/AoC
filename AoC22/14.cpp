#include <iostream>
#include <fstream>
#include <array>
#include <unordered_set>

template<>
struct std::hash<std::array<int, 2>> {
    size_t operator()(const std::array<int, 2>& arr) const {
        return arr[0] * 1000 + arr[1];
    }
};

std::unordered_set<std::array<int, 2>> rocks;
std::unordered_set<std::array<int, 2>> sands;

bool fall(int ymax, bool p2=false) {
    int x = 500, y = 0;
    if (p2 && sands.count({x, y})) return false;
    while (y < ymax)
        if (!rocks.count({x, y + 1}) && !sands.count({x, y + 1}))
            ++y;
        else if (!rocks.count({x - 1, y + 1}) && !sands.count({x - 1, y + 1}))
            --x, ++y;
        else if (!rocks.count({x + 1, y + 1}) && !sands.count({x + 1, y + 1}))
            ++x, ++y;
        else break;
    if (y == ymax && !p2) return false;
    sands.insert({x, y});
    return true;
}

int main() {
    std::ifstream fin{"input"};
    int i, j, k, x0, y0, x1, y1, z, ymax = 0;
    for (std::string s; std::getline(fin, s);) {
        i = s.find(','), j = s.find(' ', i);
        x0 = stoi(s.substr(0, i)), y0 = stoi(s.substr(i + 1, j - i - 1));
        ymax = y0 > ymax ? y0 : ymax;
        for (k = 0; (k = s.find('>', k) + 1);) {
            i = s.find(',', k), j = s.find(' ', i);
            x1 = stoi(s.substr(k + 1, i - k - 1)), y1 = stoi(s.substr(i + 1, j - i - 1));
            ymax = y1 > ymax ? y1 : ymax;
            if (x0 == x1)
                if (y0 < y1) for (z = y0; z < y1; ++z) rocks.insert({x0, z});
                else for (z = y0; z > y1; --z) rocks.insert({x0, z});
            else if (x0 < x1) for (z = x0; z < x1; ++z) rocks.insert({z, y0});
            else for (z = x0; z > x1; --z) rocks.insert({z, y0});
            x0 = x1, y0 = y1;
        }
        rocks.insert({x1, y1});
    }

    for (i = 0; fall(ymax); ++i);
    std::cout << i << '\n'; 
    for (; fall(ymax + 1, true); ++i);
    std::cout << i << '\n'; 
}
