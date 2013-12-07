#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob as g
import MySQLdb as sql
import aprenentatge
import decimal as d
import learndatamani as l

path = './image/*.jpg' 
tam = len(path) - 5  
x = g.glob(path)  
nfile = raw_input("Introdueix el nom del fitxer del aprenentatge:") 
if not os.path.isfile(nfile): 
	query = "SELECT count(*) FROM sed2013_task2_dataset_train_tags;" 
	db = sql.connect(host="localhost", user="root", passwd="root",db="gdsa") 
	mapren = aprenentatge.aprenentatge(x,tam,db)
	db.close()
	l.serialization(mapren,nfile)
else : 
	mapren= l.deserialization(nfile)
	

path = raw_input( "Introdueix el path de la carpeta de imatges a classificar, path relatiu o absolut \n")
tam = len(path)
x = g.glob(path+"/*.jpg")
for image in x:
	image = image[tam:-4]
	#clasificació de la imatge
	clasificador(mapren,image,db)
		
		
		
