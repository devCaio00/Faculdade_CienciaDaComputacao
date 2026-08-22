import re

def analisar(entrada):
    if entrada is None:
        return False
    
    # Remove tudo que não for letra ou número e converte para minúsculas
    limpa = re.sub(r'[^a-zA-Z0-9]', '', entrada).lower()
    
    # Inverte a string usando fatiamento (slicing)
    invertida = limpa[::-1]
    
    return limpa == invertida

if __name__ == "__main__":
    texto1 = "A sacada da casa de cadasa"
    texto2 = "Socorram-me, subi no ônibus em Marrocos"

    print(f"Teste 1: {analisar(texto1)}")
    print(f"Teste 2: {analisar(texto2)}")