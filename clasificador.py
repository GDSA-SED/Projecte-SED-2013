# -*- coding: utf-8 -*-
import math

def clasificador(mapren,x,db,tam):
	for image in x:
		# elimino el path i la extensió de la imatge deixan solament el seu nom
		image = image[tam:-4] 
		# declaració del un cursor
		cursor = db.cursor()
		# busco els tags de la imatge
		query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
		# executo la query
		cursor.execute(query)
		aux = dict()
		print "Processing image: ", image
		# analitzo tots els tags de la imatge
		for row in cursor.fetchall():
			# mirem a aquines classes apareixen
			for clas in mapren:
				# si trobem el tag en aquella classe el posem dins de aux
				if mapren[clas].has_key(row[0]):
					# si ja tenim la clas declara al dict llavors agreguem el nou tag
					if aux.has_key(clas):
						aux[clas]+=row[0]
					# si no tenim la clas declarada al dict llavors la creem i posem el tag	
					else:
						aux[clas]=[row[0]]
		# busco el max de tags coincidents per això he de recorre aux i busca el max
		
		# màxim de tags coincidents
		maxt = 0
		for clas in aux:
			if len(aux[clas]) > maxt:
				maxt = 	len(aux[clas])
				# classes coincidents és resetegen a clas
				clasc = [clas]

			elif len(aux[clas]) == maxt:
				# s'agrega una nova classe
				clasc.append(clas)

		# si tenim 0 de coincidents el clasificarem a non_event
		if len(clasc) == 0:
			print "non_event"
			print "Len de clasc = ", len(clasc)
		# si sol tenim 1 clase amb un max de tags coincidents llavors ja la tenim clasificada
		elif len(clasc) == 1:
			print image," ",clasc[0]
			print "Len de clasc = ", len(clasc) 
		#else:
			# pasem analitzar els tf-idf per fer això farem consultes a mapren a partir dels tags que tenim guardats a aux i les clases coincidents que tenim a clasc
			# TODO 
