from time import sleep
menu = '''

[d] DEPOSITAR 
[e] EXTRATO
[s] SACAR
[q] SAIR

--> '''

saldo = s = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

def titulo(a):
    print(60*'-')
    print('{:^60}'.format(a))
    print(60*'-')

while True:
    opcao = input(menu).lower().strip()

    if opcao == 'd':
        titulo('DEPÓSITO')
        s = float(input('Digite o valor que será depositado:  R$'))
        saldo += s
        extrato += f'+R${s}\n'

    elif opcao == 's':
        if numero_saques != limite_saques:
            titulo('SAQUE')
            numero_saques += 1
            s = float(input('Digite o valor que será sacado:  R$'))
            if s > saldo:
                print('ERRO, VOCÊ NÃO POSSUI ESSE VALOR NA CONTA')
            else:
                saldo -= s
                extrato += f'-R${s:.2f}\n'
        else:
            print('VOCÊ JÁ ATINGIU O LIMITE DO NÚMERO DE SAQUES DIÁRIOS. TENTE NOVAMENTE AMANHÃ')

    elif opcao == 'e':
        titulo('EXTRATO')
        print(extrato)
        print(f'TOTAL: R${saldo:.2f}')

    elif opcao == 'q':
        print('\nATÉ MAIS! VOLTE SEMPRE')
        break
    sleep(2)
