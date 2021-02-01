"""
Criar uma variavel para nome(str), idade (int)
altura float e peso float de uma pessoa
Obter o NO DE BNASCIMENTO DA PESSOA(BASEADO NA IDADE E NO ANO ATUAL
OBTER O imc DA PESSOA CM 2 CASA DECIMAIS(PESO E NA ALTURA DA PESSOA
EXIBIR UM TEXTO COM TODOS O VALORES NA TELA USANDO f-sTRINGS (COM AS CHAVES)
"""
nome = 'Jesus'
idade = 50
alt = 1.69
peso = 80
ano_atual = 2020
ano_nascimento = (idade - ano_atual)
imc = peso / (alt ** 2)

print(f'{nome} tem {idade} anos de idade. {alt} de altura. Pesa {peso} kg. O imc de {nome} é  {imc:.2F}')
print(f'{nome} nasceu em {ano_nascimento}')
