import time

especiais = ["gestante", "pcd", "outro"]
fila = []
atendidos = 0

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
        for i, pessoa in enumerate(fila, start=1):
            print(f"{i} - {pessoa['nome']} - Idade: {pessoa['idade']} - Necessidade: {pessoa['necessidade']} - Prio: {'Sim' if pessoa['prioridade'] else 'Não'}")

    if atendidos > 0:
        total = atendidos + len(fila)
        porcentagem_atendidos = (atendidos / total) * 100
    else:
        porcentagem_atendidos = 0
    priori = sum(1 for pessoa in fila if pessoa["prioridade"])
    porcentagem = (priori / len(fila)) * 100 if fila else 0

    print(f"\n    {porcentagem:.1f}% são prioritários na fila atual")
    print(f"    {porcentagem_atendidos:.1f}% já foram atendidos")
    time.sleep(3)

def m_fila():
    # debug da fila
    print(fila)

def atender():
    global atendidos
    if not fila:
        print("Fila vazia")
    else:
        pessoa = fila.pop(0)
        atendidos += 1
        print(f"Atendido: {pessoa['nome']} ({pessoa['idade']} anos)  {'prioritário: ' + pessoa['necessidade'] if pessoa['prioridade'] else ''}")

def menu():
    while True:
        print(f"\n -----------// MENU //-----------\n")
        print("1 - Adicionar pessoa a fila")
        print("2 - mostrar fila")
        print("3 - Atender proximo da fila")
        print("4 - Sair")

        op = (input("\nEscolha uma opção: "))
        opções = {'1': add, '2': mostrar, '4': exit, '3': atender, '0': m_fila}
        if op in opções:
            opções[op]()
        else:
            print("Opção inválida. Tente novamente.")
            continue

menu()
