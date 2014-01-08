# -*- coding: utf-8 -*-
import math
import decimal as d
def learning(x,tam,db):
	# dlearn dictionary initialization
	dlearn = dict()
	
	# ctags is a auxiliar variable, type dict
	ctags = dict()
	
	# analazing all the images of directory	
	for image in x:  
		# get name of the image 
		image = image[tam:-4] 
		#initialization of cursor
		cursor = db.cursor() 
		#get the image class
		query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ image + "';" 
		# execute query
		cursor.execute(query) 
		# get the class and save in the key variable
		key=cursor.fetchall()[0][0] 
		# search the tags of the image 
		query = "SELECT tag FROM sed2013_task2_dataset_train_tags where document_id='"+ image + "';"
		# execute query
		cursor.execute(query)
		# wander the tags
		for row in cursor.fetchall():
			row = row[0].lower() 
			# if in dlearn exists the class that is being processed
			if dlearn.has_key(key):
				# if in class is being processed exists the tag, we add 1				
				if dlearn[key].has_key(row): 
					dlearn[key][row]+=1
				#if in class is being processed isn't exist the tag. Initialization of tag to one
				else: 
					dlearn[key][row]=1

					#count the number of the tags that appear in all the classes
					# if the tag is already processed add one
					if ctags.has_key(row):
						ctags[row]+=1;
					# if the tag isn't already processed initialization of tag to one						
					else:
						ctags[row]=1;
			
			else:  
				dlearn[key]={row:1}
				ctags[row]=1
	# calculate the idf to know if the word is uncommon in the classes
	ndocuments = len(dlearn)
	for k in ctags:

		ctags[k]=d.Decimal(math.log10(ndocuments/float(ctags[k]+1)))

	#calculate the tf-idf
	for clas in dlearn:
		ntag=d.Decimal(len(dlearn[clas]))
		amax = 0;
		#search the tag that appear more
		for key in dlearn[clas]:
			if amax < dlearn[clas][key]:
				amax = 	dlearn[clas][key]
		# calculate the tf-idf of this class		
		for tag in ctags:
			if dlearn[clas].has_key(tag):
				dlearn[clas][tag]=float((((d.Decimal(0.5)*dlearn[clas][tag])/ntag)/(amax/ntag)+d.Decimal(0.5))*ctags[tag])	
						 
	return dlearn
