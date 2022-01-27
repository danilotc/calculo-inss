# Cálculo do INSS 2021 e 2022

Este documento tem por finalidade esclarecer um questionamento a certa do valor a ser descontado para o INSS na folha de pagamento  para o ano 2021  pela empresa onde prestamos serviço como recepcionista. Embora o objetivo seja calcular valores para o INSS referentes ao ano 2021, o mesmo cálculo se aplica com a tabela vigente de 2022, visto que as alíquotas permanecem as mesmas.

Com base na tabela oficial de cálculo dos valores a serem descontados para o serviço do Instituto Nacional do Seguro Social (INSS) desenvolvi um algoritmo que irá receber o **ano** e o **salário base** a ser calculado e retorna o valor a ser descontado na folha de pagamento.

## Como calcular o valor a ser pago usando seu algoritmo?

Ao executar o algoritmo você precisará informar os dois valores necessários, **ano** e **salário base**, como mostra o exemplo abaixo considerando a tabela vigente de 2022 e um salário de 6 mil reais.

![Solicitação](https://raw.githubusercontent.com/danilotc/assets/master/solicitacao.png)

Em seguida, basta analisar o resultado que será impresso na tela, a tabela irá indicar a faixa em que o salário informado se enquadra, logo a porcentagem dessa faixa é a que está sendo calculada, como no exemplo a seguir.

![Resultado texto](https://raw.githubusercontent.com/danilotc/assets/master/resultado1.png)
![Resultado tabela](https://raw.githubusercontent.com/danilotc/assets/master/resultado2.png)

Este é o resultado do algoritmo funcionando. A fórmula utilizada para este cálculo específico é a seguinte:

(6.000,00 - 3.641,04) x 14 / 100 + 345,92

## O "x" da questão

Considerando que você realizou os cálculos disponíveis no arquivo utilizando a calculadora e  validou cada resultado, gostaria de entrar no X da questão.

Como mencionei no início deste documento, o principal objetivo deste estudo foi tentar descobrir se o valor que estava sendo descontado em 2021 para o INSS em nossa folha de pagamento estava correto, isso foi questionado por alguns colegas. A fim de esclarecer essa dúvida, uni meus estudos de programação com essa investigação e obtive o seguinte resultado.

Considerando minha folha de pagamento do ano 2021, o desconto indicado foi de R$  88,06 que corresponde a 9% do salário base. Para realizar esse cálculo considerei meu salário base de R$ 1.161,78 e a resposta do algoritmo foi essa.

![Solicitação](https://raw.githubusercontent.com/danilotc/assets/master/solicitacao2.png)<br><br>
![Resultado 3](https://raw.githubusercontent.com/danilotc/assets/master/resultado3.png)<br>
![Resultado 4](https://raw.githubusercontent.com/danilotc/assets/master/resultado4.png)

O resultado acima é a resposta do algoritmo que escrevi após estudar o cálculo que é utilizado para desconto do valor a ser pago ao INSS. Logo, como podemos observar, o valor descontado e a faixa em que o valor base se enquadra mostram que o desconto  em nossa folha de pagamento estava correto.

Com isso, posso afirmar que não estava sendo descontado 7,5%, mas 9% visto que o salário base ultrapassa o salário mínimo do ano em questão.

Para testar o funcionamento  deste algoritmo clique na imagem abaixo.  Lembre-se apenas de utilizar `(.)` no lugar de `(,)` para separar os decimais.

<p align="center" size="10px">
<a href="https://replit.com/@danilocastro5/calculoinss" target="_black"><img src="https://blog.replit.com/images/logo.png" width="200px"></a>
</p>


## Tabela de cálculo utilizada

A tabela abaixo é a junção de duas fontes distintas, isto porque as duas primeiras colunas são oficiais do [INSS](https://www.gov.br/inss/pt-br/saiba-mais/seus-direitos-e-deveres/calculo-da-guia-da-previdencia-social-gps/tabela-de-contribuicao-mensal) enquanto a última se refere a um método utilizado pela escola [Avante RH](https://www.avanterh.net/tabeladeinss2022) para calcular o valor do INSS a ser pago.


### 2022

| Salário de Contribuição (R$)     | Alíquota | "Valor a agregar" |
|----------------------------------|:--------:|----------:|
| Até R$ 1.121,00                  | 7,5%     | -         |
| De R\$ 1.212,01 a R\$ 2.427,35   | 9%       | R$ 90,90  |
| De R\$ 2.427,36 a R\$ 3.641,03   | 12%      | R$ 200,28 |
| De R\$ 3.641,04 a R\$ 7.087,22   | 14%      | R$ 345,92 |


### 2021

| Salário de Contribuição (R$)     | Alíquota | "Valor a agregar" |
|----------------------------------|:--------:|----------:|
| Até R$ 1.100,00                  | 7,5%     | -         |
| De R\$ 1.100,01 a R\$ 2.203,48   | 9%       | R$ 82,50  |
| De R\$ 2.203,49 a R\$ 3.305,22   | 12%      | R$ 181,81 |
| De R\$ 3.305,23 a R\$ 6.433,57   | 14%      | R$ 314,01 |


Para melhor compreensão do cálculo utilizando esta terceira coluna, caso ainda não conheça, recomendo assistir este [este vídeo](https://youtu.be/y0Ko6S_L4Vc)  com o **Prof. Rafael Lopes da Avante RH** explicando tudo com riqueza de detalhes.

## Detalhes técnicos

Alguns métodos utilizam diferentes formas de calcular e exibir o resultado, por exemplo, mostrar o resultado com 3 casas decimais, ou 2, ou ainda sempre arredondar o valor decimal. Pensando nisso, decidi manter o resultado com apenas duas casas decimais sem arredondar implementando a seguinte função. 

```python
def trunca_decimal(valor, decimal):
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))
```

Além disso, é importante observar as faixas setadas antes de sua utilização. Gostaria de realçar a quarta faixa. Com resultado *boleano* o trecho avalia se o salário está entre o valor mínimo e máximo da faixa 4 ou se é maior que ela. Em ambos os casos será aplicado alíquota de 14%.


```python
faixa4 = (salario >= min_faixa4) and (salario <= max_faixa4) or (salario > max_faixa4)
```

O bloco que irá calcular alíquota de 14% independente se está entre os valores da faixa ou acima do teto é este.

```python
# código oculto
elif faixa4:
    if salario > max_faixa4:
        valor_inss = aliq_faixa4
    else:
        valor_inss = ((salario - max_faixa3) * percentua_faixa4) + aliq_faixa3
# código oculto
```

## Objetivo final

Pesquisei para tentar entender um questionamento sobre a empresa que nos contratou, pois acreditou-se que a mesma estava descontando 7,5% e colocando na folha de pagamento 9%. Contudo, considero esta investigação concluída.

Caso queira ver mais detalhes sobre essa investigação, sugiro a leitura [deste documento](https://drive.google.com/file/d/1TzN6WKTK1IrV30nFGtLCZtkr8N8nXOnk/view) com algumas fórmulas aplicadas ao algoritmo para validação do mesmo.
