import calculo_inss_2021_2022 as calcular

# Trata mensagem de erro, caso o valor necessário seja digitado de forma
# incorreta, o sistema será encerrado e uma mensagem mais intuitiva será
# mostrada ao usuário (valor digitado é inválido...).
try:
    ano = int(input("Ano de contribuição [2021 ou 2022]: "))
    incremento = 0
    while ano not in (2021, 2022):
        # Enquanto o valor digitado não for igual a 2021 ou 2022
        # este bloco será executado infinitamente solicitando o
        # valor correto.
        ano = int(input("\033[31mAno não aceito!\033[m Tente novamente digitando 2021 ou 2022: "))
        incremento += 1
    calcular.inss(ano)
except ValueError:
    print("Valor inválido! Tente novamente digitando 2021 ou 2022")
