
x = int(input("Inserisci il primo numero:> "))
y = int(input("Inserisci il secondo numero:> "))
z = int(input("Inserisci il terzo numero:> "))

if x >= y and x >= z:
    massimo = x
elif y >= x and y >= z:
    massimo = y
else:
    massimo = z

print('Il massimo è', massimo)
