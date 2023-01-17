def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou=False
    acertou = False
    
    while not enforcou and not acertou:
        
        chute=(input("Qual letra? ")).strip()
        
        index=0
        for letra in palavra_secreta:
            if letra.lower() == chute.lower():
                print(f"Você encontrou {chute} na posição {index}")
            index += 1

        print("Jogando...")

    print ("Fim do jogo")

if __name__ == "__main__":
    jogar()