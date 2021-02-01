"""
formataao de string
"""
nome = 'Maria'
idade = 32
altu = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altu ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc {imc:.2F}') # 2F DEIXA SO DUAS CASAS DECIMAIS A VISTA
print('{} tem {} anos de idade e seu imc {:.2f}'.format(nome, idade, imc))
print('{im} tem {n} anos de idade e seu imc {i:.2f}'.format(n=nome, i=idade, im=imc))

