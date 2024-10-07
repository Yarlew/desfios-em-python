"""nota= float(input('qual foi sua nota?'))

if nota >= 6:
      print('aprovado')
elif nota >= 4:
      print('recuperação')
else:
      print('reprovado/a')"""


login=input('digite seu login: ')
senha=input('digite sua senha: ')

if login == 'café' and senha == 'biru':
   print(f'bem vindo {login :=^20} !!!')
else:
   print('senha ou login errado, tente novamente!!! ')