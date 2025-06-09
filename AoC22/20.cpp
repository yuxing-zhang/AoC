#include <iostream>
#include <fstream>

void move(int* prv, int* nxt, int curr, int step) {
    nxt[prv[curr]] = nxt[curr];
    prv[nxt[curr]] = prv[curr];
    int dest = prv[curr];
    for (int i = 0; i < step; ++i, dest = nxt[dest]) {}
    prv[nxt[dest]] = curr;
    nxt[curr] = nxt[dest];
    nxt[dest] = curr;
    prv[curr] = dest;
}

const int N = 5000, M = 811589153, L = M % (N - 1);

int main() {
    std::ifstream ifs("input");
    int prv[N], nxt[N], v[N], i, j, k, s;
    for (i = 0; i < N; ++i) {
        prv[i] = i - 1;
        nxt[i] = i + 1;
        ifs >> v[i];
        if (v[i] == 0) j = i;
    }
    prv[0] = N - 1, nxt[N - 1] = 0;
    for (k = 0; k < 10; ++k)
        for (i = 0; i < N; ++i) {
            if ((s = L * v[i] % (N - 1)) < 0) s += N - 1;
            move(prv, nxt, i, s);
        }
    for (s = 0, i = 0, k = j; i < 3000; ++i) {
        k = nxt[k];
        if ((i + 1) % 1000 == 0) s += v[k];
    }
    std::cout << (long) M * s;
}
