#!/usr/local/bin/python2

arquivo = open('pessoas.csv')

for registro in arquivo:
    print('nome: {}, idade: {}'.format(*registro.split(',')))

arquivo.close()

print("ola mundo")