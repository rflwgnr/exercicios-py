preco = float(input('Digite o preço do produto: '))
promocao = 33

precoPromocional = preco * (1 - (promocao / 100))

print('O produto de R${:.2f} está saindo por {:.2f}'.format(preco, precoPromocional))