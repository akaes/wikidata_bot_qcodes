#!/usr/bin/python3
import pywikibot
import csv

qcodes = []
count = 0

#einlesen der csv-datei
fin = open("test.csv", "r")

#ermitteln des q-codes und schreiben in eine neue datei
for name in fin:
    #festlegen der wikidate-parameter
    site = pywikibot.Site("de", "wikipedia")
    page = pywikibot.Page(site, name)
    item = pywikibot.ItemPage.fromPage(page)
    #zusammenführen des strings
    newName = str(page)+str(item)
    #schreiben in das leere array qcodes
    qcodes.append(newName)
    #zähler hochzählen und anzeigen
    count = count+1
    print(count)
    
#speichern des arrays in eine datei
with open("ergebnis.csv", "w") as fout:
    writer = csv.writer(fout, lineterminator='\n')
    for val in qcodes:
        writer.writerow([val])    
fout.close()





