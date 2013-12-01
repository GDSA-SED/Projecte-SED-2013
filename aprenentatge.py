def aprenentatge(image,mapren,db,count):
	tmp=dict() # creo un dict temporal
	cursor = db.cursor() # obtinc el cursor
	query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ str(image) + "';" # select per obtenir la classe de la imatge
	cursor.execute(query) # executem la query
	key=cursor.fetchall()[0][0] # obtinc la classe que sera la key del dict
	query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';" # obtinc el tag que sera la key del dict tmp
	cursor.execute(query)
	for row in cursor.fetchall(): # recorro tots els tags de la imatge
		if mapren.has_key(key): # si la classe ja ha estat declara al dict
			tmp=mapren[key] # obtinc el dict que hi ha dins del dict, aquest conte tag i repeticions normalitzades per el num total de tags
			if tmp.has_key(row[0]): # si el tag ja existeix li sumo un i el normalitzo
				tmp[row[0]]=((tmp[row[0]]*count)+1)/count
			else: # si no existeix, el creo i el normalitzo
				tmp[row[0]]=1/count
			mapren[key]=tmp
		else:  # si la clase no ha estat declarada
			tmp[row[0]]=1/count; # creo el dict que hi ha dins de mapren amb el tag normalitzat
			mapren[key]=tmp	# creo la clase i poso el dict tmp dins de la classe
	
	return mapren # retorno mapren
