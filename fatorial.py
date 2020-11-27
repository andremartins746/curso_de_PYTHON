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