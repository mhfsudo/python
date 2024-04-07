#Datenausgabe von File
#r = read
fr = open("Test.txt","r")
for line in fr:
    print(line.rstrip())
fr.close()

#Datenausgabe in File
#w = write
fw = open("Test.txt","w")
print("Test Text1", file=fw)
fw.write("Test Text2")
fw.close()

#Mit a wird Datei nicht überschrieben sondern ergänzt
fw = open("Test.txt","a")
print("Test Text3", file=fw)
fw.write("Test Text4")
fw.close()
