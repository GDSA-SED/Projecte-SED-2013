#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as SQL
import numpy as np
import matplotlib.pyplot as pl
import math as m
import glob as g
import sys
import string as s
from StringIO import StringIO

f=open('vt.txt','w')
db = SQL.connect(host="localhost", user="root", passwd="root",db="gdsa") 
cursor = db.cursor()
path = raw_input( "Insert the path file of the images to clasify, realtive path or absolute path \n")
tam = len(path)+1
x = g.glob(path+"/*.jpg")
for image in x:
	image = image[tam:-4]
	query = "select event_type from sed2013_task2_dataset_train_gs where document_id= '"+ image + "';" 
	cursor.execute(query)
	f.write(image+" "+cursor.fetchall()[0][0]+'\n')
f.close()

file_name = raw_input("Insert the path of the classifier .txt result file (write \"exit\" to leave):")

if file_name != "exit":
        file = open(file_name, 'r') #Open the results .txt file from clasificator in read mode
        cdata = file.readline() #Read the first line content

        #Declaration of the evaluation variables
        pre = [0,0,0,0,0,0,0,0,0] #Precision by clases
        pre_tot = 0 #Total precision
        rec = [0,0,0,0,0,0,0,0,0] #Recall by clases
        rec_tot = 0 #rTotal recall
        F_score = [0,0,0,0,0,0,0,0,0] #F-score by clases
        F_score_tot = 0 #Total F-score
        #Confusion matrix by clases (position 0: true positives, 1: false positives, 2: true negatives, 3: false negatives)
        dict_MC = {"sports":[0,0,0,0], "concert":[0,0,0,0], "exhibition":[0,0,0,0], "protest":[0,0,0,0], "fashion":[0,0,0,0], "conference":[0,0,0,0], "theater_dance":[0,0,0,0], "other":[0,0,0,0], "non_event":[0,0,0,0]}
	cont_imag = 0 #Image clasified countc(needed for NMI calculation)
	dict_cat = {"sports" :set(), "concert":set(), "exhibition":set(), "protest":set(), "fashion":set(), "conference":set(), "theater_dance":set(), "other":set(), "non_event":set()} #Dictionary with ground truth information (needed for NMI calculation)
	dict_clas = {"sports" : set(), "concert":set(), "exhibition":set(), "protest":set(), "fashion":set(), "conference":set(), "theater_dance":set(), "other":set(), "non_event":set()} #Dictionary with clasification information (needed for NMI calculation)

        #Database connection
        while cdata != "": #Read of claisfication .txt fileline by line
		cont_imag += 1 #Image count update
                ID = cdata[0 : cdata.find(" ")] #ID from clasified image
                clas = cdata[cdata.find(" ") + 1 : - 1] #Event from clasified image
		dict_clas[clas].add(ID)
                cursor = db.cursor()
                #Ground truth query of the image with the current ID
                cursor.execute("SELECT event_type FROM sed2013_task2_dataset_train_gs WHERE document_id =" + "'" + ID + "'")
                clas_db = cursor.fetchone()[0] #Ground truth event adquisition
		dict_cat[clas_db].add(ID)

                #True positives,false positives, true negatives and false negatives calculation for each class confusion matrix
                if clas == clas_db:
                        dict_MC[clas][0] += 1
                        for i in range(len(dict_MC)):
                                if dict_MC.keys()[i] != clas:
                                        d = dict_MC.keys()[i]
                                        dict_MC[d][2] += 1
                else:
                        for i in range(len(dict_MC)):
                                if dict_MC.keys()[i] != clas_db and dict_MC.keys()[i] != clas:
                                        d = dict_MC.keys()[i]
                                        dict_MC[d][2] += 1
                        dict_MC[clas_db][3] += 1
                        dict_MC[clas][1] += 1

                cdata = file.readline() #Reading of the next line
        file.close()

        #Precision, recall and F-score calculation using the confusion matrix data
        num_div_p = 0 #Divisor number for calculate the average precision
        num_div_r = 0 #Divisor number for calculate the average recall
        num_div_f = 0 #Divisor number for calculate the average F-score
        for i in range(len(dict_MC)):
                d = dict_MC.keys()[i]
                if dict_MC[d][0] + dict_MC[d][1] != 0:
                        pre[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][1]),5) #Precision by clases (5 decimal precision)
                elif dict_MC[d][1] != 0:
                        pre[i] = 0
                else:
                        pre[i] = "none"
                if dict_MC[d][0] + dict_MC[d][3] != 0:
                        rec[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][3]),5) #Recall by clases (5 decimal precision)
                elif dict_MC[d][3]!= 0:
                        rec[i] = 0
                else:
                        rec[i] = "none"
                if pre[i] != "none" and rec[i] != "none":
                        if pre[i] + rec[i] != 0:
                                F_score[i] = round(2 * pre[i] * rec[i] / (pre[i] + rec[i]),5) #F-Score by clases (5 decimal precision)
                        else:
                                F_score[i] = 0
                else:
                        F_score[i] = "none"
        for i in range(len(dict_MC)):
                if pre[i] != "none":
                        pre_tot = pre[i] + pre_tot #Average precision calculation
                        num_div_p += 1
                if rec[i] != "none":
                        rec_tot = rec[i] + rec_tot #Average Recall Calculation
                        num_div_r += 1
                if F_score[i] != "none":
                        F_score_tot = F_score[i] + F_score_tot #Average F-score calculation
                        num_div_f += 1
        pre_tot = round(pre_tot / num_div_p,5) #NMI average precision (5 decimal precision)
        rec_tot = round(rec_tot / num_div_r,5) #NMI average recall (5 decimal precision)
        F_score_tot = round(F_score_tot / num_div_f,5) #NMI average F-score (5 decimal precision)

	#NMI calculation
	#den1_NMI = 0.0
	#den2_NMI = 0.0
	#num_NMI = 0.0
	#for event_d1 in dict_clas:
	#	den1_NMI += (float(len(dict_clas[event_d1])) / float(cont_imag)) * m.log(float(len(dict_clas[event_d1])) / float(cont_imag),2)
	#	eset = set()
	#	for id_clas in dict_clas[event_d1]:
	#		for event_d2 in dict_cat:
	#			for id_cat in dict_cat[event_d2]:
	#				if id_cat == id_clas:
	#					eset.add(str(event_d2))
	#	for event in eset:
	#		num_NMI += (float(len(dict_clas[event_d1] & dict_cat[event]))/float(cont_imag)) * (m.log((float(cont_imag) * float(len(dict_clas[event_d1] & dict_cat[event]))) / (float(len(dict_clas[event_d1])) * float(len(dict_cat[event]))), 2))
	#for event_d2 in dict_cat:
	#	den2_NMI += (float(len(dict_cat[event_d2])) / float(cont_imag)) * m.log(float(len(dict_cat[event_d2])) / float(cont_imag),2)
	#NMI = round(num_NMI / (((-1)*den1_NMI + (-1)*den2_NMI) / 2), 5) #NMI (5 decimal precision)
	
	#Divergence from a random baseline
	buffer = StringIO()
	sys.stdout = buffer
	sys.argv= ['./eval_sed2013.py','--challenge2','--baseline', './vt.txt','./results/3.1.txt']
	execfile('./eval_sed2013.py')
	sys.stdout = sys.__stdout__
	string = str(buffer.getvalue())
	i = s.find(string,"Divergence F1 per category, average")
	string = string[i:]
	i = s.find(string,"|")
	f = s.find(string,"-")
	divergence = string[i+2:f-3]

        #Evaluation results comparison bar graph
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
        ax.set_title('Evaluation Scores of ' + file_name[10 : -4])
        ax.set_xticks(ind+1.5*width)
        ax.set_xticklabels( ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE'), rotation='vertical')
        ax.legend((bar_p[0], bar_r[0],bar_f[0]), ('Precision', 'Recall', 'F-Score'), loc='center left', bbox_to_anchor=(1, 0.5))
        ax.autoscale(tight=True)
        pl.subplots_adjust(right = 0.85,bottom = 0.35)
	
	#Avaluation results comparison table
        labels_fil = ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE')
        labels_col = ('Precision', 'Recall', 'F-Score','Divergence F-Score')
        val_table = [[pre[8],rec[8],F_score[8],"-"], [pre[4],rec[4],F_score[4],"-"], [pre[7],rec[7],F_score[7],"-"], [pre[2],rec[2],F_score[2],"-"], [pre[3],rec[3],F_score[3],"-"], [pre[0],rec[0],F_score[0],"-"], [pre[5],rec[5],F_score[5],"-"], [pre[1],rec[1],F_score[1],"-"], [pre[6],rec[6],F_score[6],"-"], [pre_tot, rec_tot, F_score_tot,divergence]]
        ax = fig.add_subplot(212)
	ax.axis('off')
        table = ax.table(cellText = val_table, cellLoc = 'center', rowLabels = labels_fil, rowLoc = 'center', colLabels = labels_col,colLoc = 'center', loc = 'bottom')
        pl.show()
