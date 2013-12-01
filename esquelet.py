#!/usr/bin/python
import os
import glob as g
import MySQLdb as sql
import aprenentatge
import decimal as d
path = './image/*.jpg' # directori de imatges
tam = len(path) - 5  # s'utilitzara per obtenir el nom de la imatge
x = g.glob(path)  # obtenim una llista de paths de les imatges a processar
fitxer = raw_input("Introdueix el nom del fitxer del aprenentatge:") # demanem el nom del fitxer d'aprenentatge
mapren = dict() # declarem el dict buit
if ~os.path.isfile(fitxer): # si no existeix el fitxer d'aprenentatge el crearem
	query = "SELECT count(*) FROM sed2013_task2_dataset_train_tags;" # query per contar el nombre de tags totals
	db = sql.connect(host="localhost", user="root", passwd="root",db="gdsa") # conexió a la base de dades
	cursor = db.cursor() # creem el cursor
	cursor.execute(query) # executem la query
	count = d.Decimal(cursor.fetchall()[0][0]) # obtenim el total de tags. SOL SERÀ ÚTIL EN CAS QUE VULGUEM UTILITZAR EL COUNT A LA FUNCIÓ D'APRENENTATGE
	for image in x: # analitzem totes les imatges
		image = image[tam:-4] # obtenim el nom de la imatge
		mapren=aprenentatge.aprenentatge(image,mapren,db,count) # aprenem les classes i guardem els descriptors de classe, SI NO VOLEM EL METODE QUE DIVIDEIX LES DADES PEL NOMBRE TOTAL DE TAGS TREIEM EL PARAMETRE COUNT
	
	db.close() # tanquem la conexió de la base de dades

# ELS SEGÜENTS COMENTARIS ELS HE POSAT PER A QUE COMPILI EL CODI A MESURA QUE TINGUEM LES FUNCIONS FETES HAUREM DE TREURE ELS COMENTARIS

#	serializaraprenentatge(mapren,fitxer)
#else : 
#	deserializaciomapren(&mapren,fitxer)

#while(1):
#	path = raw_input( "Introdueix el path de la carpeta de imatges a classificar, path relatiu o absolut:(per sortir del programa escrigui exit)\n")
#	if path == "exit":
#		break
#	x = g.glob(path+"/*.jpg")
#	for image in x:
#		# treure els descriptors
#		desc = descriptor (image)
#		# clasific de la imatge
#		clasificador(desc,path,&mapren)
		
