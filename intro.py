#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import psycopg2
import cgi, cgitb
cgitb.enable()


print("""Content-type: text/html; charset=utf-8



<html>
        <head>
                <title>Introduction</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
		<link href="styles.css" rel="stylesheet" type="text/css">
		<?xml-stylesheet type="text/css" href="styles.css">
		<style>
			rect {
			   fill: #B5CC45;
			   stroke: black;
			   stroke-width: 2px;
			}
			.center-div {
				margin: 0 auto;
				width: 300px; 
			}
			h1 , p{
				text-align :center;
			
			}
			h1{
				font-size: 90px;
				margin-top:90px;
			
			}
			p{
				font-size: 35px;
			
			}
		</style>
        </head>
        <body>
		""")
	

form = cgi.FieldStorage()


print("""<div class="container">
		<h1>Le projet Bot' Norris</h1>
		
	</div>""")
print("""<HR align=center size=10 width="50%">""")

print("""<div><p>Cliquer sur l'image pour entrer dans le monde des citations à 2 balles !</p></div>

		<div class="center-div"><a href="chuck.py"><img src="im1.jpeg" alt="image_chuck" style="width:300px;height:350px;"></a></div>""")


 
print("""</body></html>""")
