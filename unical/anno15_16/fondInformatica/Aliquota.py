print ("Salve...Dovrebbe inserire il suo reddito per avviare lo script-calcolo delle aliquota 2015/2016")
reddito = float (input ("Digiti di seguito il suo reddito: "))


if reddito < 20000 and reddito > 0 :
   aliquota2 = 2/100
   print ("L'aliquota è del",aliquota2,"%")
   tassa1 = (reddito * aliquota2)
   print ("La tassa ammonta a:",tassa1)

elif reddito > 2001 and reddito < 50000 and reddito != 0 :
    aliquota5 = 5/100
    print ("L'aliquota è del",aliquota5,"%")
    tassa2 = (reddito * aliquota5)
    print ("La tassa ammonta a:",tassa2)

elif reddito > 50000 and reddito < 1000000000 :
    aliquota9 = 9/100
    print ("L'aliquota è del",aliquota9,"%")
    tassa3 = (reddito * aliquota9)
    print ("La tassa ammonta a:",tassa3)
elif reddito > 1000000000 :
    print ("E chi ssi...Bill Gates !?")
else:
   print ("Povero...")
