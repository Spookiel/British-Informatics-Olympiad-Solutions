#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<ll> gen(ll limit){
    vector<long long> fibs;
    ll prev = 1;
    ll cur = 1;
    while (cur <= limit)
    {
        fibs.push_back(cur);
        ll tmp = prev;
        prev = cur;
        cur = tmp + cur;
    }
    reverse(fibs.begin(), fibs.end());
    return fibs;
}

vector<ll> zecken(vector<ll> &fibs, ll n){
    vector<ll> ans;
    for(auto x: fibs){
        if(n >= x){
            n -= x;
            ans.push_back(x);
        }
        if(n == 0) break;
    }
    return ans;
}

void partdbrute(){
    /* Takes a couple of mins, must be a better way...*/
    ll ans = 0;
    const ll ULIM = 5000000000;
    const ll LLIM = 1000000000;
    const ll BANNED = 701408733;
    vector<ll> fibs = gen(ULIM);
    vector<ll> fibscop;
    for(auto x: fibs){
        if(x < BANNED) break;
         fibscop.push_back(x);
    }
    for(ll i = LLIM; i <= ULIM; i++){
        auto res = zecken(fibscop, i);
        if(res[res.size()-1] != BANNED)ans++;
    }
    cout << ans << "\n";

}


void partc(){
    /*
    Suppose you have 9 fibs
    1 2 3 5 8 13 21 34 55
    
    Fix each number as in, and then for each number at position p you have (p-2) choices call this p2
    similarly for the third number you have p2-2 choices, note that this means you must have p >= 5
    */
    ll target = 53316291173;
    // ll target = 832040;
    vector<ll> fibs = gen(target);
    int N = (int) fibs.size();
    N -= 1;
    int ans = 0;
    for(int p=5; p <= N; p++){
        for(int p2=3; p2 <= p-2; p2++){
            ans += p2-2;
        }
    }
    cout <<"Part c: " << ans << "\n";

}

int main()
{
    vector<ll> fibs = gen(1e6);
    vector<int> ans;

    int n;
    cin >> n;
    for(auto d: zecken(fibs, n)) cout << d << " ";
    cout << "\n";
    partc();
    // partdbrute();



}

/*
b) Largest Fib under 1e6, which is 832040

c) 18424


*/
