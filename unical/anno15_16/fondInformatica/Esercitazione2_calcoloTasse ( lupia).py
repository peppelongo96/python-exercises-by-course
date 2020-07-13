

reddito = int(input("Inserisci il tuo reddito:> "))

aliquota2 = 2/100
aliquota5 = 5/100
aliquota9 = 9/100

if reddito < 20000:
    tasse = aliquota2 * reddito

elif 2000 <= reddito <= 50000:
    tasse = aliquota5 * reddito

else:
    tasse = aliquota9 * reddito

print("Tasse totali =", tasse)
