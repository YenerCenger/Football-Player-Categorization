# -*- coding: utf-8 -*-

bjk = []
gs = []
fb = []
def futbolcu_takım(a):
    a = a[:-1]
    liste = a.split(",")

    isim = liste[0]
    takım = liste[1]

    if takım == "Beşiktaş":
        bjk.append(isim)
    elif takım == "Fenerbahçe":
        fb.append(isim)
    elif takım == "Galatasaray":
        gs.append(isim)


with open("futbolcular.txt","r",encoding="utf-8") as file:
    for i in file:
        futbolcu_takım(i)

    with open("Beşiktaş.txt","w",encoding="utf-8") as file1:
        for i in bjk:
            file1.write(i+"\n")

    with open("Fenerbahçe.txt","w", encoding="utf-8") as file2:
        for i in fb:
            file2.write(i + "\n")

    with open("Galatasaray.txt","w", encoding="utf-8") as file3:
        for i in gs:
            file3.write(i + "\n")

