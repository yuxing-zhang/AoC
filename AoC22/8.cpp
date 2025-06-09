#include <iostream>
#include <fstream>
#include <set>
#include <vector>


int main() {
    std::vector<std::vector<int>> M;
    std::ifstream fin{"input"};
    int i = 0, m, n, s = 0;
    for (std::string s; std::getline(fin, s);) {
        M.push_back({});
        for (char c : s) M[i].push_back(c - '0');
        ++i;
    }
    m = i, n = M[0].size();

    std::vector<std::vector<int>> L(m, std::vector<int>(n, -1));
    std::vector<std::vector<int>> R(m, std::vector<int>(n, n));
    std::vector<std::vector<int>> U(m, std::vector<int>(n, -1));
    std::vector<std::vector<int>> D(m, std::vector<int>(n, m));
    std::vector<int> stk;
    for (int i = 0; i < m; ++i) {
        stk.clear();
        for (int j = 0; j < n; ++j) {
            while (!stk.empty() && M[i][stk.back()] <= M[i][j]) {
                R[i][stk.back()] = j;
                stk.pop_back();
            }
            stk.push_back(j);
        }
        stk.clear();
        for (int j = 0; j < n; ++j) {
            while (!stk.empty() && M[i][stk.back()] < M[i][j]) stk.pop_back();
            if (!stk.empty()) L[i][j] = stk.back();
            stk.push_back(j);
        }
    }
    for (int j = 0; j < n; ++j) {
        stk.clear();
        for (int i = 0; i < m; ++i) {
            while (!stk.empty() && M[stk.back()][j] <= M[i][j]) {
                D[stk.back()][j] = i;
                stk.pop_back();
            }
            stk.push_back(i);
        }
        stk.clear();
        for (int i = 0; i < m; ++i) {
            while (!stk.empty() && M[stk.back()][j] < M[i][j]) stk.pop_back();
            if (!stk.empty()) U[i][j] = stk.back();
            stk.push_back(i);
        }
    }
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            if (U[i][j] == -1 || D[i][j] == m || L[i][j] == -1 || R[i][j] == n)
                ++s;
    std::cout << s << '\n';

    s = 0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j) {
            if (L[i][j] == -1) ++L[i][j];
            if (R[i][j] == n) --R[i][j];
            if (U[i][j] == -1) ++U[i][j];
            if (D[i][j] == m) --D[i][j];
            s = std::max(s, (j - L[i][j]) * (R[i][j] - j) * (i - U[i][j]) *
                    (D[i][j] - i));
        }
    std::cout << s << '\n';
}
