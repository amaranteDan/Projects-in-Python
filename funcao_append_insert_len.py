def main ():
        a = [1, 2, 3, 4]
        a.append(6) #Adicionando o 6 ao final da lista
        print(a)
        [1, 2, 3, 4, 5, 6]
        a.insert(0, 0.0) #Adicionando o 0.0 na posição 0
        print(a)
        [0.0, 1, 2, 3, 4, 5, 6]
        print(len(a)) #Mostra o numero de elementos da lista.
        a[2:4] = [5.0, 5.0] #Modifica trecho da lista
        print(a)
main ()
