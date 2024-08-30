# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json


def processar_faturamento(opcao, json_interno=None, arquivo_externo=None):
    if opcao == 1 and arquivo_externo:
        with open(arquivo_externo, 'r') as file:
            faturamento = json.load(file)["faturamento_diario"]
    elif opcao == 0 and json_interno:
        faturamento = json.loads(json_interno)["faturamento_diario"]
    else:
        print("Erro: Opção inválida ou JSON não fornecido.")
        return

    faturamento = [f for f in faturamento if f > 0]

    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


# EU NÃO SABIA SE QUERIAM COM JSON NO CORPO DO CÓDIGO OU EXTERNO, FIZ A OPÇÃO COMPLETA COM OS DOIS MODELOS

# *** USANDO JSON INTERNO COMO VARIÁVEL ***
json_interno = '''
{
    "faturamento_diario": [
        1200.50, 2300.75, 0.0, 4500.00, 3500.25, 0.0, 500.00, 7000.00, 0.0, 1000.00,
        11000.00, 2500.50, 800.00, 0.0, 3400.75, 9200.30, 0.0, 12500.50, 1100.00, 0.0,
        0.0, 1500.25, 4200.75, 8000.00, 0.0, 9700.00, 3600.00, 0.0, 2100.00, 7500.00
    ]
}
'''

processar_faturamento(0, json_interno=json_interno)

# *** USANDO JSON EXTERNO COMO VARIÁVEL (TIRAR '#' DA LINHA SEGUINTE) ***

#processar_faturamento(1, arquivo_externo='faturamento.json')