#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:14:48 2020

@author: guillaume
"""

import requests
import re
from bs4 import BeautifulSoup
import psycopg2, config

# connection à PG, bdd_garnaud
conn = psycopg2.connect(database="bdd_garnaud", user=config.user,password=config.password, host='127.0.0.1') 
cur = conn.cursor() 
                       
                        


# fonction qui permet de remplir les 2 tables de la bdd  
def traiteInfo(id, rate, vote, fact):
        print("%4d : %.2f %5d %s" % (id, rate, vote, fact))
        cur.execute("""INSERT INTO public."blagues" VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;""", (id, fact))
        cur.execute("""INSERT INTO public."infos" VALUES (NOW()::date, %s, %s, %s) ON CONFLICT DO NOTHING;""", (rate, vote,id))
        


#fonction qui gère la récupération des données
def recupPage(page):
    url = "https://chucknorrisfacts.net/facts.php?page=%d" % (page)
    print("\nRécupération de %s" %(url))
    # extraction du document HTML
    r = requests.get(url, headers={"User-Agent": "Mon navigateur perso d'ici"})
    # Traitement des données avec la librairie BS4
    soup = BeautifulSoup(r.content, 'html.parser')
    # Récupération de tous les blocks qui contiennent les info qui nous intéressent.
    # Utilisation de soup.select avec un selecteur CSS
    blocks = soup.select("#content > div:nth-of-type(n+2)")
    # on récupère les données recherchées sur tous les blocs d'une page
    for block in blocks: 
        # Recherche des champs (rate, vote, fact)
        # On affiche (si la variable fact n'est pas vide)
        fact = block.select_one("p")
        if fact is not None:
            id = block.select_one("ul.star-rating").attrs['id']
            rate = block.select_one("span.out5Class")
            vote = block.select_one("span.votesClass")
            traiteInfo(int(id[6:]), float(rate.text), int(vote.text[:-6]), fact.text)

"""
# fonction non active (à revoir) pour gérer le nombre x de pages à récupérer

def nbPage(page):  
    url = "https://chucknorrisfacts.net/facts.php?page=%d" % (page)
    print("\nRécupération de %s" %(url))
    # extraction du document HTML
    r = requests.get(url, headers={"User-Agent": "Mon navigateur perso d'ici"})
    # Traitement avec la librairie BS
    soup = BeautifulSoup(r.content, 'html.parser')
    lastPage = soup.select("#content  a:link")
    lastOne= str(lastPage[-1].get("href"))
    number=re.findall(r'\d+',lastOne)
    return(int(number[0]))
"""

        
        
for p in range(267):
    recupPage(p)
    
  # affichage sur la console des données qui sont récupérées  
cur.execute("""SELECT COUNT(*) FROM "blagues";""")
print(cur.fetchall())
conn.commit()
conn.close()
