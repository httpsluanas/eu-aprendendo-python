import math

num1 = input("Digite o primeiro número: ")

if num1 == "pi":
   num1 = float(math.pi)
else:
   num1 = float(num1)

raiz = math.sqrt(num1)
cosseno = math.cos(num1)
seno = math.sin(num1)
tangente = math.tan(num1)
   
operacao = input("Agora, solicite a operação (+ = Adição; - = Subtração; x = Multiplicação; : = Divisão; ^ = Potenciação; media = Média; / = Raiz Quadrada; cos = Cosseno; sin = Seno; tan = Tangente.) : ")

if operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/" and operacao != "**" and operacao != "*" and operacao != "/" and operacao != "cos" and operacao != "sin" and operacao != "tan" and operacao != "media":
   print("Solicite uma operação válida")

#operacao com apenas um numero
elif operacao == "/":
      print("A raiz quadrada de ",num1, "é", raiz)
elif operacao == "cos":
      print("O cosseno de ",num1, "é", cosseno)
elif operacao == "sin":
      print("O seno de ",num1, "é",("%.2f" % seno))
elif operacao == "tan":
      print("A tangente de ",num1, "é",("%.2f" % tangente))
#operacao com mais de um numero
else:
      num2 = float(input("Digite o segundo número: ")) 
         
      
if operacao == "+":
    print("O resultado da conta é: ",num1 + num2)
elif operacao == "-":
    print("O resultado da conta é: ",num1 - num2)
elif operacao == "*":
    print("O resultado da conta é: ",num1 * num2)
elif operacao == ":":
    print("O resultado da conta é: ",num1 / num2)
elif operacao == "^":
    print("O resultado da conta é: ",num1 ** num2)
elif operacao == "media":
    print("O resultado da conta é: ",(num1 + num2) / 2)

