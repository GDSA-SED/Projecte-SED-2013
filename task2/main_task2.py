#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob as g
import MySQLdb as sql
import learning as learn
import classifier_task2 as clasi
import learndatamani as l
import time
import random as r

#copyright of our code
print "SED-Project Copyright (C) 2013 Albert Mosella, Albert Montes Jordi Yáñez, David Márquez"

#Establish the connection with our mysql database
db = sql.connect(host="localhost", user="root", passwd="root",db="GDSA")


# Define path and size of the ID of the image
path = './image/*.jpg'
tam = len(path) - 5
x = g.glob(path)
for i in range (5): #5 loop cross-validation
	xl = [] #70% image data learning
	xc = [] #30% image data testing
	ind = r.randint(0, len(x) - 1) #First random image of the list
	cont = 0
	while cont < int(0.7 * len(x)):
		xl.append(x[ind])
		if ind == len(x) - 1:
			ind = 0
		else:
			ind += 1
		cont += 1
	while cont < len(x):
		xc.append(x[ind])
		if ind == len(x) - 1:
			ind = 0
		else:
			ind += 1
		cont += 1

	nfile = raw_input("Insert the name of the learning file: ")

	#if this learning file doesn't exist we create it
	if not os.path.isfile(nfile):
		start = time.time()
		dlearn = learn.learning(xl,tam,db)
		stop = time.time()
		l.serialization(dlearn,nfile)
		print "Total time to learn: "+str(stop - start) + " seconds"
	else :
		while os.path.isfile(nfile):
			nfile = raw_input("That file already exists. Insert a valid name of the learning file: ")
			if not os.path.isfile(nfile):
				start = time.time()
	       			dlearn = learn.learning(xl,tam,db)
				stop = time.time()
				l.serialization(dlearn,nfile)
				print "Total time to learning: "+str(stop - start) + " seconds"
				break

	#Image clasification
	start = time.time()
	clasi.classifier(dlearn,xc,db,tam,i)
	stop = time.time()
	print "Total time to classify: "+str(stop - start) + " seconds"
#close the database
db.close()
