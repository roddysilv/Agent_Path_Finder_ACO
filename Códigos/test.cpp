#include <iostream>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int h,w;

vector<vector<char>> G;

void leInstancia(string instancia){

    string s;
    ifstream file;
    file.open(instancia);
    file >> s;
    h = stoi(s);
    file >> s;
    w = stoi(s);

    vector<char> aux;

    for(int i = 0; i < h; i++){
        file >> s;
        for(int j =0;j<w;j++){
            aux.push_back(s[j]);
        }
        G.push_back(aux);
        aux.clear();
    }

}

int main(){

    string instancia = "../Instâncias/M_5x5.txt";

    leInstancia(instancia);

    /*string s;

    ifstream file;
    file.open(instancia);

    file >> s;

    h = stoi(s);

    file >> s;

    w = stoi(s);
    cout<<h<<" "<<w<<endl;*/

    for(int i = 0; i < h; i++){
        for(int j =0;j<w;j++){
            cout<<G[i][j];
        }
        cout<<endl;
    }

    G[0][0]='v';


    for(int i = 0; i < h; i++){
        for(int j =0;j<w;j++){
            if(G[i][j]=='.'){
                cout<<'s';
            }
        }
        
    }
    /*file >> s;

    cout<<s<<endl;
    cout<<s[0]<<endl;*/

    return 0;
}