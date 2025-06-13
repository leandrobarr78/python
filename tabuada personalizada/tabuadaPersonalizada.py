# -*- coding: utf-8 -*-
import sys
import os

# Configura o encoding para Windows (isso é crucial!)
if sys.stdout.encoding != 'utf-8':
    os.system('chcp 65001 > nul')  # Altera o código página para UTF-8
    sys.stdout.reconfigure(encoding='utf-8')

def verificar_par_impar(num):
    return "PAR" if num % 2 == 0 else "ÍMPAR"  # Retorna se o número é par ou ímpar

def mostrar_menu():
    print("\n" + "="*50)
    print("=== TABUADA UNIVERSAL ===")
    print("1. Tabuada padrão (multiplicação)")  # Opção para tabuada de multiplicação padrão
    print("2. Tabuada personalizada")  # Opção para tabuada com operações personalizadas
    print("3. Verificar par/ímpar")  # Opção para verificar se o número é par ou ímpar
    print("0. Sair")  # Opção para sair do programa
    print("="*50)

def gerar_tabuada_padrao(num):
    print(f"\nTabuada de multiplicação do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i:2} = {num * i:3}")  # Exibe a multiplicação do número de 1 a 10

def gerar_tabuada_personalizada(num):
    operacoes = {
        '+': ('Adição', lambda a, b: a + b),
        '-': ('Subtração', lambda a, b: a - b),
        '*': ('Multiplicação', lambda a, b: a * b),
        '/': ('Divisão', lambda a, b: a / b if b != 0 else "ERRO")  # Evita divisão por zero
    }
    
    print("\nOperações disponíveis:")
    for simbolo, (nome, _) in operacoes.items():
        print(f" {simbolo} : {nome}")  # Lista as operações disponíveis
    
    operacao = input("Escolha a operação: ").strip()
    while operacao not in operacoes:
        print("Operação inválida! Use:", ", ".join(operacoes.keys()))
        operacao = input("Tente novamente: ").strip()
    
    # Validação do intervalo
    while True:
        try:
            inicio = int(input("Início do intervalo: "))  # Início do intervalo para a tabuada
            fim = int(input("Fim do intervalo: "))  # Fim do intervalo para a tabuada
            if inicio > fim:
                print("Erro: O início deve ser menor ou igual ao fim!")
                continue
            break
        except ValueError:
            print("Digite apenas números inteiros!")
    
    print(f"\nTabuada do {num} ({operacoes[operacao][0]}):")
    for i in range(inicio, fim + 1):
        resultado = operacoes[operacao][1](num, i)  # Calcula o resultado da operação
        print(f"{num} {operacao} {i:2} = {resultado:>5}")  # Exibe o resultado formatado

# Programa principal
while True:
    mostrar_menu()
    try:
        opcao = int(input("Opção: "))  # Recebe a opção do usuário
        if opcao == 0:
            print("Até logo!")  # Mensagem de despedida
            break  # Sai do programa
        num = int(input("Digite um número: "))  # Recebe o número para a tabuada
        print(f"» {num} é {verificar_par_impar(num)}")  # Exibe se o número é par ou ímpar
        
        if opcao == 1:
            gerar_tabuada_padrao(num)  # Gera tabuada padrão
        elif opcao == 2:
            gerar_tabuada_personalizada(num)  # Gera tabuada personalizada
        elif opcao == 3:
            continue  # Apenas verifica par/ímpar, volta ao menu
        else:
            print("Opção inválida!")  # Mensagem para opção inválida
    except ValueError:
        print("Erro: Digite apenas números!")  # Tratamento para erro de valor inválido
