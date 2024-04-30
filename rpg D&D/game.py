#-REGRAS: Caso queria alterar algo, pode so me avisa oq é e qual alteraçao vai fazer, é isso bj
#copyright @ Kauan, Enzo 2024 
#importa as bibliotecas 
from random import choice as r, randint as rint
import os 
import time as t

#sons = os.listdir("audio.mp3") esta em desenvolvimento, porem se quiser baixar o audio é: https://www.youtube.com/watch?v=CKA1zCwcYBE baixa e manda

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



def historia():
    #print(sons['relogio.mp3'()])
    print("Mais 5 minutos por favor")
    t.sleep(300)
    #print(sons['relogio.mp3'()])
    print("Bora filho levanta!!!")
    t.sleep(1)
    print("TA bom, ja levantei mae!")
    t.sleep(50)
    print("desdendo as escadas")
    t.sleep(2)
    print("ola, tio Bem")
    t.sleep(2)
    nome = input("Hmm, Ha ola:  ")    
    t.sleep(1)
    print("pegue suas coisas " + nome)
    t.sleep(1)
    def choose_weapon():
        armas_disponiveis = {
            "espada": 10,
            "machado": 15,
            "arco": 20,
            "gozo": 250
        }

        print("Escolha sua arma:")
        for arma, dano in armas_disponiveis.items():
            print(f"{arma.capitalize()} - Dano: {dano}")

        escolha = input("Digite o nome da arma que deseja: ").lower()

        if escolha in armas_disponiveis:
            return escolha, armas_disponiveis[escolha]
        else:
            print("Arma inválida. Escolha novamente.")
            return choose_weapon()


print(historia())    



def create_player():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    classe = input("Digite sua classe: ")
    raça = input("Digite sua raça: ")

    return nome, idade, classe, raça

def create_boss():
    nome = ['soldado', 'demonio', 'elfo', 'Goblin']
    level = rint(1, 10)

    return r(nome), level

def choose_weapon():
    armas_disponiveis = {
        "espada": 10,
        "machado": 15,
        "arco": 20,
        "gozo": 250
    }

    print("Escolha sua arma:")
    for arma, dano in armas_disponiveis.items():
        print(f"{arma.capitalize()} - Dano: {dano}")

    escolha = input("Digite o nome da arma que deseja: ").lower()

    if escolha in armas_disponiveis:
        return escolha, armas_disponiveis[escolha]
    else:
        print("Arma inválida. Escolha novamente.")
        return choose_weapon()

def attack_with_weapon(dano_arma):
    print(f"Você atacou com sua arma e causou {dano_arma} pontos de dano.")

def attack_with_hands():
    print("Você atacou com as mãos e causou 1 ponto de dano.")

nome, idade, classe, raça = create_player()
arma_escolhida, dano_arma = choose_weapon()

print("\nJogador criado:")
print("Nome:", nome)
print("Idade:", idade)
print("Classe:", classe)
print("Raça:", raça)
print("Arma Escolhida:", arma_escolhida.capitalize())
print("Dano da Arma:", dano_arma)

escolha_ataque = input("\nComo você deseja atacar? (arma/mãos): ").lower()

if escolha_ataque == "arma":
    attack_with_weapon(dano_arma)
elif escolha_ataque == "mãos":
    attack_with_hands()
else:
    print("Opção inválida. Você perdeu a oportunidade de atacar desta vez.")

monster_name, monster_level = create_boss()

print("\nBoss criado:")
print("Nome do Boss:", monster_name)
print("Level do Boss:", monster_level)

