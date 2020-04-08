def main ():
        lucro = float(input("Digite o valor do lucro: "))
        imposto = lucro * 0.26 #Usar sempre ponto.
        resultado = "Sobre lucro de R${0} voce devera pagar R${1} de imposto" .format(lucro, imposto)
        print(imposto)


main()
        
