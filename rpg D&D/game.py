print("""

""")

def create_player():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    classe = input("Digite sua classe: ")
    raça = input("Digite sua raça: ")
    
    return nome, idade, classe, raça

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

def atacar_com_arma(dano_arma):
    print(f"Você atacou com sua arma e causou {dano_arma} pontos de dano.")

def atacar_com_mãos():
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
    atacar_com_arma(dano_arma)
elif escolha_ataque == "mãos":
    atacar_com_mãos()
else:
    print("Opção inválida. Você perdeu a oportunidade de atacar desta vez.")
