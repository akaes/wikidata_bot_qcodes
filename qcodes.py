#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import pywikibot
import csv

qcodes = []
count = 0

#einlesen der csv-datei "test.csv"
fin = open("test.csv", "r")

#ermitteln des q-codes und schreiben in eine neue datei "ergebnis.csv"
for name in fin:
    #festlegen der wikidata-parameter
    site = pywikibot.Site("de", "wikipedia")
    page = pywikibot.Page(site, name)
    item = pywikibot.ItemPage.fromPage(page)
    #zusammenführen des strings
    newName = str(page)+str(item)
    #schreiben des strings in das array "qcodes"
    qcodes.append(newName)
    #zähler hochzählen und anzeigen - wichtig für fehlersuche
    count = count+1
    print(count)
    
#speichern des arrays "qcodes" in die leere vorher angelegte ausgabedatei
with open("ergebnis.csv", "w") as fout:
    writer = csv.writer(fout, lineterminator='\n')
    for val in qcodes:
        writer.writerow([val])    
fout.close()
