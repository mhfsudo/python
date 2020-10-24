#String in Char aufteilen
s = "Python"
print(s[0])
print(s[-5])
indexLastChar = len(s) - 4
print(s[indexLastChar])
print(s[indexLastChar+1])
LastCharacter = s[-2]
print(LastCharacter)

#String vergleichen
a = "Linux"
b = "Linux"
print(a is b)
#funktioniert nicht in der Console wenn Sonderzeichen vorhanden
a = "Linux!"
b = "Linux!"
print(a is b)

#String kuerzen
txt = "Hello World"
print(txt[1:7])
print(txt[1:10:2])

#String umkehren
print(txt[::-1])

"""
\       Zeilenfortsetzung
\\      Backslash
\'      Einzel Ausführunszeichen
\"      Doppel Ausfpührungszeichen
\a      Glocke
\b      Rücskschritt
\e      Ausmaskieren
\0      Null
\n      Zeilenvorschub (Linefeed)
\v      Vertikaler Tabulator
\t      Horizontaler Tabulator
\r      Wagenrücklauf (Carriage Return)
\f      Seitenvorschub
\0XX    Oktaler Wert
\xXX    Hexadezimaler Wert
"""


