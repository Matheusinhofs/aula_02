# data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")

# data_separada = data_usuario.split("/")

# print(f"O dia é {data_separada[0]}")
# print(f"O mês é {data_separada[1]}")
# print(f"O ano é {data_separada[2]}")

# QUALQUER COISA QUE VAI INTERAGIR E ESTA FORA DO SEU CONTROLE É BOM TER ESSE TRATAMENTO

# try:
#     numero_01 = int(input("Digite um numero inteiro: "))
#     numero_02 = int(input("Digite outro numero inteiro: "))
#     resultado = numero_01 // numero_02
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except KeyboardInterrupt:
#     print("acho que vc não quis digitar um número")

# # Exemplo que causa TypeError
# nome = 7
# try:
#     resultado = len(nome)
#     print(resultado)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro

# # TYPEERROR TRAZ A MENSAGEM DE ERRO PRO USUÁRIO
# # USA EM QUASE QUALQUER COISA ESSE TRY EXCEPT

# nome = 5
# try:
#     resultado = len(nome)
#     print(resultado)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro
# else:
#     print("deu tudo certo")

# # O ELSE ELE VAI RODAR SE DER CERTO
# finally:
#     print("você pelo menos tentou")
# # O FINALLY RODA DE QUALQUER FORMA



nome = 5
numero = int(input("Digite um número: "))
# VERIFICA SE A VARIÁVEL É DO TIPO QUE DESEJA
if isinstance(numero,int):
    print("seu número é um inteiro")
else:
    print("deu tudo certo")


