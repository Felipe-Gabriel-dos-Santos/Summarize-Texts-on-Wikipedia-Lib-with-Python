import wikipedia

print('Digite o Tema ao ser Pesquisado')
Tema = input()
print('Digite a quantidade de letras que o texto terá:')
Letras = int (input())

wikipedia.set_lang('pt')
Pequisa = wikipedia.search(Tema)
print(Pequisa)

texto = wikipedia.summary(Tema, sentences=1)

letras = len(texto)

print(letras)
i = 1
while letras <= Letras:
    texto = wikipedia.summary(Tema, sentences=i)
    letras = len(texto)
    i += 1
    print(letras)
    

print(texto)


