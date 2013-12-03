def clasificador(mapren,image,db)

  # Busquem els tags de la imatge a classificar
  query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
	cursor.execute(query)
	
	# Analitzem els tags de la imatge
  for row in cursor.fetchall():
    
