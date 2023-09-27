resp="s"
while resp=="s":
    n=int(input("Digite um número: "))
    while n==0:
        n= int(input("Número inválido! Digite outro número: "))
    else:
        if n>0:
            print("Número positivo")
        else:
            print("Número negativo")

    resp= input("Quer tentar novamente?")
