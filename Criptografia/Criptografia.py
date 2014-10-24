criptografia = {'a':'e', 'e':'i', 'i':'o', 'o':'u', 'u':'a'}

palavra = 'algoritmo'
saida = ""

for c in palavra:
    if c in criptografia.keys():
        saida = saida + criptografia[c]
    else:
        saida = saida + c
        
print (saida)
