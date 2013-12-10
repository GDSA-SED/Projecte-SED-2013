#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as SQL
import numpy as np
import matplotlib.pyplot as pl
import math as m

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
	cont_imag = 0 #contador de les imatges classificades (necessari pel NMI)
	dict_cat = {"sports" :set(), "concert":set(), "exhibition":set(), "protest":set(), "fashion":set(), "conference":set(), "theater_dance":set(), "other":set(), "non_event":set()} #Diccionari amb informació de la veritat terreny (necessari pel NMI)
	dict_clas = {"sports" : set(), "concert":set(), "exhibition":set(), "protest":set(), "fashion":set(), "conference":set(), "theater_dance":set(), "other":set(), "non_event":set()} #Diccionari amb informació de la clasificació (necessari pel NMI)

        #Connexió a la base de dades
        db = SQL.connect(host="localhost", user="root", passwd="root",db="gdsa")
        while cdata != "": #Lectura línia a línia el fitxer .txt fins al final
		cont_imag += 1 #Actualitzem el contador d'imatges
                ID = cdata[0 : cdata.find(" ")] #Substring que correspon a la ID de la imatge classificada
                classe = cdata[cdata.find(" ") + 1 : - 1] #Substring que correspon a la clase de la imatge classificada
		dict_clas[classe].add(ID)
                cursor = db.cursor()
                #Consulta a la base de dades la veritat terreny de la imatge a través de la seva ID
                cursor.execute("SELECT event_type FROM sed2013_task2_dataset_train_gs WHERE document_id =" + "'" + ID + "'")
                classe_db = cursor.fetchone()[0] #Adquisició de la clase de la imatge de la base de dades
		dict_cat[classe_db].add(ID)

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
        fitxer.close()

        #Càlcul dels paràmetres de precisió, record i F-Score a partir de les matrius de confusió
        num_div_p = 0 #Número divisori per calcular la mitjana de precisió
        num_div_r = 0 #Número divisori per calcular la mitjana de record
        num_div_f = 0 #Número divisori per calcular la mitjana de F-score
        for i in range(len(dict_MC)):
                d = dict_MC.keys()[i]
                if dict_MC[d][0] + dict_MC[d][1] != 0:
                        pre[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][1]),5) #Precisió per clases (5 decimals precisió)
                elif dict_MC[d][1] != 0:
                        pre[i] = 0
                else:
                        pre[i] = "none"
                if dict_MC[d][0] + dict_MC[d][3] != 0:
                        rec[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][3]),5) #Record per clases (5 decimals precisió)
                elif dict_MC[d][3]!= 0:
                        rec[i] = 0
                else:
                        rec[i] = "none"
                if pre[i] != "none" and rec[i] != "none":
                        if pre[i] + rec[i] != 0:
                                F_score[i] = round(2 * pre[i] * rec[i] / (pre[i] + rec[i]),5) #F-Score per clases (5 decimals precisió)
                        else:
                                F_score[i] = 0
                else:
                        F_score[i] = "none"
        for i in range(len(dict_MC)):
                if pre[i] != "none":
                        pre_tot = pre[i] + pre_tot #Càlcul de la precisió total
                        num_div_p += 1
                if rec[i] != "none":
                        rec_tot = rec[i] + rec_tot #Càlcul del record total
                        num_div_r += 1
                if F_score[i] != "none":
                        F_score_tot = F_score[i] + F_score_tot #Càlcul de la F-Score total
                        num_div_f += 1
        pre_tot = round(pre_tot / num_div_p,5) #Precisió total normalitzada (5 decimals precisió)
        rec_tot = round(rec_tot / num_div_r,5) #Record total normalitzat (5 decimals precisió)
        F_score_tot = round(F_score_tot / num_div_f,5) #F-Score total normalitzada (5 decimals precisió)

	#Càlcul NMI
	den1_nmi = 0.0
	den2_nmi = 0.0
	num_nmi = 0.0
	for event_d1 in dict_clas:
		den1_nmi += (float(len(dict_clas[event_d1])) / float(cont_imag)) * m.log(float(len(dict_clas[event_d1])) / float(cont_imag),2)
		eset = set()
		for id_clas in dict_clas[event_d1]:
			for event_d2 in dict_cat:
				for id_cat in dict_cat[event_d2]:
					if id_cat == id_clas:
						eset.add(str(event_d2))
		for event in eset:
			num_nmi += (float(len(dict_clas[event_d1] & dict_cat[event]))/float(cont_imag)) * (m.log((float(cont_imag) * float(len(dict_clas[event_d1] & dict_cat[event]))) / (float(len(dict_clas[event_d1])) * float(len(dict_cat[event]))), 2))
	for event_d2 in dict_cat:
		den2_nmi += (float(len(dict_cat[event_d2])) / float(cont_imag)) * m.log(float(len(dict_cat[event_d2])) / float(cont_imag),2)
	nmi = round(num_nmi / (((-1)*den1_nmi + (-1)*den2_nmi) / 2), 5) #NMI (5 decimals precisió)
	
        #Creació d'una gràfica amb els resultats obtinguts a l'avaluació
	val_table = [[pre[8],rec[8],F_score[8]], [pre[4],rec[4],F_score[4]], [pre[7],rec[7],F_score[7]], [pre[2],rec[2],F_score[2]], [pre[3],rec[3],F_score[3]], [pre[0],rec[0],F_score[0]], [pre[5],rec[5],F_score[5]], [pre[1],rec[1],F_score[1]], [pre[6],rec[6],F_score[6]], [pre_tot, rec_tot, F_score_tot]]
	n = np.array(range(10))
        val_p = [0,0,0,0,0,0,0,0,0,0]
        val_r = [0,0,0,0,0,0,0,0,0,0]
        val_f = [0,0,0,0,0,0,0,0,0,0]
        for i in range(10):
                for j in range(3):
                        if val_table[i][j] == "none":
                                val_table[i][j] = 0
                val_p[i] = val_table[i][0]
                val_r[i] = val_table[i][1]
                val_f[i] = val_table[i][2]
	fig = pl.figure(figsize = (12,7))
        ind = np.arange(10)
        width = 0.25
        ax = fig.add_subplot(211)
        bar_p = ax.bar(ind, val_p, width, color='r')
        bar_r = ax.bar(ind+width, val_r, width, color='b')
        bar_f = ax.bar(ind+2*width, val_f, width, color='g')
        ax.set_title('Avaluation Scores')
        ax.set_xticks(ind+1.5*width)
        ax.set_xticklabels( ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE'), rotation='vertical')
        ax.legend((bar_p[0], bar_r[0],bar_f[0]), ('Precision', 'Recall', 'F-Score'), loc='center left', bbox_to_anchor=(1, 0.5))
        ax.autoscale(tight=True)
        pl.subplots_adjust(right = 0.85,bottom = 0.35)

	#Creació d'una taula amb els resultats obtinguts a l'avaluació
        etiquetas_fil = ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE')
        etiquetas_col = ('Precision', 'Recall', 'F-Score','NMI')
        val_table = [[pre[8],rec[8],F_score[8],"-"], [pre[4],rec[4],F_score[4],"-"], [pre[7],rec[7],F_score[7],"-"], [pre[2],rec[2],F_score[2],"-"], [pre[3],rec[3],F_score[3],"-"], [pre[0],rec[0],F_score[0],"-"], [pre[5],rec[5],F_score[5],"-"], [pre[1],rec[1],F_score[1],"-"], [pre[6],rec[6],F_score[6],"-"], [pre_tot, rec_tot, F_score_tot,nmi]]
        ax = fig.add_subplot(212)
	ax.axis('off')
        table = ax.table(cellText = val_table, cellLoc = 'center', rowLabels = etiquetas_fil, rowLoc = 'center', colLabels = etiquetas_col,colLoc = 'center', loc = 'bottom')
        pl.show()
