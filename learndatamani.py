# -*- coding: UTF-8 -*-
import json
def serialization(mapren,nfile):
	f = open(nfile, 'w')
	json.dump(mapren, f, encoding="iso-8859-15")
	f.close()

def deserialization(nfile):
	f = open(nfile, 'r')
	mapren=json.load(f,encoding="iso-8859-15")
	f.close()
	return mapren
