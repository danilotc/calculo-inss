# Cálculo INSS

Criado com objetivo de compreender o cálculo para desconto do [INSS - Instituto Nacional do Seguro Social](https://www.gov.br/inss/pt-br) para trabalhadores com carteira assinada, este algoritmo calcula o valor a ser pago para o INSS com base no salário bruto.

Execute o programa [Calculo_INSS](https://replit.com/@danilocastro5/calculoinss#calculo_inss_2022.py)

## Tabela de cálculo utilizada

A tabela abaixo é a junção de duas fontes distintas, isto porque as duas primeiras colunas são oficiais do [INSS](https://www.gov.br/inss/pt-br/saiba-mais/seus-direitos-e-deveres/calculo-da-guia-da-previdencia-social-gps/tabela-de-contribuicao-mensal) enquanto a última se refere a um método utilizado pela escola [Avante RH](https://www.avanterh.net/tabeladeinss2022) para calcular o valor do INSS a ser pago.

| Salário de Contribuição (R$)     | Alíquota | "Valor a agregar" |
|----------------------------------|:--------:|----------:|
| Até R$ 1.121,00                  | 7,5%     | -         |
| De R\$ 1.212,01 a R\$ 2.427,35   | 9%       | R$ 90,90  |
| De R\$ 2.427,36 a R\$ 3.641,03   | 12%      | R$ 200,28 |
| De R\$ 3.641,04 a R\$ 7.087,22   | 14%      | R$ 345,92 |

O trecho que calcula os valores da tabela acima é este, ou seja, para cada alíquota calculada, exceto a de 7,5%, será somado o valor das anteriores já faturadas.

```python
aliq_faixa1 = 1212.0 * 7.5 / 100
aliq_faixa2 = ((2427.35 - 1212.00) * 9 / 100) + aliq_faixa1
aliq_faixa3 = ((3641.03 - 2427.35) * 12 / 100) + aliq_faixa2
aliq_faixa4 = ((7087.22 - 3641.03) * 14 / 100) + aliq_faixa3
```
Para melhor compreensão do cálculo utilizando esta terceira coluna, caso ainda não saiba, recomendo que veja [este vídeo](https://youtu.be/y0Ko6S_L4Vc)  com o **Prof. Rafael Lopes da Avante RH** explicando tudo com riqueza de detalhes.

## Detalhes técnicos

Alguns métodos utilizam diferentes formas de calcular e exibir o resultado, por exemplo, mostrar o resultado com 3 casas decimais, ou 2, ou ainda sempre arredondar o valor decimal etc. Pensando nisso, decidi manter o resultado com apenas duas casas decimais sem arredondamentos através da seguinte função. 

```python
def trunca_decimal(valor, decimal):
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))
```

Além disso, é importante observar as faixas setadas antes de sua utilização. Gostaria de realçar a quarta faixa. Com resultado *boleano* o trecho avalia se o salário está entre (3.641,04 e 7.087,22) ou se é maior que o teto (salario > 7.087,22). Em ambos os casos será aplicado alíquota de 14%.

```python
faixa4 = (salario >= 3641.04) and (salario <= 7087.22) or (salario > 7087.22)
```

E por fim, o bloco que irá executar o cálculo de 14% é este.

```python
# código oculto
elif faixa4:
    if salario > 7087.22:
        valor_inss = aliq_faixa4
    else:
        valor_inss = ((salario - 3641.03) * 14 / 100) + aliq_faixa3
# código oculto
```

## Objetivo final

Feita essa explicação, continuarei estudando para tentar resolver um problema identificado na empresa que nos contratou, pois parece que ela está descontando 7,5% e colocando na folha de pagamento 9%. Seguirei com esse estudo a fim de concluir essa investigação.
