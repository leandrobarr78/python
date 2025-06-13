def calcular_fatorial(n):
    """Calcula o fatorial de um número inteiro positivo"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)  # Recursão

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero < 0:
            print("Erro: O número deve ser positivo!")
            continue  # Volta ao início do loop
        
        resultado = calcular_fatorial(numero)
        print(f"\nO fatorial de {numero} é: {resultado}")
        
        # Mostra o cálculo passo a passo (opcional)
        print("\nDetalhamento do cálculo:")
        for i in range(numero, 0, -1):
            print(f"{i} {'×' if i > 1 else '='} ", end="")
        print(f"{resultado}\n")
        
        break  # Encerra após cálculo válido
    
    except ValueError:
        print("Erro: Digite apenas números inteiros!")