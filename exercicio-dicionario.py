pessoa = [{
    'nome':'Daiane',
    'idade':30,
    'cidade':'Campos'}]
pessoa['cidade']='Rio de Janeiro' #alterar item do dicionário
pessoa['profissão']='artista' #adicionar campo no dicionário
pessoa.pop('idade') #remover campo

print(pessoa)

if 'nome' in pessoa: # ver se chave existe no dicionário 
    print('Sim, a chave nome esta no dicionário pessoa')

#dicionário de numeros 1 a 5 e seus ²
numeros_quadrados = {i: i**2 for i in range (1,6)}
print(numeros_quadrados)
