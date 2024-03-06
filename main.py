import pandas as pd

# Função para inserir transação na planilha
def inserir_transacao(planilha, data, descricao, conta, valor):
    planilha = planilha.append({'Data': data, 'Descrição': descricao, 'Conta': conta, 'Valor': valor}, ignore_index=True)
    return planilha

# Função para calcular saldo de caixa
def calcular_saldo(planilha):
    saldo = planilha['Valor'].sum()
    return saldo

# Função principal
def main():
    # Criar uma planilha vazia
    planilha = pd.DataFrame(columns=['Data', 'Descrição', 'Conta', 'Valor'])

    while True:
        print("\nOpções:")
        print("1. Inserir transação")
        print("2. Ver saldo de caixa")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            data = input("Data da transação (DD/MM/AAAA): ")
            descricao = input("Descrição da transação: ")
            conta = input("Conta bancária: ")
            valor = float(input("Valor da transação: "))
            tipo_transacao = input("Tipo de transação (entrada/saída): ").lower()

            if tipo_transacao == 'entrada':
                valor *= 1  # Manter o valor positivo para entrada
            elif tipo_transacao == 'saída':
                valor *= -1  # Transformar o valor em negativo para saída
            else:
                print("Tipo de transação inválido.")
                continue

            planilha = inserir_transacao(planilha, data, descricao, conta, valor)
            print("Transação inserida com sucesso.")

        elif opcao == '2':
            saldo = calcular_saldo(planilha)
            print(f"Saldo de caixa atual: {saldo}")

        elif opcao == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    # Salvar a planilha em um arquivo CSV
    planilha.to_excel('fluxo_de_caixa.xlsx', index=False)

if __name__ == "__main__":
    main()
