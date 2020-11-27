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