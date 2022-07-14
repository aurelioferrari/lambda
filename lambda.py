# receber uma lista de nomes e retornar uma lista com a string Sr. adicionada

nomes = ['aurelio', 'gabriel', 'roberto', 'luiz']

def senhor(i):
    return 'Sr.'+i

def mostrar(s):
    print(s)

senhores = map(senhor, nomes)

final = list(senhores)

print(final)

imprimir = list(map(mostrar, final))

# com lambda
print('')
imprimir = map((lambda nome: 'Sr.' + nome), nomes)

teste = list(map(lambda i: print(i), imprimir))





