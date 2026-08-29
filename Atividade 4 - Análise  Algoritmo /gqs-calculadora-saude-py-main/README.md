# Calculadora de Saúde
## Identificando e Analisando o algoritmo

Este algoritmo é uma calculadora que permite calcular o IMC, a quantidade de agua necessária por kg e a frequência cardiaca máxima (BPM) através de um menu no terminal.

--

# Bugs identificados no algoritmo

| Bug encontrado | O que acontece | Solução |
|---|---|---|
| **Bug 1:** Multiplicação em vez de potenciação no cálculo do IMC | Retornando valor incorreto para o IMC. | Trocar o sinal matemático para potenciação (`**`). |
| **Bug 2:** Faixas de classificação sobrepostas e sem retorno para limites | Conflito entre a classificação ou ausência de retorno em valores exatos (ex: 18.5). | Corrigido sobreposição de 18.5 para 18.6 e ajustado os operadores lógicos. |
| **Bug 3:** Fórmula dividindo o peso em vez de multiplicar por 35ml | O cálculo da água diária resulta em um valor completamente irreal. | Corrigido alterando o sinal de divisão para sinal de multiplicação (`*`). |
| **Bug 4:** Somando a idade em vez de subtrair de 220 | O cálculo da frequência cardíaca máxima fica acima do esperado/equivocado. | Corrigido trocando o sinal de adição pelo sinal de subtração (`-`). |
| **Bug 5:** `input()` retorna string, mas o código não trata a conversão | O tipo de dado lido não batia com o tipo esperado pelo menu (número). | Corrigida tratativa da variável envolvendo o `input()` com a função `int()`. |
| **Bug 6:** As comparações falham devido ao tipo de dado da 'opcao' | O programa caía na mensagem "Opção inválida" para qualquer escolha. | Corrigido em conjunto com o Bug 5, onde a conversão para inteiro garantiu a leitura correta dos `ifs`. |
| **Bug 7:** Ausência do `break` para sair do loop infinito | O sistema não encerrava ao escolher a opção 4, repetindo o menu para sempre. | Inserido o comando `break` para quebrar o loop logo após a mensagem de despedida. |

A Tabela foi construída com o auxílio de IA.

## Como Executar o Projeto

1. **Verifique o Python:** Abra o terminal e digite `python --version` para garantir que a linguagem está instalada.
2. **Salve o código:** Guarde o código já corrigido em um arquivo chamado `calculadora_saude.py`.
3. **Navegue até a pasta:** Abra o Terminal (ou CMD) e vá até a pasta onde salvou o arquivo usando o comando `cd` (ex: `cd ~/Documentos/Projetos`).
4. **Rode o programa:** Execute o comando `python calculadora_saude.py` (use `python3` se estiver no Mac/Linux).
5. **Navegue pelos menus**: O algoritmo funciona por terminal, então basta digitar o menu que deseja e inserir as informações necessárias, sequencialmente o programa irá retornar o resultado com as informações inseridas.
