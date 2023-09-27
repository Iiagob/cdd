resp="s"
while resp=="s" or resp=="S":
    b=float(input("Qual a base do triângulo? "))
    while b==0:
        b= float(input("Número da base invalido!Qual a base do triângulo? ")

    a=float(input("Qual a altura do triângulo? "))
    while a==0:
        a= float(input("Número da base invalido!Qual a altura do triângulo? "))

    area= (b*a)/2
    print(f"A área do triângulo é {area}")
    resp=input("Deseja refazer o calculo (s/n)?")



'''a=float(input("Qual a altura do triângulo? "))
b=float(input("Qual a base do triângulo? "))
while b==0 or a==0:
    print("Número invalido! Digite novamente!")
    b= float(input("Qual a base do triângulo? "))
    a= float(input("Qual a altura do triângulo? "))
area= (b*a)/2
print(f"A área do triângulo é {area}")'''
