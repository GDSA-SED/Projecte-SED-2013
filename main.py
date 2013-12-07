#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob as g
import MySQLdb as sql
import aprenentatge
import clasificador
import learndatamani as l

path = './image/*.jpg' 
tam = len(path) - 5  
x = g.glob(path) 
db = sql.connect(host="localhost", user="root", passwd="root",db="gdsa")  
nfile = raw_input("Introdueix el nom del fitxer del aprenentatge:")
if not os.path.isfile(nfile): 
	query = "SELECT count(*) FROM sed2013_task2_dataset_train_tags;" 
	learn = aprenentatge.aprenentatge(x,tam,db)
  	l.serialization(learn,nfile)
else : 
	learn= l.deserialization(nfile)
   	
path = raw_input( "Introdueix el path de la carpeta de imatges a classificar, path relatiu o absolut \n")
tam = len(path)
x = g.glob(path+"/*.jpg")

#clasificació de la imatge
clasificador.clasificador(learn,x,db,tam)

db.close()
