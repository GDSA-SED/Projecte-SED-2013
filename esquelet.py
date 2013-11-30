#!/usr/bin/python
import os
import glob as g
import MySQLdb as sql

path = './image/*.jpg';
tam = len(path) - 4 # l'utiltizaré per saber on comença el nom de la imatge
x = g.glob(path) 
fitxer = raw_input("Introdueix el nom del fitxer del aprenentatge:")
mapren = dict()
if os.path.isfile(fitxer) == 0:
	# conexió
	db = sql.connect(host="localhost", user="root", passwd="root",db="GDSA")	
	for image in x:
		cursor = db.cursor()
		image = image[tam:-4]
		aprenentatge(image,&mapren,&cursor)
	serializaraprenentatge(mapren,fitxer)
else : 
	deserializaciomapren(&mapren,fitxer)

while(1):
	path = raw_input( "Introdueix el path de la carpeta de imatges a classificar, path relatiu o absolut:(per sortir del programa escrigui exit)\n")
	if path == "exit":
		break
	x = g.glob(path+"/*.jpg")
	for image in x:
		# treure els descriptors
		desc = descriptor (image)
		# clasific de la imatge
		clasificador(desc,path,&mapren)
		
		
