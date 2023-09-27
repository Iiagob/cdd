n1=int(input("digite um número:"))
'''
for x in range(n1+1):
    for y in range(1,x+1):
        print( y, end=" ")
    print()'''

cont=1
x=""
while cont<=n1:
    x+=str(cont)
    print(x)
    cont+=1
