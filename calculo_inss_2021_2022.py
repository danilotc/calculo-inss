# Importando módulos necessários
from trata_numero import trunca_decimal
import tabela


def inss(ano):
    """Recebe o ano com quatro dígitos, ex: 2022"""

    # Obtendo salário via teclado
    salario = float(input("Salário bruto: R$ "))
    valor_inss = 0.0
    faixa_inss = 0

    # Setando as faixas de contribuição com base nos valores oficiais
    # do INSS para os anos 2021 e 2022.
    if ano == 2022:
        salario_minimo = 1212.00
        # limite da faixa 2
        min_faixa2 = 1212.01
        max_faixa2 = 2427.35
        # limite da faixa 3
        min_faixa3 = 2427.36
        max_faixa3 = 3641.03
        # limite da faixa 4
        min_faixa4 = 3641.04
        max_faixa4 = 7087.22
    elif ano == 2021:
        salario_minimo = 1100.00
        # limite da faixa 2
        min_faixa2 = 1100.01
        max_faixa2 = 2203.48
        # limite da faixa 3
        min_faixa3 = 2203.49
        max_faixa3 = 3305.22
        # limite da faixa 4
        min_faixa4 = 3305.23
        max_faixa4 = 6433.57

    # O percentual de cada alíquota é o mesmo para 2021 e 2022
    percentual_faixa1 = 0.075  # 7.5/100
    percentual_faixa2 = 0.09  # 9/100
    percentual_faixa3 = 0.12  # 12/100
    percentual_faixa4 = 0.14  # 14/100

    # Verificando cada faixa salarial
    faixa1 = salario <= salario_minimo
    faixa2 = (salario >= min_faixa2) and (salario <= max_faixa2)
    faixa3 = (salario >= min_faixa3) and (salario <= max_faixa3)
    faixa4 = (salario >= min_faixa4) and (salario <= max_faixa4) or (salario > max_faixa4)

    # Calculando as alíquotas para cada faixa, os cálculos seguem a metodologia
    # aplicada pela escola Avante RH (www.avanterh.net)
    # Tabela utilizada: https://www.avanterh.net/tabeladeinss2022
    aliq_faixa1 = salario_minimo * percentual_faixa1
    aliq_faixa2 = ((max_faixa2 - salario_minimo) * percentual_faixa2) + aliq_faixa1
    aliq_faixa3 = ((max_faixa3 - max_faixa2) * percentual_faixa3) + aliq_faixa2
    aliq_faixa4 = ((max_faixa4 - max_faixa3) * percentual_faixa4) + aliq_faixa3

    # Com base no salário informado decidir qual bloco executar
    if faixa1:
        valor_inss = salario * percentual_faixa1
        faixa_inss = 1
    elif faixa2:
        valor_inss = ((salario - salario_minimo) * percentual_faixa2) + aliq_faixa1
        faixa_inss = 2
    elif faixa3:
        valor_inss = ((salario - max_faixa2) * percentual_faixa3) + aliq_faixa2
        faixa_inss = 3
    elif faixa4:
        # Verifica se o salário está acima do teto, então o valor a ser pago será
        # o limite para esta faixa. Do contrário, calcula o valor sobre o salário
        if salario > max_faixa4:
            valor_inss = aliq_faixa4
        else:
            valor_inss = ((salario - max_faixa3) * percentual_faixa4) + aliq_faixa3
        faixa_inss = 4

    # Mostra o valor do INSS a ser pago com 2 casa decimais não arredondadas
    print("\nCom o salário bruto de \033[34mR$ {0:.2f}\033[m o colaborador {1} ".format(salario, "precisou" if ano == 2021 else "precisa"))
    print("pagar \033[34mR$ {1:.2f}\033[m de INSS, segundo a tabela de {0}.".format(ano, trunca_decimal(valor_inss, 2)))

    # Mostra a tabela de contribuição do ano escolhido realçando a faixa de
    # contribuição com base no salário informado.
    tabela.mostrar(ano, faixa_inss)
