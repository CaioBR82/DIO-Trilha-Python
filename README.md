# Projeto Banco DIO

**Este projeto em Python simula operações bancárias básicas, permitindo criar contas, realizar depósitos, saques e consultar extratos. O sistema é dividido em duas classes principais: Cliente e ContaBancaria.**

### Classes Criadas
  - Classe Cliente
      - Cliente: Representa um cliente com nome, CPF, endereço e CEP. CPF e CEP são formatados automaticamente.
  -Classe ContaBancaria
      - ContaBancaria: Representa uma conta bancária associada a um cliente, com número do banco, agência, conta corrente e saldo.

### Constantes:
  - LIMITE_SAQUE_DIARIO: Limite de valor para saques diários (R$ 1500,00).
  - LIMITE_SAQUES_DIARIOS: Limite de quantidade de saques diários (3).

### Métodos criados :
  - formatar_cpf(cpf): Formata o CPF.
  - formatar_cep(cep): Formata o CEP.
  - depositar(valor): Adiciona um valor ao saldo, se for positivo.
  - sacar(valor): Realiza um saque, respeitando os limites diários e o saldo disponível.
  - extrato(): Retorna o extrato das transações.
    
### informacoes(): Retorna as informações da conta.
**Validações**
  - CPF: Deve conter 11 dígitos numéricos.
  - CEP: Deve conter 8 dígitos numéricos.

**Funcionalidades**
  - Criação de conta com validações de CPF e CEP.
  - Depósito inicial opcional.
  - Realização de transações: saques, depósitos e consulta de extratos.
  - imitações e mensagens de erro claras para operações inválidas.
