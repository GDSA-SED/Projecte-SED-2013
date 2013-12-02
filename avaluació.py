#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as SQL

nom = raw_input("Introdueixi el nom del fitxer que conte els resultats de les imatges clasificades (escrigui exit per sortir):")
if nom != "exit":
	fitxer = open(nom, 'r') #Obrim el fitxer de dades .txt del clasificador end mode lectura
	cdata = fitxer.readline() #Llegim el contingut de la primera línia del fitxer

	#Declaració de les variables d'avaluació a calcular
	pre = [0,0,0,0,0,0,0,0,0] #precisió per clases
	pre_tot = 0 #precisió total
	rec = [0,0,0,0,0,0,0,0,0] #record per clases
	rec_tot = 0 #record total
	F_score = [0,0,0,0,0,0,0,0,0] #F-score per clases
	F_score_tot = 0 #F-score total
	#Matrius de confusió per clases (posició 0: positius certs, 1: positius falsos, 2: negatius certs, 3: negatius falsos)
	dict_MC = {"sports":[0,0,0,0], "concert":[0,0,0,0], "exhibition":[0,0,0,0], "protest":[0,0,0,0], "fashion":[0,0,0,0], "conference":[0,0,0,0], "theater_dance":[0,0,0,0], "other":[0,0,0,0], "non_event":[0,0,0,0]}

	#Connexió a la base de dades
	db = SQL.connect(host="localhost", user="root", passwd="root",db="GDSA") 
	while cdata != "": #Lectura línia a línia el fitxer .txt fins al final
		ID = cdata[0 : cdata.find(" ")] #Substring que correspon a la ID de la imatge classificada
		classe = cdata[cdata.find(" ") + 1 : - 1] #Substring que correspon a la clase de la imatge classificada
		cursor = db.cursor()
		#Consulta a la base de dades la veritat terreny de la imatge a través de la seva ID
		cursor.execute("SELECT event_type FROM sed2013_task2_dataset_train_gs WHERE document_id =" + "'" + ID + "'")
		classe_db = cursor.fetchone()[0] #Adquisició de la clase de la imatge de la base de dades

		#Càlcul dels positius certs, positius falsos, negatius certs i negatius falsos per a cada matriu de confusió de cada classe 
		if classe == classe_db:
			dict_MC[classe][0] += 1
			for i in range(len(dict_MC)):
				if dict_MC.keys()[i] != classe:
					d = dict_MC.keys()[i]
					dict_MC[d][2] += 1
		else:
			for i in range(len(dict_MC)):
				if dict_MC.keys()[i] != classe_db and dict_MC.keys()[i] != classe:
					d = dict_MC.keys()[i]
					dict_MC[d][2] += 1
			dict_MC[classe_db][3] += 1
			dict_MC[classe][1] += 1

		cdata = fitxer.readline() #Lectura de la següent línia

	#Càlcul dels paràmetres de precisió, record i F-Score a partir de les matrius de confusió
	for i in range(len(dict_MC)): 
		d = dict_MC.keys()[i]
		if dict_MC[d][0] + dict_MC[d][1] != 0:
			pre[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][1]),5) #Precisió per clases (5 decimals precisió)
		else:
			pre[i] = 0
		if dict_MC[d][0] + dict_MC[d][3] != 0:
			rec[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][3]),5) #Record per clases (5 decimals precisió)
		else:
			rec[i] = 0
		if pre[i] + rec[i] != 0:
			F_score[i] = round(2 * pre[i] * rec[i] / (pre[i] + rec[i]),5) #F-Score  per clases (5 decimals precisió)
		else:
			F_score[i] = 0
		pre_tot = pre[i] / len(dict_MC) + pre_tot #Càlcul de la precisió total
		rec_tot = rec[i] / len(dict_MC) + rec_tot #Càlcul del record total
		F_score_tot = F_score[i] / len(dict_MC) + F_score_tot #Càlcul de la F-Score total
	pre_tot = round(pre_tot,5) #Precisió total normalitzada (5 decimals precisió)
	rec_tot = round(rec_tot,5) #Record total normalitzat (5 decimals precisió)
	F_score_tot = round(F_score_tot,5) #F-Score total normalitzada (5 decimals precisió)

	print "Matrius de confusió:", dict_MC
	print "Precisió per clases:", pre
	print "Record per clases:", rec
	print "Precisió total:", pre_tot
	print "Record total:", rec_tot
	print "F-Score per clases:", F_score
	print "F-Score total:", F_score_tot
	fitxer.close()
