
zahl1 = input("Was ist deine erste Zahl?")
zahl2 = input("Was ist deine zweite Zahl?")
aktion = input("Welche Aktion willst du? (+/-/*/:)")

zahl1 = int(zahl1)
zahl2 = int(zahl2)

summe1 = zahl1+zahl2
summe2 = zahl1-zahl2
summe3 = zahl1*zahl2
summe4 = zahl1/zahl2


if(aktion == "+"):
    print("Das Ergebnis von", zahl1,"+", zahl2,"=", summe1)
if(aktion == "-"):
    print("Das Ergebnis von", zahl1,"-", zahl2,"=", summe2)
if(aktion == "*"):
    print("Das Ergebnis von", zahl1,"*", zahl2,"=", summe3)
if(aktion == "/"):
    print("Das Ergebnis von", zahl1,"/", zahl2,"=", summe4)
