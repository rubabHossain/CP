// https://atcoder.jp/contests/abc160
// ABC 160
// D. Line++

#include <iostream>
#include <algorithm>

using namespace std;

int ans[2003];

int main(int argc, const char* argv[]) {

    int N, X, Y;
    cin >> N >> X >> Y;
    for(int i = 1; i < N; i++)
        ans[i] = 0;
    

    for(int i = 1; i <= N; i++) {
        for(int j = i+1; j <= N; j++) {
            int direct = abs(i - j);
            int shortcut1 = abs(i - X) + abs(j - Y) + 1;
            int shortcut2 = abs(j - X) + abs(i - Y) + 1;
            int shortcut = min(shortcut1, shortcut2);
            int dist = min(direct, shortcut);
            ans[dist]++;
        }
    }

    for(int i = 1; i < N; i++)
        cout << ans[i] << endl;
    
}