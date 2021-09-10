#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>
#include <stdlib.h>
#include <cmath>
#include <algorithm>

using namespace std;

int formigas, iteracoes,h,w;

float alpha, beta, rho, C;

pair<int,int> inicio;

vector<pair<int,int>> objetivos;

vector<vector<char>> G;

vector<vector<float>> T;

vector<vector<int>> Pontos;

vector<vector<pair<int,int>>> caminhos;

void iniciaPontos()
{
    vector<int> aux;
    int k = 0;
    for(int j = 0; j < h; j++)
    {
        for(int i = 0; i < w; i++)
        {
            aux.push_back(k);
            k++;
        }
        Pontos.push_back(aux);
    }

}

void leInstancia(string instancia)
{

    string s;
    ifstream file;
    file.open(instancia);
    file >> s;
    h = stoi(s);
    file >> s;
    w = stoi(s);

    vector<char> aux;

    for(int i = 0; i < h; i++)
    {
        file >> s;
        for(int j =0; j<w; j++)
        {
            aux.push_back(s[j]);
        }
        G.push_back(aux);
        aux.clear();
    }
}

void reiniciaInstancia()
{
    for(int i = 0; i < h; i++)
    {
        for(int j =0; j<w; j++)
        {
            if(G[i][j] == 'v')
            {
                G[i][j] = '.';
            }
        }
    }
}

int calculaDistancia(int x1, int y1, int x2, int y2)
{
    return abs(x1-x2) + abs(y1-y2);
}

float distancia(int x, int y)
{
    vector<int> d;
    for(int i = 0; i<objetivos.size(); i ++)
    {
        d.push_back(calculaDistancia(x,y,objetivos[i].first, objetivos[i].second));
    }
    int min = d[0];
    for(int i = 0; i<d.size(); i ++)
    {
        if(min > d[i])
        {
            min = d[i];
        }
    }
    if (min == 0)
    {
        return 1;
    }
    else
    {
        return 1.0/min;
    }
}

void iniciaFer()
{

    vector<float> aux;

    for(int i =0; i<w; i++)
    {
        aux.push_back(0.1);
    }
    for(int i =0; i<h; i++)
    {
        T.push_back(aux);
    }
}

void diminuiFer()
{
    for(int i =0; i<h; i++)
    {
        for(int j =0; j<w; j++)
        {
            T[i][j] = (1-rho) * T[i][j];
        }
    }
}

void atualizaFerormonio()
{
    for(int i =0; i<caminhos.size(); i++)
    {
        for(int j =0; j<caminhos[i].size()-1; j++)
        {
            int x = caminhos[i][j].first;
            int y = caminhos[i][j].second;
            int x_n = caminhos[i][j+1].first;
            int y_n = caminhos[i][j+1].second;
            T[Pontos[x][y]][Pontos[x_n][y_n]] += C;
        }
    }
}

void grid(int h, int w)
{

    vector<char> aux;

    for(int i =0; i<w+2; i++)
    {
        aux.push_back('.');
    }
    for(int j =0; j<h+2; j++)
    {
        G.push_back(aux);
    }
    for(int i =0; i<w+2; i++)
    {
        for(int j =0; j<h+2; j++)
        {
            if(i == 0 || i==h+1 || j==0 || j==w+1)
            {
                G[i][j]='T';
            }
        }
    }
}

