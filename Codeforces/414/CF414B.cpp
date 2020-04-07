// https://codeforces.com/contest/414/problem/B
// CodeForces Round 240
// B. Mashmokh and ACM

#include <iostream>
int dp[2][n_+1];
int mod = 1000000007;

int solve(int n_, int k_) {

    // int divisorList[n_][];
    
    // init first row of dp
    for(int i = 1; i <= n_; i++)
        dp[0][i] = 1;
    

    for(int k = 1; k < k_; k++) {
        for(int n = 1; n <= n_; n++) {
            int total = 0;
            for(int i = 1; i <= n; i++) {
                total = (n % i == 0) ? (total + dp[ (k-1)%2 ][i]) : total;
                total = total >= mod ? total - mod : total;
            }
            dp[(k%2)][n] = total;
        }
    }

    int ans = 0;
    for(int i = 1; i <= n_; i++) {
        ans += dp[((k_+1)%2)][i];
        ans = ans >= mod ? ans - mod : ans;
    }
    return ans;
}

int main(int argc, const char* argv[]) {

    
    int n_, k_;
    std::cin >> n_ >> k_;
    std::cout << (solve(n_, k_));
}