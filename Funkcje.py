#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Funkcje użyte w transkryptorze kodu genetycznego na kod aminokwasowy.
'''

import Slownik

def odczyt(dane, naglowki, kod):
    for informacje in dane:
        informacje = informacje.rstrip('\n')
        if informacje[0] == '>':
            naglowki.append(informacje)
            kod.append('')
        else:
            kod[-1] += informacje

def TnaU(kod):
    licznik = 0
    dlugosc = len(kod)
    if licznik <= dlugosc:
        kod[licznik] = kod[licznik].translate(kod[licznik].maketrans('T', 'U'))
        licznik += 1

def translacja(kod, bialka, pominiete):
    for RNA in kod:
        bialko = ''
        while len(RNA) % 3 != 0:
            pominiete.append(RNA[-1])
            RNA = RNA[:-1]
        for i in range(0, len(RNA), 3):
            kodon = RNA[i:i + 3]
            bialko += Slownik.kod_genetyczny_RNA[kodon]
        bialka.append(bialko)

def zapis(utworz, naglowki, bialka):
    zapisz = open(utworz, 'w')
    numer = 0
    ilosc = len(bialka) - 1
    while numer < ilosc:
        zapisz.write(naglowki[numer] + '\n')
        zapisz.write(bialka[numer] + '\n')
        numer += 1
    zapisz.write(naglowki[numer] + '\n')
    zapisz.write(bialka[numer])
    zapisz.close()

