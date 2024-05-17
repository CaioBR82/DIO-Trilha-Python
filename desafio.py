# Exercicio de Python... fiz um pouco maior para treinar
# Incluir algumas verifiações e mensagens de erro também.
# Classe cliente dissociada da classe conta para no futuro criar tabelas em banco de dados

class Cliente:
    def __init__(self, nome, cpf, endereco, cep):
        self.nome = nome
        self.cpf = self.formatar_cpf(cpf)
        self.endereco = endereco
        self.cep = self.formatar_cep(cep)

    def formatar_cpf(self, cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    def formatar_cep(self, cep):
        return f"{cep[:2]}.{cep[2:5]}-{cep[5:]}"


class ContaBancaria:
    LIMITE_SAQUE_DIARIO = 1500.00
    LIMITE_SAQUES_DIARIOS = 3

    def __init__(self, cliente, numero_banco, agencia, conta_corrente):
        self.cliente = cliente
        self.numero_banco = f"{numero_banco:03d}"
        self.agencia = agencia
        self.conta_corrente = conta_corrente
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0
        self.valor_saques_diarios = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R$ {valor:.2f}")
            return f"Depósito de R$ {valor:.2f} realizado com sucesso."
        else:
            return "O valor do depósito deve ser positivo."

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            return "O valor do saque deve ser um número."
        if self.saques_diarios >= self.LIMITE_SAQUES_DIARIOS:
            return "Limite diário de saques atingido."
        elif valor > 500:
            return "O valor máximo por saque é R$ 500,00."
        elif self.saldo < valor:
            return "Saldo insuficiente para realizar o saque."
        elif self.valor_saques_diarios + valor > self.LIMITE_SAQUE_DIARIO:
            return "Saque não autorizado, ultrapassa o seu limite diário de saques."
        else:
            self.saldo -= valor
            self.transacoes.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            self.valor_saques_diarios += valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."

    def extrato(self):
        if not self.transacoes:
            return "Não houve movimentação financeira."
        else:
            extrato = "\n".join(self.transacoes)
            extrato += f"\nSaldo atual: R$ {self.saldo:.2f}"
            return extrato

    def informacoes(self):
        return (f"Nome: {self.cliente.nome}\n"
                f"CPF: {self.cliente.cpf}\n"
                f"Endereço: {self.cliente.endereco}\n"
                f"CEP: {self.cliente.cep}\n"
                f"Banco: {self.numero_banco}\n"
                f"Agência: {self.agencia}\n"
                f"Conta Corrente: {self.conta_corrente}\n"
                f"Saldo: R$ {self.saldo:.2f}")


def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def validar_cep(cep):
    return len(cep) == 8 and cep.isdigit()


print("Bem vindo(a) ao Banco DIO.")

# Perguntando ao cliente se ele deseja abrir uma conta corrente, caso contrário, encerra o programa.
while True:
    abrir_conta = input("Deseja abrir uma conta corrente no Banco DIO? (S/N): ").strip().upper()
    if abrir_conta in ["S", "N"]:
        break
    print("Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não.")

if abrir_conta == "S":
    nome = input("Digite o seu nome: ")

    cpf = input("Digite o seu CPF (11 dígitos): ")
    while not validar_cpf(cpf):
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
        cpf = input("Digite o seu CPF (11 dígitos): ")

    endereco = input("Digite o seu endereço (até 90 caracteres): ")

    cep = input("Digite o seu CEP (8 dígitos): ")
    while not validar_cep(cep):
        print("CEP inválido. O CEP deve conter 8 dígitos numéricos.")
        cep = input("Digite o seu CEP (8 dígitos): ")

    # Criando o cliente com nome, cpf, endereço e cep. Poderia colocar rg, telefone, celular e outros campos
    cliente = Cliente(nome, cpf, endereco, cep)

    numero_banco = int(input("Digite o número do banco (3 dígitos): "))
    agencia = input("Digite o número da agência (até 6 dígitos): ")
    conta_corrente = input("Digite o número da conta corrente (até 9 dígitos): ")

    conta = ContaBancaria(cliente, numero_banco, agencia, conta_corrente)

    # Perguntando ao cliente se ele deseja realizar um depósito inicial, caso contrário encerra a operação
    realizar_deposito = input("Deseja realizar um depósito inicial? (S/N): ").strip().upper()
    if realizar_deposito == "S":
        valor_deposito = float(input("Digite o valor do depósito: "))
        mensagem = conta.depositar(valor_deposito)
        print(mensagem)
        print(f"O depósito no valor de R$ {valor_deposito:.2f} já está disponível para uso.")

        while True:
            realizar_transacao = input("Deseja realizar alguma transação? (S/N): ").strip().upper()
            if realizar_transacao == "S":
                tipo_transacao = input("Escolha a transação: Saque (S), Depósito (D), Extrato (E): ").strip().upper()
                if tipo_transacao == "S":
                    while True:
                        valor_saque = input("Digite o valor do saque: ")
                        try:
                            valor_saque = float(valor_saque)
                            break
                        except ValueError:
                            print("Valor inválido. O valor do saque deve ser um número.")

                    mensagem = conta.sacar(valor_saque)
                    print(mensagem)
                elif tipo_transacao == "D":
                    valor_deposito = float(input("Digite o valor do depósito: "))
                    mensagem = conta.depositar(valor_deposito)
                    print(mensagem)
                elif tipo_transacao == "E":
                    print(conta.extrato())
                else:
                    print("Opção inválida. Por favor, escolha Saque (S), Depósito (D) ou Extrato (E).")
            elif realizar_transacao == "N":
                print("Muito Obrigado por Utilizar os Serviços do Banco DIO.")
                break
            else:
                print("Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não.")
    else:
        print("\nMuito Obrigado por Utilizar os Serviços do Banco DIO.\n")
else:
    print("Obrigado! Até a próxima.")
