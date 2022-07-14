string = 'O rato roeu a roupa do rei de roma'
def espaco(x):
    global count
    if x == ' ':
        count += 1


tamanho = (lambda x: len(x))(string)
print(tamanho)

#contar quantos espaços tem em uma string
count = 0
espacos = list(map(espaco, string))
print(count)