def trunca_decimal(valor, decimal):
    """
    Recebe o valor do INSS a ser pago e a quantidade de casas decimais desejada,
    retorna o mesmo valor truncado com 2 casas decimais não arredondadas.
    """
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))

# Obtendo salário via teclado para cálculo
salario = float(input("Informe o Salário: R$ "))
valor_inss = 0.0

# Verificando cada faixa salarial
faixa1 = salario <= 1212.0
faixa2 = (salario >= 1212.01) and (salario <= 2427.35)
faixa3 = (salario >= 2427.36) and (salario <= 3641.03)
faixa4 = (salario >= 3641.04) and (salario <= 7087.22) or (salario > 7087.22)

# Calculando as alíquotas para cada faixa, os cálculos seguem a metodologia
# aplicada pela escola Avante RH (www.avanterh.net)
# Tabela utilizada: https://www.avanterh.net/tabeladeinss2022
aliq_faixa1 = 1212.0 * 7.5 / 100
aliq_faixa2 = ((2427.35 - 1212.00) * 9 / 100) + aliq_faixa1
aliq_faixa3 = ((3641.03 - 2427.35) * 12 / 100) + aliq_faixa2
aliq_faixa4 = ((7087.22 - 3641.03) * 14 / 100) + aliq_faixa3

# Com base no salário informado decidir qual bloco executar
if faixa1:
    valor_inss = salario * 7.5 / 100
elif faixa2:
    valor_inss = ((salario - 1212.00) * 9 / 100) + aliq_faixa1
elif faixa3:
    valor_inss = ((salario - 2427.35) * 12 / 100) + aliq_faixa2
elif faixa4:
    # Verifica se o salário está acima do teto, então o valor a ser pago será
    # o limite para esta faixa. Do contrário, calcula o valor sobre o salário
    if salario > 7087.22:
        valor_inss = aliq_faixa4
    else:
        valor_inss = ((salario - 3641.03) * 14 / 100) + aliq_faixa3

# Mostra o valor do INSS a ser pago com 2 casa decimais não arredondadas
print("INSS: {0}".format(trunca_decimal(valor_inss, 2)))
