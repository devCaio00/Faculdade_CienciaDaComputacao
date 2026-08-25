# # 🕊️ Projeto LivyGod

**Instituição:** UNA – Contagem | Ciência da Computação  
**Professor:** Daniel Paiva  
**Equipe:** Caio Cesar, Marlon Bartoli, Rafael Ferreira

---

## 📖 Escopo e Objetivo
O **LivyGod** é um aplicativo focado em facilitar o acesso a orações, mensagens diárias e conteúdos religiosos. O sistema oferece uma experiência imersiva com recomendações integradas por Inteligência Artificial, hospedagem de lives (cultos, missas e encontros), podcasts, audiobooks de bem-estar e interação entre os usuários.

O público-alvo inclui pessoas que necessitam de facilidade de acesso a práticas religiosas e também aquelas que desejam aprofundar ou conhecer um ambiente de fé para adequar à sua vida pessoal.

---

## 📄 Finalidade dos Arquivos de Requisitos
Os documentos de engenharia de software e requisitos (como a *Matriz de Requisitos*, *Diagrama de Classes* e o *Plano de Qualidade*) disponibilizados neste repositório foram elaborados com as seguintes finalidades:

1. **Alinhamento e Base Arquitetural:** Servir como o "contrato" de desenvolvimento, garantindo que toda a equipe técnica tenha uma visão clara e unificada sobre o que deve ser construído, evitando desvios de escopo.
2. **Garantia de Acessibilidade:** Documentar formalmente a necessidade de interfaces adaptadas (modos "comum" e "facilitado"), garantindo que o público com pouca familiaridade tecnológica não seja excluído.
3. **Critérios de Aceite:** Definir métricas claras de sucesso para cada funcionalidade (como tempo de resposta de SMS, carregamento de vídeos e limite de mensagens), permitindo que os testes de qualidade (QA) sejam precisos e objetivos.
4. **Mapeamento de Dados:** Estruturar as entidades do sistema (Usuário, Religião, Grupos e Eventos) para orientar a criação do banco de dados relacional e a comunicação entre as classes da aplicação.

---

## ⚙️ Regras de Negócio

1. **Exclusividade de Vínculo Religioso:** O sistema permite a exibição de todas as religiões disponíveis no banco de dados, porém um usuário só pode ter o cadastro vinculado a **uma única religião**.
2. **Interação Restrita por Crença:** As recomendações de chat e networking no aplicativo são restritas a usuários que compartilham da mesma religião, fomentando um ambiente seguro e alinhado aos interesses de cada grupo.
3. **Gestão Descentralizada de Eventos:** Apenas *Grupos* criados na plataforma têm a permissão para hostear lives, criar encontros ou disponibilizar eventos de áudio. Os usuários atuam como participantes que reservam essas vagas.
4. **Treinamento Contínuo da IA:** As recomendações diárias de ritos ou versículos devem permitir o feedback direto do usuário para refinar as futuras indicações do algoritmo.

---

## 📋 Requisitos Funcionais (RF)

| ID | Descrição | Prioridade | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **RF#001** | Interface com modos "Comum" e "Facilitado". | ALTA | Usuários do modo facilitado devem acessar 80% das funções sem ajuda. Textos visíveis. |
| **RF#003** | Permitir que o usuário escolha sua religião. | ALTA | Mostrar base de dados; limitar a um vínculo por usuário. |
| **RF#006** | Cadastro de grupos para lives, áudios e eventos. | MÉDIA | Transmissões sem travamentos ou perda de dados. |
| **RF#007** | Permitir o cadastro/reserva de usuários em eventos. | BAIXA | Contabilizar vagas e exibir confirmação na agenda do perfil. |

---

## 🚀 Requisitos Não Funcionais (RNF)

| ID | Descrição | Prioridade | Critério de Aceite |
| :--- | :--- | :--- | :--- |
| **RNF#002** | Segurança de acesso via SMS/WhatsApp. | MÉDIA | Autenticação concluída em menos de 5 segundos. |
| **RNF#004** | Recomendação via IA no 1º acesso do dia. | MÉDIA | Exibição imediata na tela e botão de feedback habilitado. |
| **RNF#005** | Chat nativo entre usuários da mesma religião. | BAIXA | Envio e recebimento de mensagens em menos de 2 segundos. |

---

## 🛠️ Qualidade e Versionamento

* **Versionamento:** SemVer (Ex: v1.0.0). Utilização de Git e GitHub para controle.
* **Code Review:** Regras de *Branch Protection* ativadas na branch `main`. Todo Pull Request exige aprovação prévia de pares e testes automatizados passando.