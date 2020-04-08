def operacao():
    operation = input(''' Selecione a operacao desejada:
+ Para soma
- para subtração
* para multiplicação
/ para divisão
r para radiacao
''')
    numero_1 = int(input('Digite o primeiro valor: '))
    numero_2 = int(input('Digite o segundo valor: '))

    if operation == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    elif operation == 'r':
        print('{} ** {} = '.format(numero_1, numero_2))
        print(numero_1 ** numero_2)    

    else:
        print('Voce não escolheu a opção correta. Tente novamente')
    again()

def again():
    calc_again = input('''
Voce quer voltar a calcular?
Digite S para Sim ou N  Nao.
''')
    if calc_again.upper() == 'S':
        tabuada()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

operacao()

