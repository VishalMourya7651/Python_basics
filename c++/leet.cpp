// Online C++ compiler to run C++ program online
#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
int main() {
    int n=18;
    vector<int>ans;
    
    while(n>0){
        if(n%2==1) ans.push_back(1);
        else ans.push_back(0);
        n/=2;
    }
    vector<int>a;
    // reverse(ans.begin(),ans.end());
    for(int i=0;i<ans.size();i++){
        if(ans[i]*2!=0) a.push_back(pow(2,i));
    }
    for(int i=0;i<a.size();i++){
        cout<<a[i]<<" ";
    }
    return 0;
}