def trunca_decimal(valor, decimal):
    """
    Recebe um valor real (string ou float) e a quantidade de casas decimais desejada,
    retorna o mesmo valor truncado com 2 casas decimais não arredondadas convertido
    para float.
    """
    lista = str(valor).split('.')
    return float('.'.join([lista[0], lista[1][:decimal]]))
