
iniciachat = input()
from random import choice
conversa1 = str("Me chamo bbot1, qual é o seu nome? ")
conversa2 = str("qual seu nome?")
conversa3 = str(" Eu sou o bbot, como vc se chama? ")

opcao = [conversa1,conversa2,conversa3]

escolha = choice(opcao)
resposta = input(escolha)

resposta2 = input(format('') + (" muito prazer " + resposta + ", você está bem? "))

if (resposta2.upper() == "SIM"):
    resposta3 = input("que ótimo, fico feliz! posso te fazer uma pergunta? ")
    
    if (resposta3.upper() == "SIM"):
        
        
        resposta4 = input("opa que bom, qual dos dois elementos é mais pesado? metal ou algodão? ")

        if (resposta4 == "nenhum dos dois"):
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
     resposta5 = input("poxa, que pena, posso ajudar? ")

     if (resposta5.upper() == "SIM"):
         resposta6 = input("ok, Me diga. Você esta triste? ")

         if (resposta6.upper() == "SIM"):
             print(" Em momentos ruins assim é bom ficar perto de alguém que te alegre ou ouvir musicas bem animadas!,"
                   "tente fazer isso ok?")
             l = input(" ")
             print(" Eu tenho certeza que vai ficar tudo bem, quando quiser conversar de novo me chama aki !")
             
     else:
         print(" puxa, vc está fazendo jogo duro, espero que as coisas melhorem pra vc "
              "se quiser conversar de novo me chama aki, um abraço !")
         import os
         os.startfile(' ')
