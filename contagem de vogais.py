def contar_vogais(frase):
    """Conta quantas vogais (a, e, i, o, u) existem na frase, ignorando acentos"""
    vogais = 'aeiouáéíóúàèìòùãõâêîôûäëïöü'  # Inclui vogais com acentos
    contador = 0
    
    # Normaliza para minúsculas e conta cada caractere
    for letra in frase.lower():
        # Remove acentos (opcional)
        letra_sem_acento = remove_acentos(letra) if 'áéíóú' in vogais else letra
        if letra_sem_acento in 'aeiou':
            contador += 1
    return contador

def remove_acentos(letra):
    """Remove acentos de vogais (opcional)"""
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
               'à':'a', 'è':'e', 'ì':'i', 'ò':'o', 'ù':'u',
               'ã':'a', 'õ':'o', 'â':'a', 'ê':'e', 'î':'i', 'ô':'o', 'û':'u',
               'ä':'a', 'ë':'e', 'ï':'i', 'ö':'o', 'ü':'u'}
    return acentos.get(letra, letra)

# Programa principal
while True:
    try:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            print("Programa encerrado!")
            break
        
        total_vogais = contar_vogais(frase)
        print(f"\nA frase possui {total_vogais} vogais.")
        print(f"Frase original: {frase}")
        print("-" * 40)
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break