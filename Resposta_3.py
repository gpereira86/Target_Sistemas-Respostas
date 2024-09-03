# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json


def processar_faturamento(arquivo_externo):
    try:
        with open(arquivo_externo, 'r') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar o JSON.")
        return

    faturamento = [item["valor"] for item in dados if item["valor"] > 0]


    if not faturamento:
        print("Nenhum valor de faturamento disponível para processamento.")
        return

    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${ maior_valor:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

processar_faturamento('dados.json')
