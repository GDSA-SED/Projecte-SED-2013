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

path = "./results/*.txt"
x = g.glob(path)
for file_name in x:
        
        file = open(file_name, 'r') #Open the results .txt file from clasificator in read mode
        cdata = file.readline() #Read the first line content

        #Declaration of the evaluation variables
        pre = [0,0,0,0,0,0,0,0,0] #Precision by clases
        pre_tot = 0 #Total precision
        rec = [0,0,0,0,0,0,0,0,0] #Recall by clases
        rec_tot = 0 #rTotal recall
        F_score = [0,0,0,0,0,0,0,0,0] #F-score by clases
        F_score_tot = 0 #Total F-score
	acc = [0,0,0,0,0,0,0,0,0] #Accuracy by clases
	acc_tot = 0 #Total Accuracy
        #Confusion matrix by clases (position 0: true positives, 1: false positives, 2: true negatives, 3: false negatives)
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
        num_div_p = 0 #Divisor number for calculate the average Precision
        num_div_r = 0 #Divisor number for calculate the average Recall
        num_div_f = 0 #Divisor number for calculate the average F-score
	num_div_a = 0 #Divisor number for calculate the average Accuracy
        for i in range(len(dict_MC)):
                d = dict_MC.keys()[i]
                if dict_MC[d][0] + dict_MC[d][1] != 0:
                        pre[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][1]),5) #Precision by clases (5 decimal precision)
                else:
                        pre[i] = "none"
                if dict_MC[d][0] + dict_MC[d][3] != 0:
                        rec[i] = round(float(dict_MC[d][0]) / (dict_MC[d][0] + dict_MC[d][3]),5) #Recall by clases (5 decimal precision)
                else:
                        rec[i] = "none"
		if dict_MC[d][0] + dict_MC[d][1] + dict_MC[d][2] + dict_MC[d][3] != 0:
                        acc[i] = round(float(dict_MC[d][0] + dict_MC[d][2]) / (dict_MC[d][0] + dict_MC[d][1] + dict_MC[d][2] + dict_MC[d][3]),5) #Accuracy by clases (5 decimal precision)
                else:
                        acc[i] = "none"
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
		if acc[i] != "none":
                        acc_tot = acc[i] + acc_tot #Average Accuracy Calculation
                        num_div_a += 1
                if F_score[i] != "none":
                        F_score_tot = F_score[i] + F_score_tot #Average F-score calculation
                        num_div_f += 1
        pre_tot = round(pre_tot / num_div_p,5) #Average Precision (5 decimal precision)
        rec_tot = round(rec_tot / num_div_r,5) #Average Recall (5 decimal precision)
	acc_tot = round(acc_tot / num_div_a,5) #Average Accuracy (5 decimal precision)
        F_score_tot = round(F_score_tot / num_div_f,5) #Average F-score (5 decimal precision)

        #Evaluation results comparison bar graph
        val_table = [[F_score[8],acc[8]], [F_score[4], acc[4]], [F_score[7], acc[7]], [F_score[2], acc[2]], [F_score[3], acc[3]], [F_score[0], acc[0]], [F_score[5], acc[5]], [F_score[1], acc[1]], [F_score[6], acc[6]], [F_score_tot, acc_tot]]
        n = np.array(range(10))
        val_f = [0,0,0,0,0,0,0,0,0,0]
	val_a = [0,0,0,0,0,0,0,0,0,0]
        for i in range(10):
                for j in range(2):
                        if val_table[i][j] == "none":
                                val_table[i][j] = 0
                val_f[i] = val_table[i][0]
                val_a[i] = val_table[i][1]
        fig = pl.figure(figsize = (12,7))
        ind = np.arange(10)
        width = 0.25
        ax = fig.add_subplot(211)
        bar_f = ax.bar(ind, val_f, width, color='r')
        bar_a = ax.bar(ind+width, val_a, width, color='b')
        ax.set_title('Evaluation Scores of ' + file_name[10 : -4])
        ax.set_xticks(ind+1.5*width)
        ax.set_xticklabels( ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE'), rotation='vertical')
        ax.legend((bar_f[0], bar_a[0]), ('F1-Score', 'Accuracy'), loc='center left', bbox_to_anchor=(1, 0.5))
        ax.autoscale(tight=True)
        pl.subplots_adjust(right = 0.85,bottom = 0.35)
        
        #Evaluation results comparison table
	val_table = [[F_score[8],acc[8]], [F_score[4], acc[4]], [F_score[7], acc[7]], [F_score[2], acc[2]], [F_score[3], acc[3]], [F_score[0], acc[0]], [F_score[5], acc[5]], [F_score[1], acc[1]], [F_score[6], acc[6]], [F_score_tot, acc_tot]]
        labels_fil = ('sports', 'concert', 'exhibition', 'protest', 'fashion', 'conference', 'theater_dance', 'other', 'non_event', 'AVERAGE')
        labels_col = ('F1-Score','Accuracy')
        ax = fig.add_subplot(212)
        ax.axis('off')
        table = ax.table(cellText = val_table, cellLoc = 'center', rowLabels = labels_fil, rowLoc = 'center', colLabels = labels_col, colLoc = 'center', loc = 'bottom')
        pl.show()