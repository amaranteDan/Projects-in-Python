import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]


#Titulo

titulo = "Scatterplot: Grafico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y)
plt.scatter(x, y, label="Meus Pontos", color="g", marker="h", s=100)
plt.legend()
plt.show()

#plt.savefig("figura1.png" dpi=300) Salva a figura em qualquer formato.

