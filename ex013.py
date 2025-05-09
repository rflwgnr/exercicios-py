salario = float(input('Digite o seu salario atual: '))
ajuste = 15

novoSalario = salario * (1 + (ajuste / 100))
print('O salario de R${:.2f} será ajustado para R${:.2f}'.format(salario, novoSalario))