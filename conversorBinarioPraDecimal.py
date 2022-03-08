binario = (int(input("Digite o número binário que deseja converter: ")))

#valor guardado
binarioInit = binario

#número de digitos
qtd = int(len(str(binario)))    

#lista para guardar as sobras
listSobra = []

#loop para receber as sobras, que serão os números digitados pelo usuário, em ordem decrescente
while binario > 0:   
    sobra = binario % 10
    binario = binario // 10
    listSobra.append(sobra)

#checa os números presente na lista e caso o valor solicitado não seja binário, o programa para.
for i in range(0, qtd):
    if listSobra[i] > 1:
        print(binarioInit,"não é um número binário. Apenas os números 0 e 1 são de representação binária")
        exit()

#lista para guardar os valores da exponenciação
listFatoracao = []

#loop para os valores da exponenciação de acordo com o número de dígitos
for i in range(0, qtd):
    base = 2 ** i
    listFatoracao.append(base)
 
#multiplica os números das duas listas
decimalList = list(map(lambda x,y: x*y ,listSobra,listFatoracao))

#soma os números da lista multiplicada
decimal = sum(decimalList)

#resultado
print(binarioInit,"em decimal é:" ,decimal)
 











