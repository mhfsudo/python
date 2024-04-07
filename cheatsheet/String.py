# String in Char aufteilen
s = "Python"
print(s[0])
print(s[-5])
indexLastChar = len(s) - 4
print(s[indexLastChar])
print(s[indexLastChar + 1])
LastCharacter = s[-2]
print(LastCharacter)

# String länge
a = "linux"
print(len(a))  # output 5

# String vergleichen
a = "Linux"
b = "Linux"
print(a is b)  # output True

##funktioniert nicht in der Console wenn Sonderzeichen vorhanden
a = "Linux!"
b = "Linux!"
print(a is b)  # output True

# String kuerzen
txt = "Hello World"
print(txt[1:7])  # output ello W
print(txt[1:10:2])  # output el ol

# String umkehren
print(txt[::-1])  # output dlroW olleH

# upper case
a = "Hello World"
print(a.upper())  # output HELLO WORLD

# lower case
print(a.lower())  # output hello world

# concatenate number and text
text = "I'm {} years old"
number = 30
print(text.format(number))  # output I'm 30 years old


"""
\       Zeilenfortsetzung
\\      Backslash
\'      Einzel Ausführunszeichen
\"      Doppel Ausfpührungszeichen
\a      Glocke
\b      Rücskschritt (backspace)
\e      Ausmaskieren
\0      Null
\n      Zeilenvorschub (Linefeed)
\v      Vertikaler Tabulator
\t      Horizontaler Tabulator
\r      Wagenrücklauf (Carriage Return)
\f      Seitenvorschub (form feed)
"""
