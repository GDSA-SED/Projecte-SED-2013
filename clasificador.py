# -*- coding: utf-8 -*-
def clasificador(mapren,x,db,tam):
	f=open('results.txt','w')
	for image in x:
		result=[]
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
						aux[clas]+=[ row[0] ]
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
			
			f.write(image+' non_event\n')
			
		# si sol tenim 1 clase amb un max de tags coincidents llavors ja la tenim clasificada
		elif len(clasc) == 1:

			f.write(image+" "+clasc[0]+'\n')
			
			
		else:
			# pasem analitzar els tf-idf per fer això farem consultes a mapren a partir dels tags que tenim guardats a aux i les clases 				coincidents que tenim a clasc
			
			#iterem clasc, que ocnte les possibles classes de la imatge	
			for k in range( 0,len(clasc) ) :
				
				#iterem aux
				for cl in aux:
					
					#mirem les clases que estan a aux i a clasc
					if clasc[k]==cl:			
						#iterem li
						tfidf=0
						for t in range( 0,len(aux[cl]) ):															
							# A la variable result guardem la lclasse que pot ser la imatge i el tfidf total
							tfidf+= mapren [ clasc[k] ][ aux[cl][t]  ]
						result+= [ [cl, tfidf] ]

			#iterem result per veure quina classe te el tfidf major, ens quedarem amb la classe que tingui un major tfidf.
			maxtdidf=0
			for k in range( 0, len(result) ):
				if result[k][1]>maxtdidf: 			
					clas = result[k][0]
					maxtdidf=result[k][1]
			f.write(image+" "+clas+'\n')			
	f.close()		
			



