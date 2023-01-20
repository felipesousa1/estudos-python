def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_descobertas=["_"]*len(palavra_secreta)
    
    enforcou=False
    acertou = False
    
    while not enforcou and not acertou:
        
        chute=(input("Qual letra? ")).strip()
        
        index=0
        for letra in palavra_secreta:
            if letra.lower() == chute.lower():
                letras_descobertas[index] = letra
            index += 1

        print("".join(letra for letra in letras_descobertas))
        
        if "_" not in letras_descobertas:
            acertou = True 
    
    print ("Fim do jogo")

if __name__ == "__main__":
    jogar()