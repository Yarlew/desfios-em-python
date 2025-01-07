#parte da soma
valor01 = int (input('Digite um valor: '))
valor02 = int (input ('digite outro valor: '))

soma = valor01 + valor02

print (f'A soma entre {valor01} e {valor02} é igual a {soma}')

#parte da do if, else e elif

pergunta = input ('Correto ? responda com sim/não ')

if pergunta == 'sim':
    print('que bom!!')

elif pergunta == "não":
    print('Que pena, vamos tentar novamente.')

else:
    print('responda com sim ou não')