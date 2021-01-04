#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import psycopg2,config
import cgi, cgitb
cgitb.enable()


print("""Content-type: text/html; charset=utf-8



<html>
	<head>
		<title> Graphique</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
		<style>
			h1{
				border: 5px solid grey;
			}
			
			img {
				display: block;
				margin-left: auto;
				margin-right: auto;
				width: 80%;
			}
			
			
			.work{
				display:block;
				float: auto;
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
					<li class="nav-item">
						<a class="nav-link" href="chuck.py">Retour à l'accueil</a>
					</li>
					    
				</ul>
			</div>  
		</nav""")

form = cgi.FieldStorage()
print("""<div class="container"><h1 class="text-center" >Répartition du nombre de citations par évaluation</h1></div>""")

print("""<div><img src="graphique1.png"></div>""")
	

print("""<div class="jumbotron text-center bg-dark" style="margin-bottom:0"><footer><p>Auteur : Guillaume ARNAUD</p></footer></div>""")

print("</body></html>")
