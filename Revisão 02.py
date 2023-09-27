ano=float(input("Digite sua idade: "))
mes=float(input("Digite quantos meses: "))
dias=float(input("Digite a quantidade de dias: "))
if dias>=30:
    mes=mes+1
    dias=dias-30
if mes >= 12:
    ano=ano+1
    mes= mes-12

diaano=ano*365
diames=mes*30

total=dias+(diames)+(diaano)
print(total)