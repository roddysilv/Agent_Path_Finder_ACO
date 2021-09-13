# Agent Path Finder - ACO
Trabalho de Inteligência Computacional

## Dependências
* G++ - Para compilar o programa em C++
* Python3 - Para poder plotar as rotas encontradas
* Pip - Para instalar as dependencias do Python
```
sudo apt -y install python3-pip
```
* Numpy
```
pip3 install numpy
```
* Matplotlib
```
pip3 install matplotlib
```
* Pandas
```
pip3 install pandas
```
## Execução
Para executar o código todo, execute o arquivo run.sh localizado na pasta códigos.
Abra o arquivo e coloque os parâmetros desejados na seguinte ordem:
* Número de Formigas
* Número de Iterações
* Peso do Ferormônio
* Peso da Hurística
* Porcentagem de Evaporação do Ferormônio
* Número de Fichas
* Mapa da Instância - Ex.: "../Instâncias/Mapas/M_30x30B2.txt"
* Tour da Instância - Ex.: "../Instâncias/Tour/10 buscas/Tour_M_30x30B2.txt"
Abra um terminal Linux e execute o seguinte comando :
```
sh run.sh
```

Resultados serão salvo na pasta Códigos/Resultados e as imagens na pasta Imagens.
