#!/usr/local/bin/python2
# AQUI ELE JA ABRE E FECHA UM ARQUIVO
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('nome: {}, idade: {}'.format(*pessoa))

if arquivo.closed:
    print("o arquivo foi fechado!!")

if saida.closed:
    print('arquivo de saida ja foi fechado!!')