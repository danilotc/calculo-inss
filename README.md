# Cálculo do INSS 2021 e 2022

Com base na tabela oficial de cálculo dos valores a serem descontados para o serviço do Instituto Nacional do Seguro Social (INSS) desenvolvi este programa que irá receber dois valores: **ano** e **salário base** retornando o valor que deverá ser descontado na folha de pagamento para o INSS.

## Como usar este programa?

Ao rodar o programa será necessário informar dois valores: **ano** e **salário base**, como mostra o exemplo abaixo considerando a tabela vigente de 2022 e um salário de 6 mil reais.<br><br>

![Solicitação](https://raw.githubusercontent.com/danilotc/assets/master/solicitacao.png) <br><br>

Em seguida, basta analisar o resultado que será impresso na tela, a tabela irá indicar a faixa em que o salário informado se enquadra, logo a porcentagem dessa faixa é a que está sendo calculada, como no exemplo a seguir. <br><br>

![Resultado texto](https://raw.githubusercontent.com/danilotc/assets/master/resultado1.png) <br>
![Resultado tabela](https://raw.githubusercontent.com/danilotc/assets/master/resultado2.png) <br><br>

Este é o resultado do algoritmo funcionando. A fórmula utilizada para este cálculo específico é a seguinte:

(6.000,00 - 3.641,04) x 14 / 100 + 345,92

## O "x" da questão

Considerando que já tenha realizado os cálculos disponíveis no arquivo PDF utilizando a calculadora para validar cada resultado, gostaria de entrar no X da questão.

Como mencionei o principal objetivo deste estudo foi tentar descobrir se o valor que era descontado para o INSS na folha de pagamento estava correto, isso foi questionado por alguns colegas. De modo a esclarecer essa dúvida, comecei a investigar, unindo o pouco conhecimento que tenho sobre programação, assim obtive o seguinte resultado.

Considerando minha folha de pagamento do ano 2021, o desconto indicado foi de **R$ 88,06** que corresponde a 9% da alíquota sobre o salário base. Para realizar esse cálculo considerei o meu salário base de **R$ 1.161,78** e a resposta do algoritmo foi essa indicando exatamente o que estava sendo descontado na folha. <br><br>

![Solicitação](https://raw.githubusercontent.com/danilotc/assets/master/solicitacao2.png) <br><br>
![Resultado 3](https://raw.githubusercontent.com/danilotc/assets/master/resultado3.png) <br>
![Resultado 4](https://raw.githubusercontent.com/danilotc/assets/master/resultado4.png) <br><br>

O resultado acima é a resposta do programa que escrevi após estudar o cálculo que é utilizado para desconto do valor a ser pago ao INSS. Logo, como podemos observar, o valor descontado e a faixa em que o valor base se enquadra mostram que o desconto na folha de pagamento estava correto.

Com isso, posso afirmar que não estava sendo descontado 7,5%, mas 9% visto que o salário base ultrapassa o salário mínimo do ano em questão.

Para testar o funcionamento deste algoritmo clique na imagem abaixo.  Lembre-se apenas de utilizar `(.)` no lugar de `(,)` para separar os inteiros dos decimais.

<p align="center" size="10px">
<a href="https://replit.com/@danilocastro5/calculoinss" target="_black"><img src="https://blog.replit.com/images/logo.png" width="200px"></a>
</p>


## Tabelas oficiais utilizadas

As tabelas abaixo são a junção de duas fontes distintas, isto porque as duas primeiras colunas são oficiais do [INSS](https://www.gov.br/inss/pt-br/saiba-mais/seus-direitos-e-deveres/calculo-da-guia-da-previdencia-social-gps/tabela-de-contribuicao-mensal) enquanto a última se refere a um método utilizado pela escola [Avante RH](https://www.avanterh.net/tabeladeinss2022) para calcular o valor do INSS a ser pago pelo colaborador.


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

<br>Para compreender melhor a utilização da tabela com esta terceira coluna, caso ainda não conheça, recomendo assistir a [este vídeo](https://youtu.be/y0Ko6S_L4Vc)  com o **Prof. Rafael Lopes** da Avante RH explicando tudo com riqueza de detalhes.

## Detalhes técnicos da aplicação

Alguns métodos utilizam diferentes formas de calcular e exibir o resultado, por exemplo, alguns mostram o resultado com 3 casas decimais, outros com 2, ou ainda sempre arredondando o valor decimal. Pensando nisso, decidi manter o resultado com apenas duas casas decimais sem arredondar, para isso implementei a seguinte função. 

```python
def trunca_decimal(valor, decimal):
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))
```

Além disso, é importante observar as faixas setadas antes da sua utilização. Gostaria de realçar a quarta faixa. Com resultado *boleano* o trecho avalia se o salário está entre o valor mínimo e máximo da faixa 4 ou se é maior que ela. Em ambos os casos será aplicado alíquota de 14%.


```python
faixa4 = (salario >= min_faixa4) and (salario <= max_faixa4) or (salario > max_faixa4)
```

Este é o bloco que irá calcular alíquota de 14% independente se está no intervalo da faixa 4 ou acima do teto.

```python
# código oculto
elif faixa4:
    if salario > max_faixa4:
        valor_inss = aliq_faixa4
    else:
        valor_inss = ((salario - max_faixa3) * percentual_faixa4) + aliq_faixa3
# código oculto
```

## Considerações finais

Esta pesquisa foi realizada para tentar entender um questionamento sobre a empresa onde atualmente prestamos serviço. Acreditou-se que a mesma descontava 7,5% e colocava na folha de pagamento 9%. Contudo, esta pesquisa prova que a mesma agiu o tempo todo de forma correta. Diante disso, considero esta investigação concluída.

Caso queira saber de mais detalhes sobre essa investigação, sugiro a leitura [deste documento](https://drive.google.com/file/d/1TzN6WKTK1IrV30nFGtLCZtkr8N8nXOnk/view) com algumas fórmulas que estão sendo utilizadas pelo algoritmo, assim poderá validar cada cálculo realizado.
