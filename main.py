from vendas.calc_precos import aumento,reducao
from vendas.formata import preco

preco = 50.00

preco_aumento =  aumento(valor= preco,porcentagem=10,formata=True)
print(preco_aumento)

preco_reducao =  reducao(valor= preco,porcentagem=10,formata=True)
print(preco_reducao)