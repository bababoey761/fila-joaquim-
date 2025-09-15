especiais = ["gestante", "pcd", "outro"]
fila = []

def add():
    while True:
        especial = False
        prioridade = False
        n = input('Qual seu nome: ')
        idade = input("Digite sua idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade inválida, por favor tente novamente")
            continue
        if idade >= 60:
            prioridade = True
            esp = "Acima de 60"
        else:
            esp = "nenhum"
        while True:
            ness = input('Você possui alguma necessidade? (escreva "n" para não ou "s" para sim): ').lower()
            if ness == "n":
                especial = False
                break
            elif ness == "s":
                especial = True
                break
            else:
                print('Resposta inválida, por favor responda apenas com "n" para não ou "s" para sim: ')
                continue
        if especial:
            while True:
                esp = input('Por favor digite qual sua necessidade (gestante, pcd ou outro): ').lower()
                if esp in especiais:
                    prioridade = True
                    break
                else:
                    print("Tipo de necessidade inválido. Tente novamente.")
                    continue
        pessoa = {
            "prioridade": prioridade,
            "ordem": len(fila),
            "nome": n,
            "idade": idade,
            "necessidade": esp
        }
        fila.append(pessoa)
        fila.sort(key=lambda x: (not x["prioridade"], x["ordem"]))
        break


def mostrar():
    if not fila:
        print("Fila vazia. Preencha a fila com pelo menos uma pessoa")
    else:
        print("\nFila de pessoas: \n")
        prio = 0
        n_prio = 0
        for i, pessoa in enumerate(fila, start=1):
            print(f"{i} - {pessoa['nome']} - Idade: {pessoa['idade']} - Necessidade: {pessoa['necessidade']} - Prio: {'Sim' if pessoa['prioridade'] else 'Não'}")
            if pessoa['prioridade']:
                prio += 1
            else:
                n_prio += 1
        print(f"\nTotal prioritários: {prio}")
        print(f"Total não prioritários: {n_prio}")

def atender():
    if not fila:
        print("Fila vazia")
    else:
        pessoa = fila.pop(0)
        print(f"Atendido: {pessoa['nome']} ({pessoa['idade']} anos)  {'prioritário: ' + pessoa['necessidade'] if pessoa['prioridade'] else ''}")

# Como ja havia feito com um menu por costume. apenas removi e coloquei o menu no fila_3.py
