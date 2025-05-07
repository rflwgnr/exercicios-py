alturaMetros = float(input('Digite sua altura em metros: '))
centimetros = alturaMetros*100
milimetros = centimetros*10
print('Você tem {:.0f}cm de altura!\nVocê tem {:.0f}mm de altura!'.format(centimetros, milimetros))