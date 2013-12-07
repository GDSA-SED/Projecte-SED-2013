# -*- coding: UTF-8 -*-
import json
def serialization(mapren,fitxer):
	f = open(fitxer, 'w')
	json.dump(mapren, f, encoding="iso-8859-15")
	f.close()

def deserialization(fitxer):
	f = open(fitxer, 'r')
	mapren=json.load(f,encoding="iso-8859-15")
	f.close()
	return mapren
