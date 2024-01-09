# Olá, seja bem-vindo(a) ao meu Projeto DIO.
# Aqui terão informações a mais do que pedidas no projeto para adicionar um toque de criatividade.

import time

# Informações do criador do script.
print("Script feito por Luis!")
time.sleep(1)



def script():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    # Apresentações para o usuário.
    print("Olá bravo(a) guerreiro(a)! Seja bem-vindo(a) ao nosso QG dos heróis de Farland City!")

    # Variável para armazenar o nome do nosso herói.
    nomeHeroi = input("\nPor favor! Peço que se apresente falando seu NOME:\n>>>\t")

    # Variável para armazenar o XP do nosso herói.
    xpHeroi = int(input("Agora, fale a quantidade de XP que você possui para colocarmos no seu relatório:\n>>>\t"))

    # Estrutura de decisão para ver qual nível o Herói está.
    nivelHeroi = None
    if xpHeroi < 1000:
        nivelHeroi = "Ferro"
    elif xpHeroi >= 1001 and xpHeroi <= 2000:
        nivelHeroi = "Bronze"
    elif xpHeroi >= 2001 and xpHeroi <= 5000:
        nivelHeroi = "Prata"
    elif xpHeroi >= 5001 and xpHeroi <= 7000:
        nivelHeroi = "Ouro"
    elif xpHeroi >= 7001 and xpHeroi <= 8000:
        nivelHeroi = "Platina"
    elif xpHeroi >= 8001 and xpHeroi <= 9000:
        nivelHeroi = "Ascendente"
    elif xpHeroi >= 9001 and xpHeroi <= 10000:
        nivelHeroi = "Imortal"
    elif xpHeroi >= 10001:
        nivelHeroi = "Radiante"
        
    # Um adicional que eu fiz para o script, que dá uma nota pro herói baseado no nível dele.
    notaHQ = None
    if xpHeroi < 1000:
        notaQG = "1/10"
    elif xpHeroi >= 1001 and xpHeroi <= 2000:
        notaQG = "2/10"
    elif xpHeroi >= 2001 and xpHeroi <= 5000:
        notaQG = "4/10"
    elif xpHeroi >= 5001 and xpHeroi <= 7000:
        notaQG = "6/10"
    elif xpHeroi >= 7001 and xpHeroi <= 8000:
        notaQG = "7/10"
    elif xpHeroi >= 8001 and xpHeroi <= 9000:
        notaQG = "8/10"
    elif xpHeroi >= 9001 and xpHeroi <= 10000:
        notaQG = "9/10"
    elif xpHeroi >= 10001:
        notaQG = "10/10"

    print("Calculando relatório de Herói...")
    time.sleep(0.5)
    print("25%")
    time.sleep(0.5)
    print("50%")
    time.sleep(0.5)
    print("75%")
    time.sleep(0.5)
    print("99%")
    time.sleep(1)
    print("100%")
    time.sleep(0.5)



    # Saída dos dados
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-------------------- RELATÓRIO DE HERÓI --------------------"
        f"\nNome: {nomeHeroi}"
        f"\nNível do Herói: {nivelHeroi} ( XP: {xpHeroi} )"
        f"\nNota QG para missões especifícas de nível: {notaQG}"
        "\nUse esse relatório com suas INFORMAÇÕES para conseguir trabalhos de acordo com seu nível."
        "\n-------------------- RELATÓRIO DE HERÓI --------------------"
    )
    
    # Pergunta se o usuário quer repetir o relatório
    repeticao = input(f"{nomeHeroi}, você desejaria fazer outro relatório de herói? (S/N):\n>>>\t")
    if repeticao == "S" or repeticao == "s":
        print("Reiniciando Script...\n\n")
        time.sleep(1)
        script()
    elif repeticao == "N" or repeticao == "n":
        print("Até a próxima.")
        exit()
    else:
        print("Comando não interpretado, fechando script.")
        exit()
script()
