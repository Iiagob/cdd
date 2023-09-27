resp="s"
while resp=="s":
    n1= int(input("Receba uma nota: "))
    n2= int(input("Receba outra nota: "))

    media= (n1+n2)/ 2

    if media>=7:
        print(f"A média do aluno foi de {media}, ele foi APROVADO!")
    elif media>=4:
        print(f"A média do aluno foi de {media}, ele está em RECUPERAÇÃO!")
    else:
        print(f"A média do aluno foi de {media}, ele está REPROVADO!")
    resp=input("Deseja fazer um novo calculo?")

