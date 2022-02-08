def trunca_decimal(valor, decimal=2):
    """
    O valor é obrigatório, a quantidade de casas decimais é
    opcional, mas recebe 2 como padrão.
    
    Para modificar a quantidade de casas decimais, digite a
    quantidade no segundo parâmetro.
    """
    lista = str(valor).split('.')
    inteiro = lista[0]
    decimal = lista[1][:decimal]
    return float('.'.join([inteiro, decimal]))
	