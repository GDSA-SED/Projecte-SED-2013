def aprenentatge(x,tam,db):
	mapren = dict()
	for image in x: 
		image = image[tam:-4] 
		cursor = db.cursor() 
		query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ str(image) + "';" 
		cursor.execute(query) 
		key=cursor.fetchall()[0][0] 
		query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
		cursor.execute(query)
		for row in cursor.fetchall(): 
			if mapren.has_key(key):				
				if mapren[key].has_key(row[0]): 
					mapren[key][row[0]][0]+=1
				else: 
					mapren[key][row[0]]=[1]				
			else:  
				mapren[key]={row[0]:[1]} 
	
	return mapren
