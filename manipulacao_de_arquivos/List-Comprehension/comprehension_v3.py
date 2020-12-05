# usando generator, ele comsome menos memoria
generator = (i ** 2 for i in range(10) if i % 2 == 0)

#o next serve para extrair o valor do generator, importante o generator nbao e uma tupla
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) aqui vai dar um ERRO apartir do 64
