import random

lista_palavras = ['python', 'programação', 'computador', 'software', 'notebook', 'software', 'openai']

palavra = random.choice(lista_palavras)
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_escondida = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_escondida += letra
        else:
            palavra_escondida += '_'

    print('Palavra:', palavra_escondida)
    print('Letras erradas:', letras_erradas)
    print('Tentativas restantes:', tentativas)

    if palavra_escondida == palavra:
        print('Você acertou!')
        break
    elif tentativas == 0:
        print('Você perdeu Burro! A palavra era:', palavra)
        break
        
    letra_usuario = input('Digite uma letra: ').lower()

    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra incorreta!')
        letras_erradas.append(letra_usuario)
        tentativas -= 1

#