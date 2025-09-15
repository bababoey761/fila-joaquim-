# Fila com priorídade (Joaquim Paulo Vieira de Melo)



Este projeto foi desenvolvido para demonstrar a evolução de um sistema de gerenciamento de filas com prioridade, utilizando a linguagem Python. O objetivo é simular o atendimento em locais onde pessoas com necessidades especiais ou idosos têm prioridade, seguindo as normas de acessibilidade e atendimento preferencial.

---

## Etapas do Projeto

### **1. [`fila_1.py`](./fila_1.py) — Identificação de Prioridade**

- **Objetivo:** Identificar se uma pessoa é prioritária ou não.
- **Funcionamento:**  
  - Solicita ao usuário o nome, idade, se é gestante e se é pessoa com deficiência (PCD).
  - Se a idade for maior ou igual a 60 anos, ou se for gestante, ou PCD, classifica como "PRIORITÁRIO".
  - Caso contrário, classifica como "NORMAL".
- **Resumo:**  
  Primeira abordagem, sem uso de filas, apenas classificação individual.

---

### **2. [`fila_2.py`](./fila_2.py) — Estruturação da Fila**

- **Objetivo:** Criar uma fila que armazena várias pessoas e identifica prioridades.
- **Funcionamento:**  
  - Permite adicionar várias pessoas à fila, coletando nome, idade e necessidades especiais.
  - Cada pessoa é registrada como prioritária ou não, de acordo com os critérios.
  - A fila é ordenada automaticamente, colocando prioritários na frente, mas mantendo a ordem de chegada entre pessoas do mesmo grupo.
  - Funções para mostrar a fila e atender (remover) o próximo da fila.
- **Resumo:**  
  Introduz a lógica de fila e prioridade, mas sem menu interativo.

---

### **3. [`fila_3.py`](./fila_3.py) — Menu Interativo**

- **Objetivo:** Facilitar a interação do usuário com o sistema.
- **Funcionamento:**  
  - Adiciona um menu com opções para adicionar pessoas, mostrar a fila, atender o próximo e sair.
  - Permite o uso contínuo do sistema até o usuário optar por sair.
  - Mostra a quantidade de prioritários e não prioritários na fila.
- **Resumo:**  
  Torna o sistema mais amigável e prático para o usuário.

---

### **4. [`fila_4.py`](./fila_4.py) — Estatísticas e Funcionalidades Avançadas**
- **Nota:** Em vez de separar, organizei todos em um fila colocar os priorítarios como priorirade
- **Objetivo:** Aprimorar o sistema com estatísticas e controle de atendimento.
- **Funcionamento:**  
  - Mantém o controle de quantas pessoas já foram atendidas.
  - Mostra a porcentagem de prioritários na fila e de pessoas já atendidas.
  - Adiciona um tempo de espera ao mostrar a fila, simulando processamento.
  - Inclui opção de debug para visualizar a estrutura interna da fila.
- **Resumo:**  
  Sistema completo, com informações gerenciais e experiência mais próxima de um sistema real.
