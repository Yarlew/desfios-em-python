#essa script sorteia um numero e pede para o usuario  acertar, o programa fale se o chute dele esta quente ou frio

from random import randint
from termcolor import colored

numero_secreto= randint(1,50)

while True:

   numero_sugerido=int(input('chute um numero, e tente sua sorte: '))

   if numero_sugerido < numero_secreto:
        print(colored('Numero Baixo ', 'blue'))

   elif numero_sugerido > numero_secreto:
        print(colored('Numero Muito Alto','red'))

   elif numero_sugerido == numero_secreto:
        print(colored('Rapaz... que bixo mizeravi mrm', 'green'))
        break
        