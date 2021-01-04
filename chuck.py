usr/bin/python3
# -*- coding: UTF-8 -*-
import psycopg2
import cgi, cgitb
cgitb.enable()


print("""Content-type: text/html; charset=utf-8



<html>
        <head>
                <title>Le projet Bot’ Norris</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
		<link href="styles.css" rel="stylesheet" type="text/css">
		<style>
			nav ul li{
				margin:0 20px; 
			}
			h1{
				text-align :center;
				margin-top:70px;
			
			}
			.container{
				margin-bottom: 20px;
			}
		</style>
        </head>
        <body>
		<nav class="navbar navbar-expand-md bg-dark navbar-dark"> <!-- menu de navigation -->
			<a class="navbar-brand" href="#">Bot' Norris</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="collapsibleNavbar">
				<ul class="navbar-nav">
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
							Les thèmes
						</a>
						<div class="dropdown-menu">
							<a class="dropdown-item" href="theme9.py">Le voyage</a>
							<a class="dropdown-item" href="theme8.py">Le sport</a>
							<a class="dropdown-item" href="theme1.py">Les virus</a>
							<a class="dropdown-item" href="theme2.py">Le combat</a>
							<a class="dropdown-item" href="theme5.py">La cuisine</a>
							<a class="dropdown-item" href="theme6.py">Les fêtes</a>
							<a class="dropdown-item" href="theme4.py">Top 10 des mieux notées</a>
							<a class="dropdown-item" href="theme7.py">Top 10 des meilleurs évaluations</a>
							
						</div>
					</li>
					
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
							outils
						</a>
						<div class="dropdown-menu">
							<a class="dropdown-item" href="modelisation.py">Modèle BDD</a>
							<a class="dropdown-item" href="rapport_donnees.py">Rapport sur les données</a>
							<a class="dropdown-item" href="https://trello.com/b/TDy9ZDMM/projet3">le Trello</a>
							<a class="dropdown-item" href="https://chucknorrisfacts.net/">Source du scraping</a>
							<a class="dropdown-item" href="graphiques.py">Graphiques</a>
							<a class="dropdown-item" href="projet3graph.pdf">Bdd>dataframe</a>
							<a class="dropdown-item" href="web_bdd.pdf">Web>Bdd</a>
						</div>
					</li>
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					<li>
						<div></div>
					</li>
					
					<li>
						<div></div>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="contact.py">Envoyer un commentaire</a>
					</li>
				</ul>
			</div>  
		</nav>""")
	

form = cgi.FieldStorage()


print("""<div class="container-fluid">
		<h1>Le projet Bot' Norris</h1>
	<HR align=center size=10 width="50%">		
		<p>Concevoir un agent / bot qui interroge une page web, extraie des données,
		alimente une base de données et réalise un reporting simplifié.</p>
		
		<p>
			<ul>
				<li>1 script Python fonctionnel, reproductible, commenté et disponible sur Github</<li>
				<li>1 table SQL alimentée et respectant les conditions demandées</li>
				<li>1 rapport simplifié sur les données de la base : des indicateurs statistiques et 1 graphique</li>
				<li>1 Trello du projet</li>
				<li>Bonus : gestion des erreurs, enrichissement des données en base (source complémentaire de
		données avec modèle relationnel), fonctionnalités supplémentaires, rapport de données
		avancé, mise en œuvre des concepts d’apprentissage supervisé et non supervisé, etc.</li>
			</ul>
		</p>           
	</div>""")

print("""<div class="container">
		<img src="im3.jpeg" class="mx-auto d-block" style="width:50%"> 
	</div>""")

print("""<div class="jumbotron text-center bg-dark" style="margin-bottom:0"  ><footer><p>Auteur : Guillaume ARNAUD</p></footer></div>""")
 
print("</body></html>")
