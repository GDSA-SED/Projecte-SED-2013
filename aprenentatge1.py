def aprenentatge(image,mapren,db):
	cursor = db.cursor() # obtinc el cursor
	query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ str(image) + "';" # select per obtenir la classe de la imatge
	cursor.execute(query) # executem la query
	key=cursor.fetchall()[0][0] # obtinc la classe que sera la key del dict
	query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';" # obtinc el tag que sera la key del dict tmp
	cursor.execute(query)
	for row in cursor.fetchall(): # recorro tots els tags de la imatge
		if mapren.has_key(key): # si la classe ja ha estat declara al dict
			mapren[key].append(row[0]) # poso al final de la llista el nou tag
		else:  # si la clase no ha estat declarada
			
			mapren[key]=row[0]# creo la clase i adjunto el tag
	
	return mapren # retorno mapren
