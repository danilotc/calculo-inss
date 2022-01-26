def trunca_decimal(valor, decimal):
    """
    Recebe o valor do INSS a ser pago e a quantidade de casas decimais desejada,
    retorna o mesmo valor truncado com 2 casas decimais não arredondadas.
    """
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))


salario = float(input("Informe o Salário: R$ "))
valor_inss = 0.0

salario_minimo = 1212.00
# limites da faixa 2
min_faixa2 = 1212.01
max_faixa2 = 2427.35
# limites da faixa 3
min_faixa3 = 2427.36
max_faixa3 = 3641.03
# limites da faixa 4
min_faixa4 = 3641.04
max_faixa4 = 7087.22

percentual_faixa1 = 0.075  # 7.5/100
percentual_faixa2 = 0.09   # 9/100
percentual_faixa3 = 0.12   # 12/100
percentual_faixa4 = 0.14   # 14/100

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
elif faixa2:
    valor_inss = ((salario - salario_minimo) * percentual_faixa2) + aliq_faixa1
elif faixa3:
    valor_inss = ((salario - min_faixa3) * percentual_faixa3) + aliq_faixa2
elif faixa4:
    # Verifica se o salário está acima do teto, então o valor a ser pago será
    # o limite para esta faixa. Do contrário, calcula o valor sobre o salário
    if salario > max_faixa4:
        valor_inss = aliq_faixa4
    else:
        valor_inss = ((salario - min_faixa4) * percentual_faixa4) + aliq_faixa3

# Mostra o valor do INSS a ser pago com 2 casa decimais não arredondadas
print("INSS: {0}".format(trunca_decimal(valor_inss, 2)))
