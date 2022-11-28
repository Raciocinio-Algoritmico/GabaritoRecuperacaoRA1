import random
import time
vida_jogador = 200
vida_inimigo = 200

#Contador, se for par é jogada do jogador, se for impar, do inimigo.
contador = 0 
while True:
    if contador % 2 == 0:
        #Vez do jogador
        print("------------| JOGADOR |------------")
        jogada_player = int(input("[1] - Atacar \n" + "[2] - Curar\n"))
        
        if jogada_player == 1:
            dano = random.randint(50, 100)
            
            if dano >= 75:
                print("JOGADOR DEU DANO CRÍTICO DE {}!".format(dano))
            else:
                print("Jogador deu {} de dano.".format(dano))
                
            vida_inimigo -= dano
        else:
            cura = random.randint(30, 50)
            
            print("Jogador curou {} de vida.".format(cura))
            
            vida_jogador += cura
            
        print("------------| STATUS |------------")
        print("Vida Jogador: {}".format(vida_jogador))
        print("Vida Inimigo: {}".format(vida_inimigo))
        print("----------------------------------\n\n")
    else:
        #Vez do inimigo
        print("------------| INIMIGO |------------")
        jogada_inimigo = random.randint(1, 2)
        
        time.sleep(2)
        
        if jogada_inimigo == 1:
            dano = random.randint(30, 50)
            
            if dano >= 75:
                print("INIMIGO DEU DANO CRÍTICO DE {}!".format(dano))
            else:
                print("Inimigo deu {} de dano.".format(dano))
                
            vida_jogador -= dano
        else:
            cura = random.randint(50, 100)
            
            print("Inimigo curou {} de vida.".format(cura))
            
            vida_inimigo += cura
        
        time.sleep(2)
        
        print("------------| STATUS |------------")
        print("Vida Jogador: {}".format(vida_jogador))
        print("Vida Inimigo: {}".format(vida_inimigo))
        print("----------------------------------\n\n")
        
    #Condição de vitoria/derrota
    if vida_inimigo < 0:
        print("VITÓRIA")
        break
    elif vida_jogador < 0:
        print("DERROTA!")
        break
        
    contador += 1
        