#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psycopg2, config # import librairies
import cgi, cgitb
#~ import pandas
cgitb.enable()

print("""Content-type: text/html; charset=utf-8

<html>
  <head>
    <title>hausses et baisses</title>
    <link rel="stylesheet" href="config.css"/>
  </head>
  <body>""")

print("<h2>Bot’Norris</h2>")

form = cgi.FieldStorage() # récupération des info de paramètres

l = 10

if 'l' in form:
    l = form['l'].value
    print(f"paramètre l={l}")

conn = psycopg2.connect(database="bdd_garnaud", user=config.user, password=config.password, host='localhost') # connexion
cur = conn.cursor() # session


print('<hr/><h3>Les hausses</h3>')

cur.execute('''
SELECT blagues.id,citations,D1.rate,D2.rate, D2.rate-D1.rate AS diff FROM "blagues" AS J
INNER JOIN "infos" AS D1 ON (J.id=D1.id AND D1.date='2020-12-09')
INNER JOIN "infos" AS D2 ON (J.id=D2.id AND D2.date=NOW()::date)
WHERE ((D1.vote!=D2.vote) AND (D1.rate<D2.rate))
ORDER BY diff DESC LIMIT 15;''') # requête SELECT
for data in cur.fetchall() : # récupération des lignes
    print("<li class='high'>%s :<i>%s</i>; rate +%s (%s-%s)</li>" % (data[0], data[1], data[4], data[2], data[3]))

print('<hr/><h3>Les baisses</h3>')

cur.execute('''
SELECT blagues.id,citations,D1.rate,D2.rate, D2.rate-D1.rate AS diff FROM "blagues" AS J
INNER JOIN "infos" AS D1 ON (J.id=D1.id AND D1.date='2020-12-09')
INNER JOIN "infos" AS D2 ON (J.id=D2.id AND D2.date=NOW()::date)
WHERE ((D1.vote!=D2.vote) AND (D1.rate>D2.rate))
ORDER BY diff LIMIT 15;''') # requête SELECT
for data in cur.fetchall() : # récupération des lignes
    print("<li class='low'>%s :<i>%s</i>; rate %s (%s-%s)</li>" % (data[0], data[1], data[4], data[2], data[3]))


print("""<p>retour haut de page <a href="indic_stats.py?l=200">ici</a></p>""")

print("<hr/>")





conn.close()


print("</body></html>")
