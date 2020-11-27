"""
print("fatorial")
def fatorial():
    fat = 1
    n= int(input("digite o fatorial:"))
    i = 2
    while i <=n:
        fat = fat * i
        i+=1

    print("o valor do fatorial eh: ", fat)

fatorial()

print("\n**************\n")

print("contagem de 0 a 10")
def contagem():
    x = 0
    while x <= 10:
        print(x)
        x +=1

contagem()

print("contagem regresiva...")

def contagem_regreciva():
    x = 10
    while x >=0:
        print(x)
        x -=1

contagem_regreciva()
"""


def juncao():
    impar = []
    par=[]
    j=[]

    print("numeros pares...")

    def numeros_pares():
        
        x = 0
        while x <=10:
            if(x % 2 == 0):
                par.append(x)
            x +=1   

        print(par) 

    numeros_pares()

    print("\n\n")

    print("numeros impares")

    def numeros_impares():
        
        x=0
        while x <= 10:
            if(x  % 2 == 1):
                impar.append(x)
            x+=1
        print(impar)

    numeros_impares()

    
    y=0
    while y<=10:
        j.append(par[y])
        j.append(impar[y+1])
        y+=1

    print(j)

juncao()