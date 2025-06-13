while True:  # Loop principal
    print("\n--- GERADOR DE TABUADAS ---")
    print("1: Adição (+)")
    print("2: Subtração (-)")
    print("3: Multiplicação (×)")
    print("4: Divisão (÷)")
    print("0: Sair")
    
    try:
        opcao = int(input("Escolha uma operação (0-4): "))
        if opcao == 0:
            print("Programa encerrado. Até mais!")
            break  # Sai do loop
        
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida. Digite um número entre 0 e 4.")
            continue  # Volta ao início do loop
        
        numero = int(input("Digite um número para a tabuada: "))
        print(f"\nTabuada do {numero} ({'+-×÷'[opcao-1]}):")
        
        for i in range(1, 11):
            if opcao == 1:  # Adição
                resultado = numero + i
                print(f"{numero} + {i:2} = {resultado:3}")
            elif opcao == 2:  # Subtração
                resultado = numero - i
                print(f"{numero} - {i:2} = {resultado:3}")
            elif opcao == 3:  # Multiplicação
                resultado = numero * i
                print(f"{numero} × {i:2} = {resultado:3}")
            elif opcao == 4:  # Divisão
                if i == 0:
                    print(f"{numero} ÷ {i:2} = Indefinido (divisão por zero)")
                else:
                    resultado = numero / i
                    print(f"{numero} ÷ {i:2} = {resultado:.2f}")  # 2 casas decimais
    
    except ValueError:  # Erro se digitar texto em vez de número
        print("Erro: Digite apenas números inteiros!")
    except ZeroDivisionError:  # Trata divisão por zero (caso específico)
        print("Erro: Divisão por zero não permitida!")