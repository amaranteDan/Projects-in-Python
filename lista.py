def main ():
    
     

main()    

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
