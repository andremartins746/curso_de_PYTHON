#!/usr/local/bin/python2
arquivo = open('desafio-ibge.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print("nono: {}, quarto: {}".format(.split(',')))