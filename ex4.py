def colorir(texto, cor): # Função para aplicar cores ao texto usando códigos ANSI
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'ciano': '\033[96m',
        'branco': '\033[97m',
        'reset': '\033[0m'  # Reseta a cor
    }
    return f"{cores[cor]}{texto}{cores['reset']}"

a = input(colorir('Digite algo: ', 'amarelo'))# Entrada do usuário

print(colorir('O tipo primitivo desse valor é ', 'vermelho') + colorir(str(type(a)), 'azul'))# Exibindo informações com cores
print(colorir('Só tem espaços? ', 'vermelho') + colorir(str(a.isspace()), 'azul'))
print(colorir('É um número? ', 'vermelho') + colorir(str(a.isnumeric()), 'azul'))
print(colorir('É alfabético? ', 'vermelho') + colorir(str(a.isalpha()), 'azul'))
print(colorir('É alfanumérico? ', 'vermelho') + colorir(str(a.isalnum()), 'azul'))
print(colorir('Está em maiúscula? ', 'vermelho') + colorir(str(a.isupper()), 'azul'))
print(colorir('Está em minúscula? ', 'vermelho') + colorir(str(a.islower()), 'azul'))