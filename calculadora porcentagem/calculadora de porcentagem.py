def calcular_porcentagem():
    while True:
        print("\n" + "="*50)
        print("=== CALCULADORA DE PORCENTAGEM TURBO ===")
        print("1. Calcular X% de um valor")  # Opção para calcular uma porcentagem de um valor
        print("2. Calcular qual % X é de Y")  # Opção para calcular qual porcentagem um valor representa de outro
        print("3. Aumento/Redução percentual")  # Opção para calcular aumento ou redução percentual
        print("4. Diferença percentual entre dois valores")  # Opção para calcular a diferença percentual entre dois valores
        print("5. Juros compostos (valor futuro)")  # Opção para calcular juros compostos
        print("6. Desconto em loja (composição de descontos)")  # Opção para calcular descontos compostos em loja
        print("0. Sair")  # Opção para sair do programa
        print("="*50)
        
        try:
            opcao = int(input("Escolha uma opção (0-6): "))  # Recebe a opção do usuário
            
            if opcao == 0:
                print("Até logo!")  # Mensagem de despedida
                break  # Sai do loop e encerra o programa
                
            elif opcao == 1:
                valor = float(input("Digite o valor total: "))  # Valor base para cálculo
                percentual = float(input(f"Qual porcentagem de {valor} você quer calcular? (%): "))  # Percentual a calcular
                resultado = valor * (percentual / 100)  # Cálculo da porcentagem
                print(f"\n{percentual}% de {valor} = {resultado:.2f}")  # Exibe o resultado formatado
                
            elif opcao == 2:
                parte = float(input("Digite o valor parcial: "))  # Parte do valor total
                total = float(input("Digite o valor total: "))  # Valor total
                percentual = (parte / total) * 100  # Cálculo do percentual que a parte representa do total
                print(f"\n{parte} é {percentual:.2f}% de {total}")  # Exibe o resultado
                
            elif opcao == 3:
                valor = float(input("Digite o valor inicial: "))  # Valor inicial para cálculo
                percentual = float(input("Digite a porcentagem de aumento/redução (%): "))  # Percentual de aumento ou redução
                if percentual >= 0:
                    resultado = valor * (1 + percentual/100)  # Cálculo para aumento percentual
                    print(f"\n{valor} + {percentual}% = {resultado:.2f}")  # Exibe o resultado
                else:
                    resultado = valor * (1 - abs(percentual)/100)  # Cálculo para redução percentual
                    print(f"\n{valor} - {abs(percentual)}% = {resultado:.2f}")  # Exibe o resultado
                    
            elif opcao == 4:
                valor1 = float(input("Digite o primeiro valor: "))  # Primeiro valor para comparação
                valor2 = float(input("Digite o segundo valor: "))  # Segundo valor para comparação
                diferenca = ((valor2 - valor1) / abs(valor1)) * 100  # Cálculo da diferença percentual
                if valor2 > valor1:
                    print(f"\nAumento de {diferenca:.2f}% (de {valor1} para {valor2})")  # Exibe aumento percentual
                else:
                    print(f"\nRedução de {abs(diferenca):.2f}% (de {valor1} para {valor2})")  # Exibe redução percentual
                    
            elif opcao == 5:
                principal = float(input("Valor inicial (R$): "))  # Valor principal inicial
                taxa = float(input("Taxa de juros ao período (%): ")) / 100  # Taxa de juros convertida para decimal
                periodos = int(input("Número de períodos: "))  # Número de períodos para cálculo
                montante = principal * (1 + taxa) ** periodos  # Cálculo do montante com juros compostos
                print(f"\nValor futuro após {periodos} períodos = R$ {montante:.2f}")  # Exibe o valor futuro
                print(f"Juros acumulados = R$ {(montante - principal):.2f}")  # Exibe os juros acumulados
                
            elif opcao == 6:
                preco = float(input("Preço original (R$): "))  # Preço original do produto
                descontos = input("Descontos (% separados por espaço): ").split()  # Lista de descontos a aplicar
                final = preco  # Inicializa o preço final
                for d in descontos:
                    final *= (1 - float(d)/100)  # Aplica cada desconto sequencialmente
                economia = preco - final  # Calcula a economia total
                print(f"\nPreço final: R$ {final:.2f}")  # Exibe o preço final após descontos
                print(f"Você economizou: R$ {economia:.2f}")  # Exibe o valor economizado
                print(f"Desconto total: {100 * (economia/preco):.2f}%")  # Exibe o desconto total percentual
                
            else:
                print("Opção inválida! Digite 0, 1, 2, 3, 4, 5 ou 6.")  # Mensagem para opção inválida
                
        except ValueError:
            print("Erro: Digite apenas números!")  # Tratamento para erro de valor inválido
        except ZeroDivisionError:
            print("Erro: O valor não pode ser zero nesta operação!")  # Tratamento para divisão por zero
        except Exception as e:
            print(f"Erro inesperado: {e}")  # Tratamento para outros erros inesperados

# Inicia a calculadora
if __name__ == "__main__":
    calcular_porcentagem()
