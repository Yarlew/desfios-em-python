nu1=int(input('valor 1 '))
nu2=int(input('valor 2 '))
res=nu1 + nu2
print(f'o soma entre {nu1} e {nu2} e igual a {res} ')


corr=input('correto? ')

if corr == 'sim' :
    print('que bom.')
elif corr == 'não' :
    print('que pena, vamos tentar novamente.')

