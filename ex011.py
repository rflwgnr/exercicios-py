altura = float(input('Insira a altura da parede em metros: '))
largura = float(input('Insira a largura da parede em metros: '))
area = altura * largura
ppl = 2 #pintura por litro

print('Você precisa de {:.1f} litros para pintar {}m²'.format(area/ppl, area))