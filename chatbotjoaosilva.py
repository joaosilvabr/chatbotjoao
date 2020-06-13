
nn = input()
from random import choice
n1 = str("Me chamo bbot1, qual é o seu nome? ")
n1a = str("qual seu nome?")
n1b = str(" Eu sou o bbot, como vc se chama? ")

op = [n1,n1a,n1b]

escol = choice(op)
n8 = input(escol)

a = {'carro':'é um veiculo','piada':
     " — Qual o seu nome?"
" — Abu Adidalah Sarafi."
" — Sexo?"
" — Quatro vezes por semana."
" — Não, não! Homem ou mulher?"
" — Homem, mulher… algumas vezes camelo também!",'nome':'meu nome é bbot e o seu ate onde sei é ' + n8 + ' rs!'}
carro = a['carro']
piada = a['piada']     
nome = a['nome']


n2 = input(format('') + (" muito prazer " + n8 + ", você está bem? "))

if (n2.upper() == "SIM"):
    n3A = input("que ótimo, fico feliz! posso te fazer uma pergunta? ")
    
    if (n3A.upper() == "SIM"):
        
        
        n3A1 = input("opa que bom, qual dos dois elementos é mais pesado? metal ou algodão? ")

        if (n3A1 == "nenhum dos dois"):
            print(" correto vc acertou, parabéns " " vc é bem inteligente!")
            input(' ')
            print(" Fiquei muito feliz em te conhecer, espero conversar com vc novamente! um abraço! ")
            
                
        else:
            print(" uhm! vc errou. a resposta certa seria nenhuma das duas,"'\n'
                  "pois um kilo de metal tem o mesmo peso que um kilo de algodão.")
            input(' ')
            input(" talvez da proxima vc acerte kk ")
            print(" quando quiser bater um papo me chama aki bye bye!")
            
                
    else:
        print(" Poxa, tudo bem, agente conversa um outra hora então.Um abraço!")
        
else:
     n3B = input("poxa, que pena, posso ajudar? ")

     if (n3B.upper() == "SIM"):
         n3B1 = input("ok, Me diga. Você esta triste? ")

         if (n3B1.upper() == "SIM"):
             print(" Em momentos ruins assim é bom ficar perto de alguém que te alegre ou ouvir musicas bem animadas!,"
                   "tente fazer isso ok?")
             l = input(" ")
             print(" Eu tenho certeza que vai ficar tudo bem, quando quiser conversar de novo me chama aki !")
             
     else:
         print(" puxa, vc está fazendo jogo duro, espero que as coisas melhorem pra vc "
              "se quiser conversar de novo me chama aki, um abraço !")
         import os
         os.startfile(' ')