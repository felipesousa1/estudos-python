import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    with open("palavras.txt", encoding='utf-8', mode="r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    palavra_secreta = random.choice(palavras).lower()
    letras_descobertas = ["_"]*len(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = (input("Qual letra? ")).strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_descobertas[index] = letra
                index += 1
        else:
            erros += 1

        print("".join(letra for letra in letras_descobertas))

        acertou = "_" not in letras_descobertas
        enforcou = erros == 5

    if acertou:
        print("Você ganhou!!")
    else:
        print(f"Você perdeu :(\nA palavra secreta era '{palavra_secreta}'")


if __name__ == "__main__":
    jogar()
