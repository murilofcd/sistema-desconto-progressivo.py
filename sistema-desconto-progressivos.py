# ==============================================================================
# PROGRAMA: Sistema de Desconto Progressivo
# ALUNO: Murilo Figueiredo Cordesco Domingues
# DISCIPLINA: Desenvolvimento de Sistemas I - Agenda 6
# ==============================================================================


def calcular_desconto_progressivo():
  """Solicita o valor total da compra, calcula o desconto progressivo

  e exibe o valor economizado e o total final a ser pago.
  """
  print("=" * 60)
  print("       SISTEMA DE DESCONTO PROGRESSIVO - LOJA ONLINE       ")
  print("=" * 60)

  try:
    # Entrada de dados: solicita o valor total da compra ao usuario
    valor_compra = float(
        input("\nDigite o valor total da compra (R$): ").replace(",", ".")
    )

    # Validacao para evitar valores negativos ou zerados
    if valor_compra <= 0:
      print("\n[ERRO] O valor da compra deve ser maior que zero!")
      return

    # Estrutura condicional para definicao do percentual de desconto
    if valor_compra < 200.00:
      percentual_desconto = 5  # 5% de desconto para compras abaixo de R$ 200
    elif valor_compra < 300.00:
      percentual_desconto = (
          10  # 10% para compras entre R$ 200.00 e R$ 299.99
      )
    else:
      percentual_desconto = (
          15  # 15% para compras maiores ou iguais a R$ 300.00
      )

    # Processamento: Calculo do valor do desconto e total a pagar
    valor_desconto = valor_compra * (percentual_desconto / 100)
    valor_final = valor_compra - valor_desconto

    # Saida de dados: Exibicao dos resultados formatados
    print("\n" + "-" * 40)
    print("             RESUMO DA COMPRA             ")
    print("-" * 40)
    print(f"Valor original da compra : R$ {valor_compra:.2f}")
    print(f"Percentual de desconto    : {percentual_desconto}%")
    print(f"Valor do desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Valor total a ser pago    : R$ {valor_final:.2f}")
    print("-" * 40)

  except ValueError:
    # Tratamento de erro caso o usuario digite texto em vez de um numero
    print(
        "\n[ERRO] Entrada invalida! Por favor, insira um numero valido para"
        " o valor."
    )
