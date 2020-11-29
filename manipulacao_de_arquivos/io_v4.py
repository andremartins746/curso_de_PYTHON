#!/usr/local/bin/python2

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('nome: {}, idade: {}'.format(*registro.strip().split(',')))

except IndexError:
    pass

finally:
    print("finally")
    arquivo.close()

if arquivo.closed:
    print("o arquivo foi fechado!!")