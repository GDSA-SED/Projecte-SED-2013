# -*- coding: utf-8 -*-
def classifier(dlearn,x,db,tam):
	f=open('./results/3.1.txt','w')
	for image in x:
		result=[]
		# get the name of the image
		image = image[tam:-4] 
		# initialization of cursor
		cursor = db.cursor()
		# search the tags of the image 
		query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
		# execute the query
		cursor.execute(query)
		aux = dict()
		# wander the tags
		for row in cursor.fetchall():
			row=row[0].lower()
			# search in which classes it appears
			for clas in dlearn:
				# if the tag is found in that class, put it on aux
				if dlearn[clas].has_key(row):
					# if we already have the class, declare it in dict and add the new tag
					if aux.has_key(clas):
						aux[clas]+=[ row ]
					# if we don't have the class in dict, then it is created and add the new tag
					else:
						aux[clas]=[row]
		# search the coincidents tags
		maxt = 0
		for clas in aux:
			if len(aux[clas]) > maxt:
				maxt = 	len(aux[clas])
				# reset the coincident class
				clasc = [clas]
				
			elif len(aux[clas]) == maxt:
				# add new class
				clasc.append(clas)

		# if we have 0 coincident, we classify it at non_event
		if len(clasc) == 0:
			
			f.write(image+' non_event\n')
			
		# if we have 1 coincident, we classify it in that class
		elif len(clasc) == 1:

			f.write(image+" "+clasc[0]+'\n')
			
			
		else:
			#we analize the tf-idf through consulting the tags and coincident classes
			#iterate clasc, that contains possible classes of the image	
			for k in range( 0,len(clasc) ) :
				
				#iterate aux
				for cl in aux:
					
					#check the clases that are at aux and at clasc
					if clasc[k]==cl:			
						#iterate li
						tfidf=0
						for t in range( 0,len(aux[cl])): 															
							# At result we save the class that can be the image an the total tfidf 
							tfidf+= dlearn [ clasc[k] ][ aux[cl][t]  ]
						result+= [ [cl, tfidf] ]

			#iterate result to search the class with more tf-idf, we'll keep that class
			maxtdidf=0
			for k in range( 0, len(result) ):
				if result[k][1]>maxtdidf: 			
					clas = result[k][0]
					maxtdidf=result[k][1]
			f.write(image+" "+clas+'\n')			
	f.close()		
