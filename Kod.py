#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
#coding: utf-8

'''
Transkryptor kodu genetycznego na kod aminokwasowy.
Program przyjmuje dane jako pliki .txt z zapisanym kodem w formacie fasta.
'''

import Funkcje

print('Witaj w programie do zamiany kodu DNA lub RNA na łańcuch aminokwasowy!')
plik = input('Wprowadź ścieżkę pliku: ')
dane = open(plik, 'r')

naglowki = []
kod = []
Funkcje.odczyt(dane, naglowki, kod)

Funkcje.TnaU(kod)

bialka = []
pominiete = []
Funkcje.translacja(kod, bialka, pominiete)

print('Jak chcesz nazwać docelowy plik?')
nazwa = input('Wprowadź nazwę docelowego pliku bez rozszerzenia: ')

print('Gdzie chcesz zapisać docelowy plik?')
lokalizacja = input('Wprowadź docelową ścieżkę bezwzględną: ')

utworz = lokalizacja + '/' + nazwa + '.txt'

Funkcje.zapis(utworz, naglowki, bialka)

print('Twój kod został pomyślnie przetłumaczony!')
pozostale = len(pominiete)
if pozostale > 0:
    pozostale = str(pozostale)
    print('Podczas pracy pominięto nukleotydy w liczbie: ' + pozostale)

