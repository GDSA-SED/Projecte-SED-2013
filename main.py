#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob as g
import MySQLdb as sql
import learning as learn
import clasificator as clasi
import learndatamani as l

# Define path and size of the ID of the image
path = './image/*.jpg'
tam = len(path) - 5

x = g.glob(path)

#Establish the connection with our mysql database
db = sql.connect(host="localhost", user="root", passwd="root",db="gdsa")


nfile = raw_input("Insert the name of the learning file: ")

#if this learning file doesn't exist we create it
if not os.path.isfile(nfile):
        dlearn = learn.learning(x,tam,db)
        l.serialization(dlearn,nfile)
else :
        dlearn= l.deserialization(nfile)

           
path = raw_input( "Insert the path of the folder of images that you want to clasificate, the path can be ralative or absolut: \n")
tam = len(path)+1
x = g.glob(path+"/*.jpg")

#Image clasification
clasi.clasificator(dlearn,x,db,tam)

#close the database
db.close()
