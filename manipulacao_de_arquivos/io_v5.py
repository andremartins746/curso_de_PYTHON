#!/usr/local/bin/python2
# AQUI ELE JA ABRE E FECHA UM ARQUIVO
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('nome: {}, idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print("o arquivo foi fechado!!")