pair<int,int> selecionaNo(pair<int,int> no)
{
    float s = 0;
    if (G[no.first+1][no.second] == '.')
    {
        s += pow(T[Pontos[no.first][no.second]][Pontos[no.first+1][no.second]],alpha) *  pow(distancia(no.first+1,no.second),beta);
    }
    if (G[no.first-1][no.second] == '.')
    {
        s += pow(T[Pontos[no.first][no.second]][Pontos[no.first-1][no.second]],alpha) * pow(distancia(no.first-1,no.second),beta);
    }
    if (G[no.first][no.second+1] == '.')
    {
        s += pow(T[Pontos[no.first][no.second]][Pontos[no.first][no.second+1]],alpha) * pow(distancia(no.first,no.second+1),beta);
    }
    if (G[no.first][no.second-1] == '.')
    {
        s += pow(T[Pontos[no.first][no.second]][Pontos[no.first][no.second-1]],alpha) * pow(distancia(no.first,no.second-1),beta);
    }
    if(s==0)
    {
        pair<int,int> y;
        y.first = -1;
        y.second = -1;
        return y;
    }
    vector<float> p= {0,0,0,0};
    if (G[no.first+1][no.second] == '.')
    {
        p[0] = (pow(T[Pontos[no.first][no.second]][Pontos[no.first+1][no.second]],alpha) *  pow(distancia(no.first+1,no.second),beta)) /s;
    }
    if (G[no.first-1][no.second] == '.')
    {
        p[1] = (pow(T[Pontos[no.first][no.second]][Pontos[no.first-1][no.second]],alpha) * pow(distancia(no.first-1,no.second),beta))/ s;
    }
    if (G[no.first][no.second+1] == '.')
    {
        p[2] = (pow(T[Pontos[no.first][no.second]][Pontos[no.first][no.second+1]],alpha) * pow(distancia(no.first,no.second+1),beta))/ s;
    }
    if (G[no.first][no.second-1] == '.')
    {
        p[3] = (pow(T[Pontos[no.first][no.second]][Pontos[no.first][no.second-1]],alpha) * pow(distancia(no.first,no.second-1),beta)) / s;
    }

    float max=0;
    for(int i =0; i<4; i++)
    {
        if(p[i]>max)
        {
            max=p[i];
        }
    }
    //SELECIONAR A PROB
    vector<int> select;
    for(int i =0; i<4; i++)
    {
        if(p[i] == max)
        {
            select.push_back(i);
        }
    }

    int RandIndex = select[rand() % select.size()];

    pair<int,int> y;

    if(RandIndex == 0)
    {
        y.first = no.first +1;
        y.second = no.second;
        return y;
    }
    if(RandIndex == 1)
    {
        y.first = no.first-1;
        y.second = no.second;
        return y;
    }
    if(RandIndex == 2)
    {
        y.first = no.first;
        y.second = no.second+1;
        return y;
    }
    if(RandIndex == 3)
    {
        y.first = no.first;
        y.second = no.second-1;
        return y;
    }
    else
    {
        y.first = -1;
        y.second = -1;
        return y;
    }
}

vector<pair<int,int>> ACO(string instancia)
{
    leInstancia(instancia);
    iniciaPontos();
    iniciaFer();
    vector<pair<int,int>> best;
    for(int i = 0; i < iteracoes; i++)
    {
        for(int j = 0; j < formigas; j++)
        {
            vector<pair<int,int>> busca = objetivos;
            pair<int,int> no = inicio;
            vector<pair<int,int>> path= {no};
            bool br = false;
            G[no.first][no.second] = 'v';
            while (busca.size() > 0)
            {
                no = selecionaNo(no);
                if( no.first == -1)
                {
                    br = true;
                    break;
                }
                G[no.first][no.second] = 'v';
                if(find(busca.begin(), busca.end(), no) != busca.end())
                {
                    //remove no de busca
                    busca.erase(remove(busca.begin(), busca.end(), no), busca.end());
                }
                path.push_back(no);
            }
            if (br != true)
            {
                if(path.size() < best.size() || best.size() == 0)
                {
                    best = path;
                }
                caminhos.push_back(path);
            }
            reiniciaInstancia();
        }
        diminuiFer();
        atualizaFerormonio();
        caminhos.clear();
    }
    return best;
}

void save(vector<pair<int,int>> c, string instancia)
{
    ofstream file;
    file.open("Resultados.csv");
    file << instancia << ",0,0"<<endl;
    for(int i =0; i< c.size(); i++)
    {
        if(find(objetivos.begin(), objetivos.end(), c[i]) != objetivos.end())
        {
            file << c[i].first << "," << c[i].second << "," << 1 <<endl;
        }
        else
        {
            file << c[i].first << "," << c[i].second << ","  << 0 << endl;
        }
    }
    file.close();
}

int main(int argc, char *argv[])
{
    formigas = atoi(argv[1]);

    iteracoes = atoi(argv[2]);

    alpha = atof(argv[3]);

    beta = atof(argv[4]);

    rho = atof(argv[5]);

    C = atof(argv[6]);

    string instancia = argv[7]; //"../Instâncias/M_20x20.txt";

    inicio.first = 1;
    inicio.second = 1;

    pair<int,int> t;
    t.first = 5;
    t.second = 5;
    objetivos.push_back(t);

    t.first = 10;
    t.second = 18;
    objetivos.push_back(t);

    vector<pair<int,int>> c = ACO(instancia);

    cout<<endl;

    if(c.size()>0){
        cout<<"Execução Terminada!"<<endl<<endl;
        save(c,instancia);
    }
    else{
        cout << "Não foram encontradas rotas!"<<endl<<endl;
    }

    cout<<alpha<<" "<<beta<<" "<<rho<<" "<<C<<" "<<endl;
    
//cout<<distancia(1,1)<<" "<<calculaDistancia(1,1,5,5);

    return 0;
}
