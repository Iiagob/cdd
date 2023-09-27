n=int(input("digite um número:"))
'''
for x in range(n+1):
    print(str(x)*x, end=" ")
'''

cont=0
while cont<=n:
    print(str(cont)*cont)
    cont+=1
