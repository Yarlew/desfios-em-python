import random
import emoji

while True:
   numero_secreto = random.randint(1, 10)

   numero_sugerido=int(input('chute um numero, e tente sua sorte: '))

   if numero_sugerido < numero_secreto:
        print('Numero Baixo ')

   elif numero_sugerido > numero_secreto:
        print('Numero Muito Alto')

   else:
        print('Rapaz... que bixo mizeravi mrm')
        break
        