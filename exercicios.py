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
#     numero_1 = float(input("Digite um número: "))
#     numero_2 = float(input("Digite um segundo número: "))
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



# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

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
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

    # data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")

    # data_separada = data_usuario.split("/")

    # print(f"O dia é {data_separada[0]}")
    # print(f"O mês é {data_separada[1]}")
    # print(f"O ano é {data_separada[2]}")

# --------------------------------------------------

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.



# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
