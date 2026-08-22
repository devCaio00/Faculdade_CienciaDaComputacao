def comprimir_rle(texto):
    # Se o texto estiver vazio, não há nada para comprimir
    if not texto:
        return ""

    resultado = ""
    caractere_atual = texto[0]  # Começa pela primeira letra
    contador = 1

    # Percorre do segundo caractere (índice 1) até o final do texto
    for i in range(1, len(texto)):
        proximo_caractere = texto[i]

        if proximo_caractere == caractere_atual:
            # Se a letra é igual à anterior, só somamos 1 ao contador
            contador += 1
        else:
            # Se a letra mudou, guardamos a letra anterior e sua contagem no resultado
            resultado += caractere_atual + str(contador)

            # Atualizamos as variáveis para a nova letra que acabou de começar
            caractere_atual = proximo_caractere
            contador = 1

    # Adiciona o último caractere e sua contagem ao resultado
    resultado += caractere_atual + str(contador)
    return resultado

# --- Bloco Principal de Teste ---
if __name__ == "__main__":
    print("=== COMPRESSOR DE TEXTO RUN-LENGTH ENCODING (RLE) ===")
    texto_original = input("Digite um texto com caracteres repetidos (ex: AAAAAABBBCCCC): ")

    texto_comprimido = comprimir_rle(texto_original)

    print("\n--- Resultados ---")
    print(f"Texto Original   : {texto_original}")
    print(f"Texto Comprimido : {texto_comprimido}")

    # Calculando a taxa de compressão
    tamanho_orig = len(texto_original)
    tamanho_comp = len(texto_comprimido)
    if tamanho_orig > 0:
        reducao = ((tamanho_orig - tamanho_comp) / tamanho_orig) * 100
        print(f"Redução de tamanho: {reducao:.1f}%")
