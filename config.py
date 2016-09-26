#!/usr/bin/env python
# -*- coding: utf-8 -*-

#	***style***
#	1. ツイ消しは愛と青春の日々機能 ON/OFF
#	2. メンヘラちゃん機能 ON/OFF
#	3. ガン無視機能　ON/OFF
#
import json
import sys
import os.path
import miniconf
from getch import _Getch

class Config:
	def __init__(self):
		if not os.path.isfile('./.labotter.cfg'):
			self.config	=	{"twikeshi":True,"menhera":False,"through":False}
		else:
			fi = open('./.labotter.cfg', 'r')
			data = fi.read()
			self.config = miniconf.load(data)

	def setting(self,config):
		#設定変更
		sys.stdout.write("current_settings\n")
		sys.stdout.write("settings@current:~/type_number_to_change_configuration \n")
		while True:
			sys.stdout.write("\rsettings@current:~/1-TwiKeshi_%s  2-Menhera_%s  3-Through_%s -> " %	(self.config["twikeshi"],self.config["menhera"],self.config["through"]))
			sys.stdout.flush()
			getch	=	_Getch()
			cfg		=	getch()
			print cfg
			if cfg == "1":
				self.config["twikeshi"]	=	not self.config["twikeshi"]
			elif cfg == "2":
				self.config["menhera"]	=	not self.config["menhera"]
			elif cfg == "3":
				self.config["through"]	=	not self.config["through"]
			else:
				break
		#設定書き込み
		data = miniconf.dump(self.config)
		fo = open('./.labotter.cfg', 'w')
		fo.write(data)
		fo.close()
		#終了
		return self.config

