# Análise de Inversor de Texto

O DesafioLogica é um código em Python, que analisa uma entrada e retorna o inverso da entrada inicial, ou seja, comparando a frase "Socorram-me, subi no ônibus em Marrocos", vamos ter um retorno True, pois o inverso desta frase é igual a entrada inicial "Socorram-me, subi no ônibus em Marrocos"

# Como funciona?

O código funciona criando um método com 2 comandos:
- Remove tudo que não for letra ou número e converte para minúsculas
- Inverte a frase usando fatiamento (slicing)

```python
def analisar(entrada):
    if entrada is None:
        return False
    
    # Remove tudo que não for letra ou número e converte para minúsculas
    limpa = re.sub(r'[^a-zA-Z0-9]', '', entrada).lower()
    
    # Inverte a string usando fatiamento (slicing)
    invertida = limpa[::-1]
    
    return limpa == invertida
```

Neste metodo, os comandos comparam as frases invertidas e retornam se o inverso é igual a entrada inicial.
- "Limpa" é a frase sem simbolos ou números e com letras minusculas
- "Invertida" é a frase invertida que já foi limpa pelo comando anterior.

## Como executar?

- Este código pode ser executado de forma local ou via Codespace Github.

**Acessando o código via CodeSpace Github**
1. Acesse o GitHub.
2. Caso não tenha criado um CodeSpace, crie um CodeSpace e faça link com um repositório de sua conta.
3. Entre no link [DesafioLogica - Github](https://github.com/danhpaiva/gqs-algoritmo-01-py)
4. Clique em "Fork" no canto superior direito e selecione o CodeSpace/Repositório criado na sua conta.
5. Abra o CodeSpace do repositório
6. Ao Abrir o CodeSpace do repositório, você verá o arquivo .py, que é o código a ser executado.

## Como utilizar o código

1. Acesse o arquivo DesafioLogica.py
2. Rolando o código para baixo, localize o seguinte:

```python
if __name__ == "__main__":
    texto1 = "A sacada da casa de cadasa"
    texto2 = "Socorram-me, subi no ônibus em Marrocos"
```

3. As variáveis **texto1** e **texto2** são as entradas que serão analisadas se, o inverso da entrada inicial é igual a entrada inicial.
4. Altere a frase que está entre aspas ("") da forma que achar melhor, sugiro "Amor Roma" para um valor verdadeiro, pois o contrário fica "Amor Roma".
5. Caso seja necessário, você pode adicionar mais testes para rodar ao mesmo tempo, para fazer isto, basta criar uma nova variável seguindo a mesma formatação anterior, exemplo: 

```python
if __name__ == "__main__":
    texto1 = "A sacada da casa de cadasa"
    texto2 = "Socorram-me, subi no ônibus em Marrocos"
    texto3 = "Luz azul"

    print(f"Teste 1: {analisar(texto1)}")
    print(f"Teste 2: {analisar(texto2)}")
    print(f"Teste 3: {analisar(texto3)}")
```
**Exemplo de Saída do Código**

```Saída
/DesafioLogica.py
Teste 1: False
Teste 2: True
Teste 3: True
```
## Qual o papel do método Main neste código?

O Método Main funciona para setorizar a análise atual, por exemplo, se o arquivo estiver sendo rodado diretamente, o python entende que você quer os testes atuais descritos neste algoritmo, caso o algoritmo fosse solicitado por outro arquivo por exemplo para utilizar o método em outro algoritmo, ele não rodaria os testes neste algoritmo, pois ele não faz parte do Main.

## Método Analisar e ReplaceAll

- O Método Analisar serve para previamente retornar se, caso a entrada seja Nula, o algoritmo retorna como False as respostas.
- O Método replaceAll vem de substitute (substituir), ele serve para fazer a limpeza das entradas e garantir que todas estejam sem números, simbolos ou espaços e somente com letras minúsculas.
- StringBuilder é quando ocorre a conversão de uma String imutável para uma String que pode ser alterada, ou seja, apagar, reescrever, inverter e colar textos à vontade, e tudo isso acontece no mesmo "quadro", aproveitando o mesmo espaço de memória, sem precisar criar objetos novos o tempo todo.

# Sobre o Autor

- O Autor que criou e documentou este Markdown a partir do Fork foi Caio Cesar (devCaio00), estudante de Ciência da Computação.
Esta atividade foi realizada na matéria de Garantia de Qualidade de Software no dia 17/08/2026, estudo de linguagem Markdown e Análise de código.

- LinkedIn: [Caio Cesar](https://www.linkedin.com/in/caiioccesar/)
- Github: [Dev Caio](https://github.com/devCaio00)






