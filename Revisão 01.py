reps=0
n=int(input("Digite um número:"))
ante=n-1
dps=n+1
while reps!="1" or reps!="2" or reps!="3":
    resp=input("Digite 1 para mostrar o antecessor\n""Digite 2 para mostrar o sucessor\n""Digite 3 para sair do programa: ")
    if resp=="1":
        print(ante)
    elif resp=="2":
        print(dps)
    elif resp=="3":
        break
    else:
        print("Opção invalida")
