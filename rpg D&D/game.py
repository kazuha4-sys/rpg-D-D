# Copyritht (c) 2024 Kauan e Enzo:
# Este é um projeto de programação criado por Kauan e Enzo em 2024.
# Todos os direitos autorais sobre este código são reservados a Kauan e Enzo.
# Qualquer reprodução ou distribuição não autorizada deste código, no todo ou em parte, é estritamente proibida.
# O uso deste código para fins comerciais ou sem permissão dos autores é proibido.
# Os autores não se responsabilizam por quaisquer danos resultantes do uso deste código.

# AVISO LEGAL: Este código é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita,
# incluindo, mas não se limitando a garantias de comercialização, adequação a uma finalidade específica e não violação.
# Em nenhuma circunstância os autores serão responsáveis por quaisquer reclamações, danos ou outras responsabilidades,
# quer em ação de contrato, delito ou de outra forma, decorrentes de, fora ou em conexão com o software ou o uso ou
# outras negociações nos programas.

# Se você pretende fazer qualquer alteração neste código, entre em contato com os programadores pelos seguintes meios:
# KAUAN
# - Número de telefone: +XX XXX XXX XXXX
# - E-mail: exemplo@gmail.com
# - Github: https://github.com/kazuha4-sys

# ENZO
# - Número de telefone: +XX XXX XXX XXXX
# - E-mail: exemplo@gmail.com
# - Github:

# Ao usar este código, você concorda com os termos e condições acima.

# Jogo D&D em terminal e site para a escola em Python, (trabalho de programação)

# Importa as bibliotecas necessárias
from random import choice as r, randint as rint
import os 
import time as t

# Logo e Copy
print("""

_________                     .__  __  .__                _____    ____  __.                                ___________                    
\_   ___ \  ____ _____________|___/  |_|  |__   ____     / ___ \  |    |/ ______   __ _______    ____       \_   _____/ ____ ____________  
/    \  \/ /  _ \\____ \_  __ |  \   __|  |  \ / ___\   / / ._\ \ |      < \__  \ |  |  \__  \  /    \       |    __)_ /    \\___   /  _ \ 
\     \___(  <_> |  |_> |  | \|  ||  | |   Y  / /_/  > <  \_____/ |    |  \ / __ \|  |  // __ \|   |  \      |        |   |  \/    (  <_> )
 \______  /\____/|   __/|__|  |__||__| |___|  \___  /   \_____\   |____|__ (____  |____/(____  |___|  / /\  /_______  |___|  /_____ \____/ 
        \/       |__|                       \/_____/                      \/    \/           \/     \/  )/          \/     \/      \/      

""")

print ("""

 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  ________    | || |    ___       | || |  ________    | |
| | |_   ___ `.  | || |  .' _ '.     | || | |_   ___ `.  | |
| |   | |   `. \ | || |  | (_) '___  | || |   | |   `. \ | |
| |   | |    | | | || |  .`___'/ _/  | || |   | |    | | | |
| |  _| |___.' / | || | | (___)  \_  | || |  _| |___.' / | |
| | |________.'  | || | `._____.\__| | || | |________.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'

""")

# Função para contar a história e criar o personagem
def historia():
    print("Mais 5 minutos por favor")
    t.sleep(300)
    print("Bora filho levanta!!!")
    t.sleep(1)
    print("TA bom, já levantei mãe!")
    t.sleep(50)
    print("descendo as escadas")
    t.sleep(2)
    print("olá, tio Bem")
    t.sleep(2)
    nome = input("Hmm, olá:  ") 
    class_personagem = {
            "guerreiro",
            "mago",
            "arqueiro",
            "Elfo"
            "Demonio"
        }
    t.sleep(1)
    print("pegue suas coisas " + nome + classe)
    t.sleep(1)
    print("Escolha sua arma:")

    def choose_weapon():
        # Armas e danos da arma 
        armas_disponiveis = {
            "espada": 10,
            "machado": 15,
            "arco": 20,
            "gozo": 250
        }

        # Exibir as opções de arma
        for arma, dano in armas_disponiveis.items():
            print(f"{arma.capitalize()} - Dano: {dano}")

        escolha = input("Digite o nome da arma que deseja: ").lower()

        if escolha in armas_disponiveis:
            return escolha, armas_disponiveis[escolha]
        else:
            print("Arma inválida. Escolha novamente.")
            return choose_weapon()

    return choose_weapon()


print(historia())    


# Função para criar monstros
def create_boss():
    nome = ['soldado', 'demonio', 'elfo', 'Goblin']
    level = rint(1, 10)

    return r(nome), level

# Funções para ataques
def attack_with_weapon(dano_arma):
    print(f"Você atacou com sua arma e causou {dano_arma} pontos de dano.")

def attack_with_hands():
    print("Você atacou com as mãos e causou 1 ponto de dano.")

# Criar personagem
nome, idade, classe, raça = historia()

# Escolher arma
arma_escolhida, dano_arma = historia()

# Exibir informações do personagem
print("\nJogador criado:")
print("Nome:", nome)
print("Idade:", idade)
print("Classe:", classe)
print("Raça:", raça)
print("Arma Escolhida:", arma_escolhida.capitalize())
print("Dano da Arma:", dano_arma)

# Escolher modo de ataque
escolha_ataque = input("\nComo você deseja atacar? (arma/mãos): ").lower()

# Executar ataque
if escolha_ataque == "arma":
    attack_with_weapon(dano_arma)
elif escolha_ataque == "mãos":
    attack_with_hands()
else:
    print("Opção inválida. Você perdeu a oportunidade de atacar desta vez.")

# Criar monstro
monster_name, monster_level = create_boss()

# Exibir informações do monstro
print("\nBoss criado:")
print("Nome do Boss:", monster_name)
print("Level do Boss:", monster_level)
