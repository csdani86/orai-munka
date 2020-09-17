# Formazott kimenet


szam = 35.3634
print("|%20.2f|" % szam) # %d - egesz szam, %f - tort szam. % -jel es a valtozo neve
       # a % és az f vagy d közötti szám meghatarozza a karakter hosszat bal:
       #hany db karakteren helyezkedik el az ertek
       
szam2 = 3425.1234
print("|%20.2f|" % szam2)
# a % es d/f kozotti szam meghatarozza hany darab tizedes jegy van 
# "%-20.2f" : a - balra igazitja 

#szöveg kiiratása
nev = 'Csizmar Daniel'
print("|%20s|" % nev) #karaktersor esetén s-t használunk

ar = 340480.0
print("Ár: %16.2f Ft" % ar)
      #tetszőleges szöveg

betu = "a"
print("%c" % betu) # c-t használunk ha 1 db karaktert akarunk kíratni


'''
print("formátum sztring" % változó_kifejezés_állandó)

	formátum_sztring > mindig % jellel kezdődik
	formátum_sztring > mindig formátum karakterrel végződik
	formátum karakterek:	
	* d decimális egész
	* f float (lebegőpontos számot)
	* s stringet (karaktersorozatot)
	* c character (karakter kiíratása esetén)

Példa:
	"%d"

A kettő között
	jelzők szélesség .pontosság
	0 vezető nulla
	+ előjel kiírása minden esetben
	-balra igazítás
	
_Modulok használata_
 Importálni kell a modulokat : import
 
 import modulNev
 
 _Matematiaki mdoul_
 
 Neve: Math
 
 pl:
 '''
 
 import math
 
 ertek = sqrt(18)
 print(ertek)
 
 ertek = math.sin(1)
 print(ertek)
