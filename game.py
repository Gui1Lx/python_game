from time import sleep
from random import randint
from emoji import emojize
import color

def linha():
    print('=' * 45)



comp = randint(0, 10) #intervalo de Número que o computador pode "pensar"

linha()
print(emojize('  Adivinhe o Número que eu pensei... :wink:  ', use_aliases = True))
linha()

acertou = False
tentativas = 0

while not acertou:
   jogador = int(input(' Qual é  o seu palpite?: '))
   tentativas += 1
   if jogador == comp:
     break
   else:
      if jogador > comp:
         print(' Menos... tente novamente! ') 
      if jogador < comp:
         print(' Mais... tente novamente!')
        
        
linha()
print(' PROCESSANDO... ')
sleep(2)
linha()
print(emojize(' VOCÊ GANHOU DE MIM!!! :white_check_mark: ', use_aliases=True))
print(f' Com {tentativas} tentativas ')