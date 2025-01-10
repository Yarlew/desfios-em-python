#essa script sorteia um numero e pede para o usuario  acertar, o programa fale se o chute dele esta quente ou frio

from random import randint 
from termcolor import colored

numero_secreto = randint(1, 10)


while True:
     usuario = int (input ('digite uma valor. tente sua sorte...  :  '))

     if usuario < numero_secreto:
          print('numero muito baixo')

     elif usuario > numero_secreto:
          print ('numero muito alto')

     elif usuario == numero_secreto:
          print('certa resposta!!!')
          break






