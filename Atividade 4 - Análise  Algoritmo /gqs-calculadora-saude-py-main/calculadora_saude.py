# calculadora_saude.py

def calcular_imc(peso, altura):
    # Bug 1: Multiplicação em vez de potenciação no cálculo do IMC
    ## Corrigido sinal de potenciação
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):#
    # Bug 2: Faixas de classificação sobrepostas e sem retorno para valores limites
    ## Corrigido Sobreposição de 18.5 para 18.6
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.6 and imc < 24.9:
        return "Peso normal"
    elif imc > 25.0 and imc < 29.9:
        return "Sobrepeso"
    elif imc > 30.0:
        return "Obesidade"

def calcular_agua_diaria(peso):
    # Bug 3: Fórmula dividindo o peso em vez de multiplicar por 35ml
    ## Corrigido Sinal de multiplicação
    litros = (peso * 35)
    return litros

def calcular_frequencia_cardiaca_maxima(idade):
    # Bug 4: Somando a idade em vez de subtrair de 220
    ## Corrigido sinal de subtração
    fc_max = 220 - idade
    return fc_max

def menu():
    print("\n" + "="*30)
    print("  SISTEMA DE SAÚDE E BEM-ESTAR  ")
    print("="*30)
    print("1. Calcular IMC")
    print("2. Calcular Recomendação de Água")
    print("3. Calcular Frequência Cardíaca Máxima")
    print("4. Sair")
    
    # Bug 5: input() retorna string, mas o código não trata a conversão no menu
    ## Corrigido tratativam de varíavel, não retornava o menu pois era um tipo diferente
    # de dado que entrava no input e que era solicitado pelo menu

    opcao = int(input("Escolha uma opção (1-4): "))
    return opcao

def main():
    while True:
        opcao = menu()
        
        # Bug 6: As comparações abaixo falharão devido ao tipo de dado da 'opcao'
        ##Corrigido no # Bug5, onde altero o tipo do dado para retornar corretamente
        if opcao == 1:
            peso = float(input("Digite seu peso (kg): "))
            altura = float(input("Digite sua altura (m): "))
            imc = calcular_imc(peso, altura)
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificar_imc(imc)}")
            
        elif opcao == 2:
            peso = float(input("Digite seu peso (kg): "))
            qtd_agua = calcular_agua_diaria(peso)
            print(f"Sua meta diária de água é: {qtd_agua:.2f} Litros")
            
        elif opcao == 3:
            idade = int(input("Digite sua idade: "))
            fc = calcular_frequencia_cardiaca_maxima(idade)
            print(f"Sua Frequência Cardíaca Máxima estimada é: {fc} bpm")
            
        elif opcao == 4:
            print("Encerrando o sistema...")
            # Bug 7: Ausência do break para sair do loop infinito
            ## Corrigido inserindo o break para quebrar o loop após mensagem de despedida.
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()