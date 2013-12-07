# -*- coding: utf-8 -*-
import math
import decimal as d
def aprenentatge(x,tam,db):
	# declaro una llista buida
	mapren = dict()

	# declaro una variable auxiliar per fer el càlcul del idf
	ctags = dict()
	
	# recorro totes les imatges de la carpeta
	for image in x: 
		# elimino el path i la extensió de la imatge deixan solament el seu nom
		image = image[tam:-4] 
		# declaració del un cursor
		cursor = db.cursor() 
		# busco la classe a la qual pertany la imatge
		query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ str(image) + "';" 
		# executo la query
		cursor.execute(query) 
		# obtinc la classe i la guardo a key
		key=cursor.fetchall()[0][0] 
		# busco la classe a la qual pertany la imatge
		query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
		# executo la query
		cursor.execute(query)
		# recorro tots els tags
		for row in cursor.fetchall(): 
			# si a mapren ja existeix la classe que estem processant
			if mapren.has_key(key):
				# si a la classe que estem processant ja te el tag sumem 1 al nombre de tags				
				if mapren[key].has_key(row[0]): 
					mapren[key][row[0]]+=1
				# si no te el tag inicialitzem el tag a 1
				else: 
					mapren[key][row[0]]=1

					# càlcul de en quantes clases(documents) apareix el tag
					# si ja tenim el tag procesat sumem 1
					if ctags.has_key(row[0]):
						ctags[row[0]]+=1;
					# si no tenim el tag procesat l'inicialitzem a 1						
					else:
						ctags[row[0]]=1;
			
			else:  
				mapren[key]={row[0]:1}
	# càlcul del idf per saber si la paraula és rara en els documents (documents = classes)
	ndocuments = len(mapren)
	for k in ctags:

		ctags[k]=d.Decimal(math.log10(ndocuments/float(ctags[k]+1)))

	# càlcul del tf-idf 
	for clas in mapren:
		ntag=d.Decimal(len(mapren[clas]))
		amax = 0;
		# busco el tag amb més aparicions
		for key in mapren[clas]:
			if amax < mapren[clas][key]:
				amax = 	mapren[clas][key]
		# càlcul del tf-idf d'aquesta clase		
		for tag in ctags:
			if mapren[clas].has_key(tag):
				mapren[clas][tag]=float((((d.Decimal(0.5)*mapren[clas][tag])/ntag)/(amax/ntag)+d.Decimal(0.5))*ctags[tag])	
						 
	return mapren
