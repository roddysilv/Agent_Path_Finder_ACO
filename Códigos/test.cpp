#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>
#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <sstream>

using namespace std;

vector<vector<pair<int,int>>> vetore;

void leTour(string tour)
{
    vector<pair<int,int>> v;
    pair<int,int> no;
    string s;
    ifstream file;
    file.open(tour);
    file>>s;
    int t = stoi(s);
    for(int i = 0; i < 10  ; i++)
    {
        for(int j = 0; j < t  ; j++)
        {
            file>>s;
            cout<<s<<" ";
            no.first = stoi(s);
            file>>s;
            cout<<s<<" ";
            no.second = stoi(s);
            v.push_back(no);
        }
        cout<<endl;
        vetore.push_back(v);
        v.clear();
    }
}

int main()
{

    leTour("../Instâncias/Tour/10 buscas/Tour_M_20x20.txt");

    cout <<endl<<endl;

    for(int i = 0; i < vetore.size();i++){
        for(int j = 0;  j< vetore[i].size();j++){
            cout << vetore[i][j].first << " " << vetore[i][j].second << endl;
        }
        cout << endl;
    }



    return 0;
}
