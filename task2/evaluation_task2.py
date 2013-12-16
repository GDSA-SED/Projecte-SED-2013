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
import time

path = "./results/*.txt"
x = g.glob(path)
val_comp = [] #List for saving the avaluation scores of all the assays in order to make a comparison bar graph and table
F1_mean = 0.0
F1_NE_mean = 0.0
acc_mean = 0.0
for file_name in x:
        start = time.time()

        file = f = open(file_name,'rU') #Open the results .txt file from clasificator in read mode
        cdata = file.readline() #Read the first line content

        #Declaration of the evaluation variables
        pre = [0,0,0,0,0,0,0,0,0] #Precision by clases
        pre_tot = 0.0 #Total precision
        rec = [0,0,0,0,0,0,0,0,0] #Recall by clases
        rec_tot = 0.0 #Total recall
        F_score = [0,0,0,0,0,0,0,0,0] #F-score by clases
        F_score_tot = 0 #Total F-score
	acc = [0,0,0,0,0,0,0,0,0] #Accuracy by clases
	acc_tot = 0.0 #Total Accuracy
        #Confusion matrix by clases (list position 0: true positives, 1: false positives, 2: true negatives, 3: false negatives)
        dict_MC = {"sports":[0,0,0,0], "concert":[0,0,0,0], "exhibition":[0,0,0,0], "protest":[0,0,0,0], "fashion":[0,0,0,0], "conference":[0,0,0,0], "theater_dance":[0,0,0,0], "other":[0,0,0,0], "non_event":[0,0,0,0]}

        #Database connection
	db = SQL.connect(host="localhost", user="root", passwd="root",db="GDSA")
        while cdata != "": #Read of claisfication .txt fileline by line
                ID = cdata[0 : cdata.find(" ")] #ID from clasified image
                clas = cdata[cdata.find(" ") + 1 : - 1] #Event from clasified image
                cursor = db.cursor()
                #Ground truth query of the image with the current ID
                cursor.execute("SELECT event_type FROM sed2013_task2_dataset_train_gs WHERE document_id =" + "'" + ID + "'")
                clas_db = cursor.fetchone()[0] #Ground truth event adquisition

                #True positives, false positives, true negatives and false negatives calculation for each class confusion matrix
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

                cdata = file.readline() #Reading the next line
        file.close()

        #Precision, Recall, F-score and Accuracy calculation using the confusion matrix data
        for i in range(len(dict_MC)):
                d = dict_MC.keys()[i]
                if dict_MC[d][0] + dict_MC[d][1] != 0:
                        pre[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][1]),5) #Precision by clases (5 decimal precision)
                else:
                        pre[i] = 0
                if dict_MC[d][0] + dict_MC[d][3] != 0:
                        rec[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][3]),5) #Recall by clases (5 decimal precision)
                else:
                        rec[i] = 0
		if dict_MC[d][0] + dict_MC[d][1] + dict_MC[d][2] + dict_MC[d][3] != 0:
                        acc[i] = round(float(dict_MC[d][0] + dict_MC[d][2]) / (dict_MC[d][0] + dict_MC[d][1] + dict_MC[d][2] + dict_MC[d][3]),5) #Accuracy by clases (5 decimal precision)
                else:
                        acc[i] = 0
                if pre[i] + rec[i] != 0:
                	F_score[i] = round(2 * pre[i] * rec[i] / (pre[i] + rec[i]),5) #F-Score by clases (5 decimal precision)
                else:
                        F_score[i] = 0
        for i in range(len(dict_MC)):
                pre_tot = pre[i] + pre_tot #Average precision calculation
                rec_tot = rec[i] + rec_tot #Average Recall Calculation
		d = dict_MC.keys()[i]
                acc_tot = acc_tot + dict_MC[d][0] #Average Accuracy Calculation
                F_score_tot = F_score[i] + F_score_tot #Average F-score calculation
	num_ima = dict_MC[d][0] + dict_MC[d][1] + dict_MC[d][2] + dict_MC[d][3]
        pre_tot = round(pre_tot / 9,5) #Average Precision (5 decimal precision)
        rec_tot = round(rec_tot / 9,5) #Average Recall (5 decimal precision)
	acc_tot = round(acc_tot / num_ima,5) #Average Accuracy (5 decimal precision)
        F_score_tot = round(F_score_tot / 9,5) #Average F-score (5 decimal precision)

	val_comp.append([F_score_tot, F_score[6], acc_tot])   
for i in range(len(val_comp)):
		F1_mean = F1_mean + val_comp[i][0] #Average F_score of the cross-validation runs
		F1_NE_mean = F1_NE_mean + val_comp[i][1] #Average F_score non_event of the cross-validation runs
		acc_mean = acc_mean + val_comp[i][2] #Average Accuracy of the cross-validation runs
F1_mean = F1_mean / len(val_comp)
F1_NE_mean = F1_NE_mean / len(val_comp)
acc_mean = acc_mean / len(val_comp)

stop = time.time()
print "Total time to evaluate: "+str(stop - start) + " seconds"

#MediaEval 2013 SED results comparison bar graph
val_f = [0.3344, 0.537, 0.4495, 0.5, F1_mean]  
val_fne = [0.7163, 0, 0.8854, 0.95, F1_NE_mean]
val_a = [0, 0.907, 0, 0, acc_mean]
fig = pl.figure(figsize = (15,7))
ind = np.arange(5)
width = 0.20
ax = fig.add_subplot(211)
bar_f = ax.bar(ind, val_f, width, color='r')
bar_fne = ax.bar(ind + width, val_fne, width, color='g')
bar_a = ax.bar(ind + 2 * width, val_a, width, color='b')
ax.set_title('Evaluation Scores MediaEval 2013 SED Comparison' ,fontweight='bold')
ax.set_xticks(ind + 1.5 * width)
ax.set_xticklabels(('CERTH-ITI', 'ADMRG', 'VIT', 'QMUL', '3.1 GDSA'))
ax.legend((bar_f[0], bar_fne[0], bar_a[0]), ('F1-Score','F1-Non_event', 'Accuracy'), loc='center left', bbox_to_anchor=(1, 0.5))
ax.autoscale(tight=True)
pl.subplots_adjust(right = 0.85,bottom = 0.35)

#MediaEval 2013 SED results comparison table
val_f = [0.3344, 0.537, 0.4495, 0.5, F1_mean]  
val_fne = [0.7163, "none", 0.8854, 0.95, F1_NE_mean]
val_a = ["none", 0.907, "none", "none", acc_mean]
val_tab= []
for i in range (5):
	val_tab.append([val_f[i], val_fne[i], val_a[i]])
labels_fil = ('CERTH-ITI', 'ADMRG', 'VIT', 'QMUL', '3.1 GDSA')
labels_col = (['F1-Score', 'F1-Non_event', 'Accuracy'])
ax = fig.add_subplot(212)
ax.axis('off')
table = ax.table(cellText = val_tab, cellLoc = 'center', rowLabels = labels_fil, rowLoc = 'center', colLabels = labels_col, loc = 'bottom')

pl.show()
