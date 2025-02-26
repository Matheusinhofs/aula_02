import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

    # try:
    #     numero_1 = int(input("Digite o primeiro número: "))
    #     numero_2 = int(input("Digite o segundo número: "))

    #     soma = numero_1 + numero_2
    # except ValueError:
    #     print("Tipo de dado não passível de soma, por favor digite um número")  # Imprime a mensagem de erro:
    #     # print("Divisão por zero não aceita")
    # else:
    #     print(f"A soma dos números é {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero_1 = float(input("Digite o primeiro número: "))

# if isinstance(numero_1,float):
#     resto_divisao = numero_1 % 5 
#     print(f"O resto da divisão dos números é {resto_divisao}")
# else:
#     print("Tipo de dado não compatível, por favor digite um número")  # Imprime a mensagem de erro:
#     # print("Divisão por zero não aceita")
    
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# try:
#     numero_1 = int(input("Digite um número: "))
#     numero_2 = int(input("Digite um segundo número: "))
#     multiplicacao = numero_1 * numero_2
# except ValueError:
#     print("Digite um número válido")
# else: 
#     print(f"A mutiplicação de {numero_1} por {numero_2} é igual a {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_1 = int(input("Digite o primeiro número: "))
# numero_2 = int(input("Digite o segundo número: "))

# div_inteira = numero_1 // numero_2

# print(div_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero_1 = int(input("Digite o primeiro número: "))

# try:
#     quadrado = numero_1 ** 2 
# except ValueError:
#      print("Digite um número válido")
# else: 
#      print(f"O quadro de {numero_1} é {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# try:
#     numero_1 = float(input("Digite o primeiro número: "))
#     numero_2 = float(input("Digite o segundo número: "))
#     soma = numero_1 + numero_2
# except ValueError:
#     print("Digite um número válido")
# else:
#     print(soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# try:
#     numero_1 = float(input("Digite o primeiro número: "))
#     numero_2 = float(input("Digite o segundo número: "))
#     media = (numero_1 + numero_2)/2
# except ValueError:
#     print("Digite um número válido")
# else:
#     print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# try:
#     numero_1 = float(input("Digite a base da potência: "))
#     numero_2 = float(input("Digite o expoente da potência: "))
#     resultado = numero_1 ** numero_2
# except ValueError:
#     print("Digite um número válido")
# else:
#     print(f"O valor da potência é: {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# try:
#     temperatura_c = float(input("Digite a temperatura em Celsius: "))
#     temperatura_f = (temperatura_c * (9/5)) + 32
# except ValueError:
#     print("Digite uma temperatura válida")
# else:
#     print(f"O valor da temperatura em Fahrenheit é: {temperatura_f}")

# --------------------------------------------------
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Digite o raio do círculo: "))

# area = 2*math.pi*(raio**2)

# print(area)

# area_formatada = {f"{area:.2f}"}

# print(f"Área formatada = {area_formatada}")

# --------------------------------------------------
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# try:
#     nome = input("Digite uma palavra: ")
#     nome_maiusculo = nome.upper()
# except TypeError as e:
#     print(e)
# else: 
#     print(nome_maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# try:
#     nome = input("Digite seu nome completo: ")
#     nome_minusculo = nome.lower()
# except TypeError as e:
#     print(e)
# else: 
#     print(nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# try:
#     frase = input("Digite uma frase: ")
#     frase_sem_espaco = frase.strip()
# except TypeError as e:
#     print(e)
# else:
#     print(frase_sem_espaco)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

    # data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")

    # data_separada = data_usuario.split("/")

    # print(f"O dia é {data_separada[0]}")
    # print(f"O mês é {data_separada[1]}")
    # print(f"O ano é {data_separada[2]}")

# --------------------------------------------------

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# try:
#     palavra_1 = input("Digite uma palavra: ")
#     palavra_2 = input("Digite a segunda palavra: ")
#     concatenado = palavra_1 + palavra_2
# except TypeError as e:
#     print(e)
# else: 
#     print(concatenado)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# try:
#     bool_1 = False
#     bool_2 = True
#     concatenado = bool_1 and bool_2
# except TypeError as e:
#     print(e)
# else: 
#     print(concatenado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# try:
#     bool_1 = False
#     bool_2 = True
#     concatenado = bool_1 or bool_2
# except TypeError as e:
#     print(e)
# else: 
#     print(concatenado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# Se só der um enter ele retorna falso, ai no not funciona

# try:
#     bool_2 = bool(input("Digite um valor booleano:"))
#     inverter = not bool_2
# except TypeError as e:
#     print(e)
# else: 
#     print(inverter)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# try:
#     nr_01 = int(input("Digite o primeiro número: "))
#     nr_02 = int(input("Digite o segundo número: "))
# except TypeError as e:
#     print(e)
# else:
#     if nr_01 == nr_02:
#         print("Os dois números são iguais")
#     else:
#         print("Os dois números são diferentes")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# try:
#     nr_01 = int(input("Digite o primeiro número: "))
#     nr_02 = int(input("Digite o segundo número: "))
# except TypeError as e:
#     print(e)
# else:
#     if nr_01 != nr_02:
#         print("Os dois números são diferentes")
#     else:
#          print("Os dois números são iguais")

# #### try-except e if

# 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except,
# garantir que a entrada seja numérica, tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (1.8 * celsius) + 32
# except ValueError:
#     print("Digite um valor correto animal")
# else:
#     print(f"Temperatura final é de {fahrenheit} graus Fahrenheit")

# 22: Verificador de Palíndromo

# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# palavra = input("Digite a palavra ou frase que é um palíndromo: ")
# palavra_invertida = palavra[::-1]
# if palavra == palavra_invertida:
#     print(f"A palavra {palavra} é um palíndromo")
# else:
#     print("A palavra não é um palíndromo")

# 23: Calculadora Simples

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     operacao = input("Digite a operação desejada: ")
#     numero_01 = float(input("Digite o primeiro número da operação: "))
#     numero_02 = float(input("Digite o segundo número da operação: "))

#     if operacao == "+":
#         resultado = numero_01 + numero_02
#         print(f"O resultado da sua operação é ", resultado)
#     elif operacao == "-":
#         resultado = numero_01 - numero_02
#         print(f"O resultado da sua operação é ", resultado)
#     elif operacao == "/" and numero_02 != 0:
#         resultado = numero_01 / numero_02
#         print(f"O resultado da sua operação é ", resultado)
#     elif operacao == "*":
#         resultado = numero_01 * numero_02
#         print(f"O resultado da sua operação é ", resultado)
#     else: 
#         print("Operação Inválida ou divisão por zero")
# except ValueError:
#     print("Digite um valor válido")

# 24: Classificador de Números

# Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica 
# e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     numero_01 = float(input("Digite um número: "))
#     if numero_01 > 0:
#         print("Número positivo!!!")
#     elif numero_01 == 0:
#         print("Número igual a zero!!!")
#     else:
#         print("Número negativo!!!")
    
#     resto = numero_01 % 2

#     if resto == 0:
#         print("Número é par!!!")
#     else:
#         print("Número é ímpar!!!")
# except ValueError:
#     print("Entrada não numérica")    
    

# 25: Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número 
# e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

# lista_solicitada: list = []
# lista_numeros = []

# lista_usuario = input("Digite uma lista de números: ")

# try:
#     lista_solicitada = list(lista_usuario)

#     for i in lista_solicitada:
#         if i != ",":
#             lista_numeros.append(int(i))
# except TypeError as e:
#     print(e)
# else:
#     print(lista_numeros)

# RESPOSTA LUCIANO

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")