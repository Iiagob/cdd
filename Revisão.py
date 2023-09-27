'''n1= float(input("Digite um número: "))
n2= float(input("Digite um número: "))
n3= float(input("Digite um número: "))
n4= float(input("Digite um número: "))

media= (n1+n2+n3+n4)/4
print(media)'''

soma=0
cont=int(input("Quantos números deseja digitar?"))
for x in range(cont):
    n=float(input(("Digite um número:")))
    soma=soma+n
    if soma>=1000:
        break
media= soma/cont
print(media)
print(soma)

