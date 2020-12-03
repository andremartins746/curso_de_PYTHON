import csv
from urllib import request

def red(url):
    with request.urlopen(url)as entrada:print('baixando o csv...')
    dados = entrada.read().decode('latin1')
    print('dowload bem sucedido!')
    for cidade in csv.reader(entrada.splitlines()):
        print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'https://files.coder.com.br/curso-python/desafio-ibge.csv')