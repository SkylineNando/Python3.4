def player():
    jogada = input("Você escolhe  1 para X ou 2 para O)? ")
    def play():
        a = 0;     
        a1 = "a1"
        a2 = "a2"
        a3 = "a3"
        b1 = "b4"
        b2 = "b5"
        b3 = "c6"        
        c1 = "c7"
        c2 = "c8"
        c3 = "c9"

        computador = "O"
                
        
        while a < 9:
            
            a = a + 1;
            
            velha = input("Posição: ") 
            jogador = "";

            if jogada == "1":
                jogador = "X"
            elif jogada == "2":
                jogador = "O"
                
            if velha == "a1":
                if jogador == a1:
                    a = a - 1;
                elif computador == a1:
                    a = a - 1;                    
                else:        
                    a1 = jogador;
            
            elif velha == "a2":
                if jogador == a2:
                    a = a - 1;
                elif computador == a2:
                    a = a - 1;   
                else:        
                    a2 = jogador;
            
            elif velha == "a3":
                if jogador == a3:
                    a = a - 1;
                elif computador == a3:
                    a = a - 1;   
                else:        
                    a3 = jogador;
                
            if velha == "b1":
                if jogador == b1:
                    a = a - 1;
                elif computador == b1:
                    a = a - 1;   
                else:        
                    b1 = jogador;
            
            elif velha == "b2":
                if jogador == b2:
                    a = a - 1;
                elif computador == b2:
                    a = a - 1; 
                else:        
                    b2 = jogador;
            
            elif velha == "b3":
                if jogador == b3:
                    a = a - 1;
                elif computador == b3:
                    a = a - 1; 
                else:        
                    b3 = jogador;    

            
            if velha == "c1":
                if jogador == c1:
                    a = a - 1;
                elif computador == c1:
                    a = a - 1; 
                else:        
                    c1 = jogador;
            
            elif velha == "c2":
                if jogador == c2:
                    a = a - 1;
                elif computador == c2:
                    a = a - 1; 
                else:        
                    c2 = jogador;
            
            elif velha == "c3":
                if jogador == c3:
                    a = a - 1;
                elif computador == c3:
                    a = a - 1; 
                else:        
                    c3 = jogador;

            if a1 == jogador:
                if a2 == jogador:
                    a3 = computador
                if a3 == jogador:
                    a2 = computador;
                if b1 == jogador:
                    c1 = computador
                if c1 == jogador:
                    b1 = computador;
                if b2 == jogador:
                    c3 = computador
                if c3 == jogador:
                    b2 = computador;

            
            if b1 == jogador:
                if a1 == jogador:
                    c1 = computador
                if c1 == jogador:
                    a1 = computador;
                if b2 == jogador:
                    b3 = computador
                if b3 == jogador:
                    b2 = computador;
                

            if c1 == jogador:
                if a1 == jogador:
                    b1 = computador
                if b1 == jogador:
                    a1 = computador;
                if b2 == jogador:
                    a3 = computador
                if a3 == jogador:
                    b2 = computador;
                if c3 == jogador:
                    c2 = computador
                if c2 == jogador:
                    c3 = computador;
                    

            if a2 == jogador:
                if a1 == jogador:
                    a3 = computador
                if a3 == jogador:
                    a1 = computador;
                if b2 == jogador:
                    c2 = computador
                if c2 == jogador:
                    b2 = computador;
                    
            if a1 == a2 == a3:            
                print("Ganhou!! jogador " + jogador )
                a = 9;
            elif b1 == b2 == b3:
                print("Ganhou!! jogador " + jogador )                
                a = 9;
            elif c1 == c2 == c3:
                print("Ganhou!! jogador " + jogador )                
                a = 9;
                
            elif a1 == b2 == c3:
                print("Ganhou!! jogador " + jogador )
                a = 9;
            elif a3 == b2 == c1:
                print("Ganhou!! jogador " + jogador )
                a = 9;
                
            elif a1 == b1 == c1:
                print("Ganhou!! jogador " + jogador )
                a = 9;
            elif a2 == b2 == c2:
                print("Ganhou!! jogador " + jogador )         
                a = 9;
            elif a3 == b3 == c3:
                print("Ganhou!! jogador " + jogador )
                a = 9;
            else:
                print("Pernde")

            print(a1 + " - " + b1 + " - " + c1);        
            print(a2 + " - " + b2 + " - " + c2);
            print(a3 + " - " + b3 + " - " + c3);
              
        if a == 9:
            nova = input("Jogar novamente? Sim ou Não ")
            if nova == "Sim":
                return play()
            else:
                print("Obrigado por jogar...")
            
        
    def playerOne():
        print("Você é X")
        return play()
        playerOne()
    def playerTwo():
        print("Você é O")
        return play()
        playerTwo()
        
    if jogada == "1":
        return playerOne()
    elif jogada == "2":
        return playerTwo()
    else:
        return player()
        play()
player()

