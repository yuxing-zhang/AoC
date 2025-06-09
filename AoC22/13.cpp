#include <iostream>
#include <fstream>
#include <stack>
#include <vector>

struct Packet {
    int n;
    std::vector<Packet> chdr;
    Packet() : n(-1), chdr({}) {}
    Packet(int n) : n(n), chdr({}) {}
    Packet(std::string s) {
        std::stack<char> stk;
        std::stack<Packet> pstk;
        for (auto i = s.rbegin(); i != s.rend(); ++i)
            switch (Packet p; *i) {
                case ',': break;
                case ']': stk.push(*i); break;
                case '[':
                    for (char c; (c = stk.top()) != ']'; stk.pop(), pstk.pop())
                        p.chdr.push_back(pstk.top());
                    stk.top() = ' ', pstk.push(p);
                    break;
                case '0':
                    stk.push(*i);
                    if (*++i == '1') pstk.push(Packet(10));
                    else --i, pstk.push(Packet(0));
                    break;
                default: stk.push(*i), pstk.push(Packet(*i - 48));
            }
        *this = pstk.top();
    }
};

void print(const Packet& p) {
    if (p.n != -1) { std::cout << p.n; return; }
    putchar('[');
    for (auto& p : p.chdr) print(p), putchar(',');
    putchar(']');
}

bool operator<(const Packet& l, const Packet& r) {
    int ls = l.chdr.size(), rs = r.chdr.size(), i;
    if (l.n >= 0 && r.n >= 0) return l.n < r.n;
    if (l.n == -1) {
        if (r.n == -1) {
            for (i = 0; i < std::min(ls, rs); ++i) {
                if (l.chdr[i] < r.chdr[i]) return true;
                else if (r.chdr[i] < l.chdr[i]) return false;
            }
            return i == ls && i != rs ? true : false;
        }
        else if (!ls) return true;
        else return l.chdr[0] < r;
    }
    if (!rs) return false;
    else return l < r.chdr[0] || !(r.chdr[0] < l) && rs > 1;
}

bool operator==(const Packet& l, const Packet& r) {
    return !(l < r) && !(r < l);
}

int main() {
    std::ifstream fin{"input"};
    std::stack<char> stk;
    std::stack<Packet> pstk;
    std::vector<Packet> pkts;
    int i = 0, sum = 0, prod = 1;
    for (std::string s; std::getline(fin, s);) {
        if (!s.size()) {
            if (pkts[2 * i] < pkts[2 * i + 1]) sum += i + 1;
            ++i;
            continue;
        }
        pkts.push_back(s);
    }
    if (pkts[2 * i] < pkts[2 * i + 1]) sum += i + 1;
    std::cout << sum << '\n';

    Packet _2{"[[2]]"}, _6{"[[6]]"};
    pkts.push_back(_2), pkts.push_back(_6);
    sort(pkts.begin(), pkts.end());
    for (int i = 0; i < pkts.size(); ++i)
        if (pkts[i] == _2 || pkts[i] == _6) prod *= i + 1;
    std::cout << prod << '\n';
}
