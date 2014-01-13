#!/usr/bin/env python

import sys
import os
import string
import pifacecad
import pyttsx

def say (phrase):
	print phrase
	cmd = '/home/pi/robot/buff_speech.sh "{0}" 2>/dev/null'.format(phrase)
	os.system(cmd)

def screen_say (phrase):
	cad.lcd.clear()
        print phrase
        cad.lcd.write(phrase)

	
def load_stock (stockfile):
	stockitems = {}
	f = open(stockfile, mode='r')
	for line in f:
		current = line.split (',')
		stockitems[current[0]] = [current[1], current[2].rstrip()]
	screen_say ("Loaded %d known\nitems" %  len(stockitems))
	say ("Loaded %d known items" %  len(stockitems))
	return stockitems


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.clear()

screen_say ("Hello. I am\nRound Eyed Robo")
say ("Hello. I am Round Eyed Robo")
screen_say ("Initializing")
say ("Initializing")
stock = load_stock('/home/pi/robot/stocklist')

tmp_code = sys.stdin.readline()
barcode = tmp_code.rstrip()

while barcode:
	if not stock.has_key(barcode):
		screen_say ("Scanned an\nunknown item.")
		say ("Scanned an unknown item.")
	else:
		details = stock[barcode]
		product_name = details[0]

		if details[1] == "PC":	
			recycle = "paper and card"
		elif details[1] == "PL":
			recycle = "plastic"
		else:
			recycle = "metal"

	screen_say ("{0}\n{1}".format(product_name, recycle))
	say ("Scanned {0} which is recyclable as {1}.".format(product_name, recycle))


	tmp_code = sys.stdin.readline()
	barcode = tmp_code.rstrip()

