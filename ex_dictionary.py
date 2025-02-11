from collections import defaultdict

word= "Espadón de fumo del dark souls 2"

contador = {}

for letra in word:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] =1

print(contador)