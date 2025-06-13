def eh_primo(num):
    """Verifica se um número é primo de forma otimizada"""
    if num <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    if num == 2:
        return True  # 2 é o único primo par
    if num % 2 == 0:
        return False  # Números pares maiores que 2 não são primos
    
    # Verifica divisores ímpares até a raiz quadrada do número
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Entrada do usuário com tratamento de erros
while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número positivo!")
            continue
        
        if eh_primo(numero):
            print(f"\n{numero} é um número primo!")
        else:
            print(f"\n{numero} NÃO é primo.")
        break
    
    except ValueError:
        print("Erro: Digite apenas números inteiros!")