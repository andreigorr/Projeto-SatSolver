import itertools

#--Entrada
entrada = input()
inputs = entrada.split(" ")
variaveis = int(inputs[2])
clausulas = int(inputs[3])

#---Pedindo as variáveis com base nas clausulas e formando o dicionário
cls=[[] for i in range(clausulas)]
for i in range(clausulas):
    x=input()
    cls[i]=x.split()
resultado = {'cls':cls}
c=resultado['cls']

#--retorna subseqüências de comprimento de elementos da entrada por conta das conbinações
list1=[]
list2=[]
for num in c:
      for n in num:
            ni=int(n)
            list1.append(ni)
      list2.append(list1)
      list1 = []
varlist=[]
for t in range(variaveis):
	t=t+1
	varlist.append(t)

#---Usando a biblioteca pois se a entrada iterável for classificada, as tuplas de combinação serão produzidas na ordem classificada
perm=set(itertools.combinations_with_replacement([1, 0, 1], variaveis))
permlist=[]
for i in perm:
	permlist.append(i)
fim=0

#--Recebe a permutação lendo o conteúdo da lista e verifica se a soma é maior que 0(que no caso nao seria satisfativel) e se for = 0 seria satisfatível e atribue se é True ou False.

for per in permlist:
	contador=0
	input=0
	list3=[]
	for j in list2:
		a=[]
		const=0
		for i in j:
			if i<0:
				if per[const]==1:
					a.append(int(0))
				else:
					a.append(int(1))
			elif i>0:
				  a.append(int(per[const]))
			else:
				break
			const+=1
		list3.append(a)
  
#--A list3 vai ser lida e para cada caso satisfatível vai ser adicionado 1 no contador.
	for i in list3:
		for i in i:
			if i==1:
				contador+=1
				break

#--Adiciono 1 para cada permutação
	if contador == clausulas:
		fim+=1

if fim>0:
	print("Satisfiable")
else:
	print("Unsatisfiable")