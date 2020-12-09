# usando generator, ele comsome menos memoria
generator = (i ** 2 for i in range(10) if i % 2 == 0)

#aqui diferente das vercoes anteriores ele faz o sistema de stremer.
#ele vai carregando sobre a nessecidade!
for numero in generator:
    print(numero)