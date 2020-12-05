# exprecao for item in list if condicional
# o comprehension e uma forma mais rapida de se criar uma lista em python 
# nele vc pode colocas toda a esprecao dentro da lista que ele ja te retorna
#  o resultado da operacao
dobros =[i * 2 for i in range(10)]
print(dobros)

# versao "normal"

dobros1 = []
for i in range(10):
    dobros1.append(i*2)

print(dobros1)