def trunca_decimal(valor, decimal):
	"""
	Recebe um valor real e a quantidade de casas decimais desejada,
	retorna o mesmo valor com 2 casas decimais não arredondadas.
	"""
	lista = str(valor).split('.')
	inteiro = lista[0]
	decimal = lista[1][:decimal]
	return float('.'.join([inteiro, decimal]))
	