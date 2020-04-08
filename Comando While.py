def main ():
        n = int(input("Digite o valor de n: "))
        k = int (input("Digite o valor de k: "))

        pot = 1
        i   = 0
        while i < k:
            pot = pot * n
            i   = i + 1


        print("A potencia e: ", pot)
        print ("O valor de %d elevado a %d e %d" %(n, k, pot))
        print("---------------------------------------------")
        print("\n\n")
                 
main()


        
            
