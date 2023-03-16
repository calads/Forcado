# Para desenvolver o jogo da forca em Python, você pode seguir os seguintes passos:

#Import
# Função para limar a tela a cada execução
# Definir as palavras que podem ser sorteadas para o jogo
# Escolher uma palavra aleatória do conjunto de palavras
# Criar uma lista vazia para representar a palavra a ser adivinhada
# Definir o número máximo de tentativas permitidas
# Inicializar o número de tentativas e as letras usadas
# Enquanto o jogador ainda tiver tentativas restantes e a palavra não tiver sido adivinhada:
	# Mostrar a palavra a ser adivinhada e as letras já usadas
	# Pedir ao jogador para tentar adivinhar uma letra
	# Se a letra já foi usada, informar o jogador e continuar
	# Adicionar a letra às letras usadas
	# Verificar se a letra adivinhada está na palavra secreta
		# Atualizar a palavra adivinhada com a letra adivinhada
		# A letra adivinhada não está na palavra secreta
	# O jogo terminou. Verificar se o jogador ganhou ou perdeu
# Bloco main


#Import
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

	limpa_tela()
	print("\nBem-vindo(a) ao jogo da forca!")
	print("Adivinhe a palavra abaixo:\n")

	# Definir as palavras que podem ser sorteadas para o jogo
	palavras = ["abacaxi", "banana", "laranja", "morango", "uva"]

	# Escolher uma palavra aleatória do conjunto de palavras
	palavra_secreta = random.choice(palavras)

	# Criar uma lista vazia para representar a palavra a ser adivinhada
	palavra_adivinhada = ["_" for letra in palavra_secreta]

	# Definir o número máximo de tentativas permitidas
	max_tentativas = 6

	# Inicializar o número de tentativas e as letras usadas
	tentativas = 0
	letras_usadas = []

	# Enquanto o jogador ainda tiver tentativas restantes e a palavra não tiver sido adivinhada
	while tentativas < max_tentativas and "_" in palavra_adivinhada:
	    # Mostrar a palavra a ser adivinhada e as letras já usadas
	    print(" ".join(palavra_adivinhada))
	    print("Letras usadas: " + " ".join(letras_usadas))

	    # Pedir ao jogador para tentar adivinhar uma letra
	    letra = input("Digite uma letra: ").lower()

	    # Se a letra já foi usada, informar o jogador e continuar
	    if letra in letras_usadas:
	        print("Você já tentou essa letra. Tente outra.")
	        continue

	    # Adicionar a letra às letras usadas
	    letras_usadas.append(letra)

	    # Verificar se a letra adivinhada está na palavra secreta
	    if letra in palavra_secreta:
	        # Atualizar a palavra adivinhada com a letra adivinhada
	        for i in range(len(palavra_secreta)):
	            if letra == palavra_secreta[i]:
	                palavra_adivinhada[i] = letra
	    else:
	        # A letra adivinhada não está na palavra secreta
	        print("Essa letra não está na palavra.")
	        tentativas += 1

	# O jogo terminou. Verificar se o jogador ganhou ou perdeu
	if "_" not in palavra_adivinhada:
	    print("Parabéns, você adivinhou a palavra " + palavra_secreta + "!")
	else:
	    print("Você perdeu. A palavra era " + palavra_secreta + ".")


# Bloco main
if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo programação em Python com a DSA.\n")