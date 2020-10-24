#Pickle Modul
#Objekte in Datei schreiben
import pickle
cities = ["Basel", "Bern", "Zürich"]
fh = open("data.pkl","bw")
pickle.dump(cities,fh)
fh.close()

#Objekte aus Datei lesen
import pickle
f = open("data.pkl","rb")
staedte = pickle.load(f)
print(staedte)