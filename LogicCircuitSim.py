#essa parte lê o arquivo
dic = {}
with open("entrada.txt", "r") as file:
    text = file.read()
    exec(text) #criar dicionário
    dic_name = text[0:2] #pegar o nome desse dicionário
    exec("dic = " + dic_name) #usar o nome "dic" para o dicionário no resto do código independente do nome do arquivo de entrada
  
#essa próxima parte cria uma lista de todas as combinações binárias para as entradas
variaveis = dic["entradas"]
combs = []
for i in range(pow(2, len(variaveis))):
    bin = format(int(i), 'b')
    while (len(variaveis) != len(bin)):
        bin = "0" + bin
    combs.append(list(bin))
  
results = [] #criar uma lista para todos os resultados

for comb in combs: #para cada combinação de valores binários, criar variáveis com nome das entradas
    k = 0
    for en in variaveis:
        exec(en + " = bool(" + comb[k] + ")")
        k = k + 1
    for gate in dic["gates"]: #para cada porta, averiguar o tipo, executar as operações necessárias com os valores de entrada e definir a saída dele com o nome e valor correto
        op = dic[gate][0]
        if op == "not":
            exec(dic[gate][1] + " = not(" + dic[gate][2] + ")")
            #simplesmente inverte a entrada
        elif op == "and":
            parc = 1 #definir "resultado parcial" inicial (para AND ele precisa ser 1, pois é o elemento neutro desta operação)
            for i in range(len(dic[gate]) - 2): #ver quantas entradas o AND tem, para repetir a operação quantas vezes forem necessárias, de 2 em 2 valores
                exec("parc = parc and " + dic[gate][i+2])
            exec(dic[gate][1] + " = " + str(parc))
        elif op == "or":
            parc = 0 #definir "resultado parcial" inicial (para OR ele precisa ser 0, pois é o elemento neutro desta operação)
            for i in range(len(dic[gate]) - 2): #ver quantas entradas o OR tem, para repetir a operação quantas vezes forem necessárias, de 2 em 2 valores
                exec("parc = parc or " + dic[gate][i+2])
            exec(dic[gate][1] + " = " + str(parc))
        elif op == "nand":
            parc = 1
            for i in range(len(dic[gate]) - 2):
                exec("parc = parc and " + dic[gate][i+2])
            exec(dic[gate][1] + " = not(" + str(parc) + ")") #mesmo que AND mas inverte o valor no final
        elif op == "nor":
            parc = 0
            for i in range(len(dic[gate]) - 2):
                exec("parc = parc or " + dic[gate][i+2]) #mesmo que OR mas inverte o valor no final
            exec(dic[gate][1] + " = not(" + str(parc) + ")")
        elif op == "xor":
            parc = 0 #definir "resultado parcial" inicial (para XOR ele precisa ser 0, pois é o elemento neutro desta operação)
            for i in range(len(dic[gate]) - 2): #ver quantas entradas o OR tem, para repetir a operação quantas vezes forem necessárias, de 2 em 2 valores
                exec("parc = (parc != " + str(dic[gate][i+2]) + ")")
            exec(dic[gate][1] + " = " + str(parc))
    saidas = []
    for sa in dic["saidas"]: #criar uma lista com todas as saídas, e adicionar essa lista para a lista de todos os resultados
        exec("saidas.append(" + sa + ")")
    results.append(saidas)
  
#a próxima parte cria o arquivo de saída
with open("saida.txt", "w") as file:
    file.write("")
with open("saida.txt", "a") as file:
    file.write("[IN], [OUT] \n")
    for index in range (0, (len(combs))):
        file.write(str(combs[index]) + ", " + str(results[index]) +" \n")
