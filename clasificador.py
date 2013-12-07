# -*- coding: utf-8 -*-
import math


def clasificador(mapren,x,db,tam):
	list_aux=[]
    	li=[]
    	results=[]
  	cont = 0
  	numtags = 0
    	event= ""
    	for image in x:
        	image = image[tam+1:-4]
        	# Busquem els tags de la imatge a classificar
		cursor = db.cursor()
        	query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
        	cursor.execute(query)
            
        	# Analitzem els tags de la imatge
                
        	for k in mapren: #retorna el valor de les key del mapren.
                	
                	for row in cursor.fetchall():
                		# row[0] és on esta el tag
                    		#conto el numero de tags que te la imatge ambun contador
                    		numtags+=1
		    		
                    
                    		#per a cada tag, conto si surt al mapren i guardo el tfidf
                    		if mapren[k].has_key(row[0]):
                        
                        		cont+=1
                        		tfidf+=mapren[ k ][ row[0] ]
                
                		#Si el numero de tags que hi ha a mapren es major a 0.5 (normalitzat)
                		#guardem en una llista: la classe, el contador de tags i el tfidf
               			if cont/numtags > 0.5:
                    
                    			list_aux =[k,cont,tfidf]
                
                		#guardem en una llista totes les possibles classes
                		li=li.append(list_aux)
                
        	n=len(li)
                
       		ntag=0
		
        	for i in range(0,n):
						
			
            		li_aux=li[i]        
            		#mirem sols els tags que apareixen. si hi ha un numbre máxim de tags l'event sera el relacionat amb aquest ntag
            		if li_aux[1]  > ntag:
                
				ntag= li_aux[1]
                
				event= li_aux[0]     
                    
            		#En cas d'empat en ntag o que ntg sigui 0:
            		if li_aux[1] == ntag:
                        
            			#si ntag és 0 el classifiquem com a not event directament
                		if ntag == 0:
                			event = "not event"
                        
                		# si ntag és diferent a 0, vol dir que hi ha empat entre classes. 
                		#Llavors mirem el tfidf y triarem el que tingui un idf major coma classe seleccionada
                		else:
					li_aux2= li[i-1]
                			if li_aux2[2] > li_aux[2] :
                        			event = li_aux2[0] 
					else:
						event=li_aux[0]
	    

		results+= [ [image, event] ]            
    
	return results
