# Importando módulos necessários
from trata_numero import trunca_decimal
import tabela


def inss(ano):
    """Recebe o ano com quatro dígitos, ex: 2022"""

    # Obtendo salário via teclado
    salario = float(input("Salário bruto: R$ "))
    valor_inss = 0.0
    faixa_inss = 0

    # Faixas de contribuição de tabelas com base nos valores oficiais
    # do INSS para os anos 2021 e 2022.
    valor = tabela.faixas_da_tabela(ano)

    # O percentual de cada alíquota é o mesmo para 2021 e 2022
    percentual_faixa1 = 0.075  # 7.5/100
    percentual_faixa2 = 0.09  # 9/100
    percentual_faixa3 = 0.12  # 12/100
    percentual_faixa4 = 0.14  # 14/100

    # Verificando cada faixa salarial
    faixa1 = salario <= valor['salario_minimo']
    faixa2 = (salario >= valor['min_faixa2']) and (salario <= valor['max_faixa2'])
    faixa3 = (salario >= valor['min_faixa3']) and (salario <= valor['max_faixa3'])
    faixa4 = (salario >= valor['min_faixa4']) and (salario <= valor['max_faixa4']) or (salario > valor['max_faixa4'])

    # Calculando as alíquotas para cada faixa, os cálculos seguem a metodologia
    # aplicada pela escola Avante RH (www.avanterh.net)
    # Tabela utilizada: https://www.avanterh.net/tabeladeinss2022
    aliq_faixa1 = valor['salario_minimo'] * percentual_faixa1
    aliq_faixa2 = ((valor['max_faixa2'] - valor['salario_minimo']) * percentual_faixa2) + aliq_faixa1
    aliq_faixa3 = ((valor['max_faixa3'] - valor['max_faixa2']) * percentual_faixa3) + aliq_faixa2
    aliq_faixa4 = ((valor['max_faixa4'] - valor['max_faixa3']) * percentual_faixa4) + aliq_faixa3

    # Com base no salário informado decidir qual bloco executar
    if faixa1:
        valor_inss = salario * percentual_faixa1
        faixa_inss = 1
    elif faixa2:
        valor_inss = ((salario - valor['salario_minimo']) * percentual_faixa2) + aliq_faixa1
        faixa_inss = 2
    elif faixa3:
        valor_inss = ((salario - valor['max_faixa2']) * percentual_faixa3) + aliq_faixa2
        faixa_inss = 3
    elif faixa4:
        # Verifica se o salário está acima do teto, então o valor a ser pago será
        # o limite para esta faixa. Do contrário, calcula o valor sobre o salário
        if salario > valor['max_faixa4']:
            valor_inss = aliq_faixa4
        else:
            valor_inss = ((salario - valor['max_faixa3']) * percentual_faixa4) + aliq_faixa3
        faixa_inss = 4
    
	# Pergunta se o usuário quer visualizar o resultado final com mais de duas casas decimais
    mudar_decimal = str(input("\nModificar quantidade de decimal no resultado? [S/N] ")).upper()
    if mudar_decimal == "S":
        valor = input("Quantidade de decimal desejado: [ex: 2, 3, 4] ")
        if valor.isdigit(): # se o valor digitado for numérico
            qtd_decimal = int(valor)
        else:
            print("\033[31mValor inválido. Considerando 2 casas decimais.\033[m")
            qtd_decimal = 2
    else:
        qtd_decimal = 2

    # Mostra o valor do INSS a ser pago com 2 casa decimais não arredondadas
    print("\nCom o salário bruto de \033[34mR$ {0:.2f}\033[m o colaborador {1} ".format(salario, "precisou" if ano == 2021 else "precisa"))
    print("pagar \033[34mR$ {0}\033[m de INSS, segundo a tabela de {1}.".format(trunca_decimal(valor_inss, qtd_decimal), ano))

    # Mostra a tabela de contribuição do ano escolhido realçando a faixa de
    # contribuição com base no salário informado.
    tabela.mostrar_faixa(ano, faixa_inss)
