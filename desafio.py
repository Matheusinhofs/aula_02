
CONSTANTE_BONUS: float = 1000.00


try:
    nome: str = input("Digite seu nome: ")
    
    if nome.isdigit():
        print("Nome inválido!!!")
        exit()
    elif nome.isspace():
        print("Você não digitou seu nome")
        exit()
    elif len(nome) == 0:
        print("Você não digitou seu nome")
        exit()
    else: 
        salario: float = float(input("Digite seu salário: "))
        bonus: float = float(input("Digite seu bônus: "))
except ValueError:
    print("Digite um valor válido")
else:
    if isinstance(salario, float) and isinstance(bonus, float):
        kpi: float = CONSTANTE_BONUS + (salario * bonus)
        if salario < 0 or bonus < 0:
            print("Salário ou bônus não podem ser negativos")
            exit()
    else:
        print("Digite um número para o salário e o bônus por favor")
        exit()
    print(f"Olá  {nome}  o seu bônus foi de {kpi}")

# RESPOSTA LUCIANO

# # Solicita ao usuário que digite seu nome
# try:
#     nome = input("Digite seu nome: ")

#     # Verifica se o nome está vazio
#     if len(nome) == 0:
#         raise ValueError("O nome não pode estar vazio.")
#         exit()
#     # Verifica se há números no nome
#     elif any(char.isdigit() for char in nome):
#         raise ValueError("O nome não deve conter números.")
#         exit()
#     else:
#         print("Nome válido:", nome)
# except ValueError as e:
#     print(e)
#     exit()

# # Solicita ao usuário que digite o valor do seu salário e converte para float

# try:
#     salario = float(input("Digite o valor do seu salário: "))
#     if salario < 0:
#         print("Por favor, digite um valor positivo para o salário.")
# except ValueError:
#     print("Entrada inválida para o salário. Por favor, digite um número.")
#     exit()

# # Solicita ao usuário que digite o valor do bônus recebido e converte para float
# try:
#     bonus = float(input("Digite o valor do bônus recebido: "))
#     if bonus < 0:
#         print("Por favor, digite um valor positivo para o bônus.")
# except ValueError:
#     print("Entrada inválida para o bônus. Por favor, digite um número.")
#     exit()

# bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# # Imprime as informações para o usuário
# print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")