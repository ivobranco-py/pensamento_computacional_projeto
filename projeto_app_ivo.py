import random

# ================== DADOS ==================

clientes = {}

combos = {
    '1': ('Combo Classico Burger + Batata', 28.90),
    '2': ('Combo Bacon Burger + Batata', 32.90),
    '3': ('Combo Chicken Crispy + Batata', 33.90),
    '4': ('Combo Cheeseburger Duplo + Batata', 34.90)
}

lanches = {
    '5': ('Hamburguer Classico', 17.90),
    '6': ('Bacon Burger', 21.90),
    '7': ('Chicken Crispy Burger', 20.90),
    '8': ('Veggie Burger', 19.90),
    '9': ('Cheeseburger Duplo', 23.90)
}

acompanhamentos = {
    '1': ('Nuggets', 9),
    '2': ('Batata extra', 7),
    '3': ('Onion Rings', 8),
    '4': ('Molho Barbecue', 4),
    '5': ('Molho Alho', 4),
    '6': ('Molho Especial', 5)
}

sucos = {
    '1': 'Laranja',
    '2': 'Morango',
    '3': 'Maracuja',
    '4': 'Abacaxi'
}

refrigerantes = {
    '1': 'Coca Cola',
    '2': 'Guarana',
    '3': 'Fanta',
    '4': 'Sprite'
}

vagas = {
    '1': ('Cozinheiro', 25, 5),
    '2': ('Atendente', 17, 1),
    '3': ('Chapeiro', 21, 2),
    '4': ('Entregador', 18, 0),
    '5': ('Gerente', 30, 5),
    '6': ('Auxiliar de Cozinha', 18, 0),
    '7': ('Caixa', 18, 1)
}

# ================== FUNÇÕES ==================

def sugestao_chef():
    item = random.choice(list(lanches.values()))

    print('\n⭐ Sugestão do chef')
    print(item[0], 'R$', item[1])

    resp = input('Deseja adicionar ao pedido? (s/n): ').lower()

    if resp == 's':
        return [(item[0], item[1], 1, 'sugestao')]

    return []

def escolher_lanches():
    carrinho = []
    total_parcial = 0

    while True:
        print('\nCARDÁPIO\n')

        for c in combos:
            print(c, '-', combos[c][0], 'R$', combos[c][1])

        for l in lanches:
            print(l, '-', lanches[l][0], 'R$', lanches[l][1])

        escolha = input('\nEscolha o número do item: ')

        if escolha in combos:
            item = combos[escolha]
        elif escolha in lanches:
            item = lanches[escolha]
        else:
            print('Opção inválida.')
            continue

        try:
            qtd = int(input('Quantidade: '))
        except:
            print('Digite apenas números.')
            continue

        carrinho.append((item[0], item[1], qtd, escolha))

        subtotal = item[1] * qtd
        total_parcial += subtotal

        print('Total parcial: R$', format(total_parcial, '.2f'))

        if input('Mais itens? (s/n): ') != 's':
            break

    return carrinho

def escolher_acompanhamentos():
    lista = []

    if input('\nDeseja acompanhamentos? (s/n): ') == 's':
        for a in acompanhamentos:
            print(a, '-', acompanhamentos[a][0], 'R$', acompanhamentos[a][1])

        while True:
            ac = input('Escolha (0 para sair): ')
            if ac == '0':
                break
            if ac in acompanhamentos:
                lista.append(acompanhamentos[ac])

    return lista

def escolher_bebida(combo=False):
    escolha = input('\n1 Suco\n2 Refrigerante\nEscolha: ')

    if escolha == '1':
        for s in sucos:
            print(s, '-', sucos[s])
        sabor = input('Escolha: ')
        if sabor in sucos:
            return (sucos[sabor], 0 if combo else 9)

    elif escolha == '2':
        for r in refrigerantes:
            print(r, '-', refrigerantes[r])
        refri = input('Escolha: ')
        if refri in refrigerantes:
            return (refrigerantes[refri], 0 if combo else 7)

    return ('Sem bebida', 0)

def escolher_pagamento():
    escolha = input('\n1 Dinheiro\n2 Cartão\n3 Pix\nEscolha: ')

    if escolha == '1':
        return 'Dinheiro'
    elif escolha == '2':
        tipo = input('1 Crédito\n2 Débito\nEscolha: ')
        return 'Cartão Crédito' if tipo == '1' else 'Cartão Débito'
    elif escolha == '3':
        return 'Pix'

def fazer_pedido(delivery=False):
    endereco = ''

    if delivery:
        tipo = input('Casa ou Apartamento: ').lower()
        rua = input('Endereço: ')
        numero = input('Número/Bloco: ')
        endereco = rua + ', ' + numero

    cliente = input('\nNome: ')

    if cliente not in clientes:
        clientes[cliente] = {"pedidos": 0}

    clientes[cliente]["pedidos"] += 1

    lanches_escolhidos = sugestao_chef()
    lanches_escolhidos += escolher_lanches()
    acompanhamentos_escolhidos = escolher_acompanhamentos()

    bebida = escolher_bebida()
    pagamento = escolher_pagamento()

    total = sum(l[1]*l[2] for l in lanches_escolhidos)
    total += sum(a[1] for a in acompanhamentos_escolhidos)
    total += bebida[1]

    if delivery and total < 60:
        total += 10

    print('\n=== RESUMO ===')
    print('Cliente:', cliente)
    if delivery:
        print('Endereço:', endereco)

    for l in lanches_escolhidos:
        print(l[0], 'x', l[2])

    print('Total: R$', format(total, '.2f'))
    print('Pagamento:', pagamento)

# ================== MENU ==================

print('Olá Mundo! - Quebrei essa maldição 😎')

while True:
    print('\n=== HAMBURGUERIA ===')
    print('1 Fazer Pedido')
    print('2 Delivery')
    print('3 Trabalhe Conosco')
    print('0 Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        fazer_pedido(False)

    elif opcao == '2':
        fazer_pedido(True)

    elif opcao == '3':
        for v in vagas:
            print(v, '-', vagas[v][0])

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Opção inválida')