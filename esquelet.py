#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob as g
import MySQLdb as sql
import aprenentatge
import decimal as d
path = './image/*.jpg' 
tam = len(path) - 5  
x = g.glob(path)  
fitxer = raw_input("Introdueix el nom del fitxer del aprenentatge:") 
if ~os.path.isfile(fitxer): 
	query = "SELECT count(*) FROM sed2013_task2_dataset_train_tags;" 
	db = sql.connect(host="localhost", user="root", passwd="root",db="gdsa") 
	mapren =aprenentatge.aprenentatge(x,tam,db)
	db.close()
#hola

#	serializaraprenentatge(mapren,fitxer)
#else : 
#	deserializaciomapren(&mapren,fitxer)

#while(1):
#	path = raw_input( "Introdueix el path de la carpeta de imatges a classificar, path relatiu o absolut:(per sortir del programa escrigui exit)\n")
#	if path == "exit":
#		break
#	x = g.glob(path+"/*.jpg")
#	for image in x:
#		# clasific de la imatge
#		clasificador(mapren,image,db)
		
		
		
