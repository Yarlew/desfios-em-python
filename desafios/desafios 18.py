nu1=float(input('digite um valor: '))
sinal=input('digite o sinal da conta: ')
nu2=float(input('digite outro valor: '))

if sinal == '+':
    print(f'resultado dessa adiçao {nu1 + nu2}')

elif sinal == 'x':
    print(f'o resultado dessa subitração é {nu1 * nu2}')

elif sinal == '/':
    print(f'o resultado da dessa divisão é {nu1 / nu2}')

elif sinal == '-':
    print(f' o resultado dessa subtração é {nu1 - nu2}')

else:
    print(f'{sinal} esse sinal não é valido, porfavor digite outro sinal entre (/), (x), (-), (+).')



#+*-/



