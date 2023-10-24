#%%Roteiro
"""
Sites de ajuda
Variáveis
Print
Listas
Vetores
Range
Loop For
Construindo listas com for
if...elif.else
Gráficos
Funções
"""
#%%Sites de Ajuda
https://www.w3schools.com/python/default.asp
https://stackoverflow.com/
https://www.python.org/
#%%Variáveis
"Variáveis são containers para armazenamentos de dados"
"Python não necessita de declaração de variáveis"
'Tipos de dados'
    #Text Type : str
    #Numeric Type : int,float,complex
    #Sequence Type : list,tuple, range
    #Mapping Type : dict
    #Set Type : set, frozenset
    #Boolean Type : bool
    #Binary Type : bytes, bytearry, memoryview
"Exemplo"
x=str(3) # x will be '3'
y=int(3) # y will be 3
z=float(3) #z will be 3.0 
#%%Print
"Python exibe valor de uma variável"
a=1
print(a)

a=1
a=2
print(a)

#%%Lista
"Listas são usadas para armazenar diversos itens em uma única variável"
lista=["carro","moto","caminhão"]
print(lista)

#É possivel acessar os elementos da lista, mas a ordem começa por 0
print(lista[0])

#Funções importantes para lista
"len() :retorna o tamanho da lista"
print(len(lista))

"lista.append(elemento) : insere o elemento no final da lista  "
lista.append("barco")
print(lista)

#%%Vetores
"Se parecem com listas, porém é possível realizar operações vetoriais"
#Para trabalhar com vetores, é necessário importar a biblioteca numpy
import numpy as np
vetor=np.array([1,2,3])
print(vetor)

#Com vetores é possível realizar calculos vetoriais
print(np.dot(vetor,vetor)) #função np.dot() :é o somarproduto do numpy , os elementos devem ser do mesmo tamanho

#%%Range
"Função que cria sequências que podem ser convertidas em listas"
#range(y) : cria uma sequência de y elementos, começando do 0 e terminando em y-1

a=range(10)
print(a)
print(list(a))

#range(x,y) : cria uma sequeência de números inteiros, começando em x e terminado em y-1
a=range(1,6)
print(a)
print(list(a))

#range(x,y,z) : cria uma sequência, começando em x, terminando em y-1, com intervalo de z
a=range(10,0,-1)
print(a)
print(list(a))

#%%Loop for
"Usado para iterar dentro de uma sequência (range,lisra,tupla,dicionário,set ou string"
#As instruções dentro do loop for devem estar indentadas comparando com o for

lista=["carro","moto","caminhão"]
for i in lista:
    print(i)

for i in range(3):
    print(i)

nome="João"

for i in nome:
    print(i)

#%%Contruindo listas com for
"Usa-se o for para contruir listas com sequências que dependem de outras listas"

lista=[]
for i in range(3):
    lista.append(i)
print(lista)

#Exemplo de for dentro de uma lista
lista=[]
lista=[i**2 for i in range(3)]
print(lista)

#%%if...elif...else
"Usado para executar ações apenas quando algum critério é atingido"
#Operadores de comparação
"""
igualdade : x==y
diferença x!=y
menor que : x<y
menor igual que : x<=y
maior que : x>y
maior igual que : x>=y
"""
a=2
b=1
if a>b:
    print("a é maior que b")

a=1
b=1
if a>b:
     print("a maior que b")
else:
    print("a não é maior que b")
    
a=1
b=1
if a>b:
     print("a maior que b")
elif a==b:
    print("a igual a b")
else:
    print("a não é maior que b")

for i in range(3):
    if i>1:
        print(i,"maior que 1")
    else:
        print(i,"menor ou igual a 1")

#%%Gráficos
"Gráfico de linha"
import matplotlib.pyplot as plt
eixox=[0,1,2,3]
eixoy=[0,1,4,9]
plt.plot(eixox,eixoy)
plt.show()

#%%Funções
"Usadas quando se repete a mesma tarefa diversas vezes"

def bomdia(nome):
    print("Bom dia, ",nome," !")

lista=["João","Vanessa","Maria","Ana"]
for nome in lista:
    bomdia(nome)